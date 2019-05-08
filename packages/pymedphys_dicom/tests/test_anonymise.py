import os

from copy import deepcopy
from os import makedirs
from os.path import abspath, basename, dirname, exists, join as pjoin
from shutil import copyfile
import subprocess
from uuid import uuid4

import pydicom
from pydicom.datadict import tag_for_keyword
from pydicom.dataset import Dataset, DataElement
from pydicom.filereader import read_file_meta_info
import pytest

from pymedphys_dicom.dicom import (
    anonymise_dataset,
    anonymise_directory,
    anonymise_file,
    BaselineDicomDictionary,
    BASELINE_KEYWORD_VR_DICT,
    dicom_dataset_from_dict,
    IDENTIFYING_KEYWORDS,
    is_anonymised_dataset,
    is_anonymised_directory,
    is_anonymised_file,
    label_dicom_filepath_as_anonymised
)
from pymedphys_utilities.utilities import remove_file, remove_dir

HERE = dirname(abspath(__file__))
DATA_DIR = pjoin(HERE, 'data', 'anonymise')
test_filepath = pjoin(DATA_DIR, "RP.almost_anonymised.dcm")
test_anon_basename = \
    "RP.1.2.246.352.71.5.53598612033.430805.20190416135558_Anonymised.dcm"
test_anon_filepath = pjoin(DATA_DIR, test_anon_basename)
file_meta = read_file_meta_info(test_filepath)
temp_dirpath = pjoin(DATA_DIR, 'temp_{}'.format(uuid4()))
temp_filepath = pjoin(temp_dirpath, "test.dcm")

VR_NON_ANONYMOUS_REPLACEMENT_VALUE_DICT = {
    'AS': "1Y",
    'CS': "SMITH",
    'DA': "20190429",
    'DT': "20190429000700.000000",
    'LO': "Smith",
    'PN': "Smith",
    'SH': "Smith",
    'SQ': [Dataset(), Dataset()],
    'ST': "Smith",
    'TM': "000700.000000",
    'UI': "11111118"}


def _check_is_anonymised_dataset_file_and_dir(ds, anon_is_expected=True,
                                              ignore_private_tags=False):
    try:
        makedirs(temp_dirpath, exist_ok=True)
        ds.is_little_endian = True
        ds.is_implicit_VR = True
        ds.file_meta = file_meta
        ds.save_as(temp_filepath, write_like_original=False)

        if anon_is_expected:
            assert is_anonymised_dataset(ds, ignore_private_tags)
            assert is_anonymised_file(temp_filepath, ignore_private_tags)
            assert is_anonymised_directory(temp_dirpath,
                                           ignore_private_tags)
        else:
            assert not is_anonymised_dataset(ds, ignore_private_tags)
            assert not is_anonymised_file(temp_filepath,
                                          ignore_private_tags)
            assert not is_anonymised_directory(temp_dirpath,
                                               ignore_private_tags)
    finally:
        remove_file(temp_filepath)
        remove_dir(temp_dirpath)


def _get_non_anonymous_replacement_value(keyword):
    """Get an appropriate dummy non-anonymised value for a DICOM element based
    on its value representation (VR)"""
    vr = BASELINE_KEYWORD_VR_DICT[keyword]
    return VR_NON_ANONYMOUS_REPLACEMENT_VALUE_DICT[vr]


def test_anonymise_dataset_and_all_is_anonymised_functions():

    # Create dict with one instance of every identifying keyword and
    # run basic anonymisation tests
    non_anon_dict = dict.fromkeys(IDENTIFYING_KEYWORDS)

    for key in non_anon_dict:
        non_anon_dict[key] = _get_non_anonymous_replacement_value(key)

    ds = dicom_dataset_from_dict(non_anon_dict)
    _check_is_anonymised_dataset_file_and_dir(ds, anon_is_expected=False)

    ds_anon = anonymise_dataset(ds)
    _check_is_anonymised_dataset_file_and_dir(ds_anon, anon_is_expected=True)

    # Test anonymisation (and check thereof) for each identifying
    # element individually.
    for elem in ds_anon.iterall():
        ds_single_non_anon_value = deepcopy(ds_anon)
        setattr(ds_single_non_anon_value,
                elem.keyword,
                _get_non_anonymous_replacement_value(elem.keyword))
        _check_is_anonymised_dataset_file_and_dir(ds_single_non_anon_value,
                                                  anon_is_expected=False)

        ds_single_anon = anonymise_dataset(ds_single_non_anon_value)
        _check_is_anonymised_dataset_file_and_dir(ds_single_anon,
                                                  anon_is_expected=True)

    # Test correct handling of private tags
    ds_anon.add(DataElement(0x0043102b, 'SS', [4, 4, 0, 0]))
    _check_is_anonymised_dataset_file_and_dir(ds_anon, anon_is_expected=False,
                                              ignore_private_tags=False)
    _check_is_anonymised_dataset_file_and_dir(ds_anon, anon_is_expected=True,
                                              ignore_private_tags=True)

    ds_anon.remove_private_tags()
    _check_is_anonymised_dataset_file_and_dir(ds_anon, anon_is_expected=True,
                                              ignore_private_tags=False)

    # Test blank anonymisation
    # # Sanity check
    _check_is_anonymised_dataset_file_and_dir(ds, anon_is_expected=False)

    ds_anon_blank = anonymise_dataset(ds, replace_values=False)
    _check_is_anonymised_dataset_file_and_dir(
        ds_anon_blank, anon_is_expected=True)

    # Test handling of unknown tags by removing PatientName from
    # baseline dict
    patient_name_tag = tag_for_keyword('PatientName')

    try:
        patient_name = BaselineDicomDictionary.pop(patient_name_tag)

        with pytest.raises(ValueError) as e_info:
            anonymise_dataset(ds)
        assert str(e_info).count("At least one of the non-private tags "
                                 "within your DICOM file is not within "
                                 "PyMedPhys's copy of the DICOM dictionary.")

        ds_anon_delete_unknown = anonymise_dataset(ds,
                                                   delete_unknown_tags=True)
        _check_is_anonymised_dataset_file_and_dir(ds_anon_delete_unknown,
                                                  anon_is_expected=True)
        with pytest.raises(AttributeError) as e_info:
            ds_anon_delete_unknown.PatientName
        assert str(e_info).count("'Dataset' object has no attribute "
                                 "'PatientName'")

        ds_anon_ignore_unknown = anonymise_dataset(ds,
                                                   delete_unknown_tags=False)
        _check_is_anonymised_dataset_file_and_dir(ds_anon_ignore_unknown,
                                                  anon_is_expected=True)
        assert patient_name_tag in ds_anon_ignore_unknown

    finally:
        BaselineDicomDictionary.setdefault(patient_name_tag, patient_name)

    # Test copy_dataset=False:
    anonymise_dataset(ds, copy_dataset=False)
    assert is_anonymised_dataset(ds)


def test_anonymise_file():
    assert not is_anonymised_file(test_filepath)

    try:
        # Private tag handling
        anon_private_filepath = anonymise_file(test_filepath,
                                               delete_private_tags=False)
        assert not is_anonymised_file(anon_private_filepath,
                                      ignore_private_tags=False)
        assert is_anonymised_file(anon_private_filepath,
                                  ignore_private_tags=True)

        anon_private_filepath = anonymise_file(test_filepath,
                                               delete_private_tags=True)
        assert is_anonymised_file(anon_private_filepath,
                                  ignore_private_tags=False)

        # Filename is anonymised?
        assert basename(anon_private_filepath) == test_anon_basename

        # Deletion of original file
        temp_basename = "{}_{}.dcm".format(
            '.'.join(test_filepath.split('.')[:-1]),
            uuid4())
        temp_filepath = pjoin(dirname(test_filepath), temp_basename)
        copyfile(test_filepath, temp_filepath)

        anon_filepath_orig = anonymise_file(temp_filepath,
                                            delete_original_file=True)
        assert is_anonymised_file(anon_filepath_orig)
        assert not exists(temp_filepath)

        # Preservation of filename if desired
        expected_filepath = "{}_Anonymised.dcm".format(
            '.'.join(test_filepath.split('.')[:-1]))
        anon_filepath_pres = anonymise_file(test_filepath,
                                            anonymise_filename=False)
        assert anon_filepath_pres == expected_filepath

    finally:
        remove_file(temp_filepath)
        remove_file(anon_private_filepath)
        remove_file(anon_filepath_orig)
        remove_file(anon_filepath_pres)


def test_anonymise_directory():
    temp_anon_filepath = label_dicom_filepath_as_anonymised(temp_filepath)
    try:
        makedirs(temp_dirpath, exist_ok=True)
        copyfile(test_filepath, temp_filepath)
        assert not is_anonymised_directory(temp_dirpath)

        # Test file deletion
        anonymise_directory(temp_dirpath, delete_original_files=False,
                            anonymise_filenames=False)
        # # File should be anonymised but not dir, since original file
        # # is still present.
        assert is_anonymised_file(temp_anon_filepath)
        assert exists(temp_filepath)
        assert not is_anonymised_directory(temp_dirpath)

        remove_file(temp_anon_filepath)
        anonymise_directory(temp_dirpath, delete_original_files=True,
                            anonymise_filenames=False)
        # # File and dir should be anonymised since original file should
        # # have been deleted.
        assert is_anonymised_file(temp_anon_filepath)
        assert not exists(temp_filepath)
        assert is_anonymised_directory(temp_dirpath)

    finally:
        remove_file(temp_anon_filepath)
        remove_dir(temp_dirpath)


@pytest.mark.skipif('SUBPACKAGE' in os.environ, reason="Need to extract CLI out of subpackages")
def test_anonymise_cli():

    # Basic file anonymisation
    assert not is_anonymised_file(test_filepath)
    assert not exists(test_anon_filepath)

    anon_file_command = ('pymedphys dicom anonymise'.split() + [test_filepath])
    try:
        subprocess.check_call(anon_file_command)
        assert is_anonymised_file(test_anon_filepath)
        assert exists(test_filepath)
    finally:
        remove_file(test_anon_filepath)

    # File anonymisation - preserve filenames
    assert not is_anonymised_file(test_filepath)

    expected_anon_filepath = label_dicom_filepath_as_anonymised(test_filepath)
    assert not exists(expected_anon_filepath)

    anon_file_pres_command = ('pymedphys dicom anonymise -f'.split()
                              + [test_filepath])
    try:
        subprocess.check_call(anon_file_pres_command)
        assert is_anonymised_file(expected_anon_filepath)
        assert exists(test_filepath)
    finally:
        remove_file(expected_anon_filepath)

    # File anonymisation - clear values
    assert not is_anonymised_file(test_filepath)
    assert not exists(test_anon_filepath)

    anon_file_clear_command = ('pymedphys dicom anonymise -c'.split()
                               + [test_filepath])
    try:
        subprocess.check_call(anon_file_clear_command)
        assert is_anonymised_file(test_anon_filepath)
        assert pydicom.dcmread(test_anon_filepath).PatientName == ''
        assert exists(test_filepath)
    finally:
        remove_file(test_anon_filepath)

    # File anonymisation - leave keywords unchanged
    assert not is_anonymised_file(test_filepath)
    assert not exists(test_anon_filepath)

    anon_file_keep_command = ('pymedphys dicom anonymise'.split()
                              + [test_filepath]
                              + '-k PatientName'.split())
    try:
        subprocess.check_call(anon_file_keep_command)
        assert not is_anonymised_file(test_anon_filepath)
        ds = pydicom.dcmread(test_anon_filepath)
        ds.PatientName = "Anonymous"
        assert is_anonymised_dataset(ds)
        assert exists(test_filepath)
    finally:
        remove_file(test_anon_filepath)

    # File anonymisation - private tag handling
    assert not is_anonymised_file(test_filepath)
    assert not exists(test_anon_filepath)

    anon_file_private_command = ('pymedphys dicom anonymise -p'.split()
                                 + [test_filepath])
    try:
        subprocess.check_call(anon_file_private_command)
        assert not is_anonymised_file(test_anon_filepath)
        assert is_anonymised_file(test_anon_filepath,
                                  ignore_private_tags=True)
        assert exists(test_filepath)
    finally:
        remove_file(test_anon_filepath)

    # TODO: File anonymisation - unknown tag handling
    # # Calling a subprocess reloads BaselineDicomDictionary...

    # Basic dir anonymisation
    assert not is_anonymised_directory(DATA_DIR)
    assert not exists(test_anon_filepath)

    anon_dir_command = ('pymedphys dicom anonymise'.split() + [DATA_DIR])
    try:
        subprocess.check_call(anon_dir_command)
        assert is_anonymised_file(test_anon_filepath)
        assert exists(test_filepath)
    finally:
        remove_file(test_anon_filepath)


def test_tags_to_anonymise_in_dicom_dict_baseline():
    baseline_keywords = [
        val[4] for val in BaselineDicomDictionary.values()]
    assert set(IDENTIFYING_KEYWORDS).issubset(baseline_keywords)