## Dependency Updates

```diff
< revision = 3
> revision = 5
<     "python_full_version >= '3.12'",
<     "python_full_version == '3.11.*'",
>     "python_full_version >= '3.12' and sys_platform == 'win32'",
>     "python_full_version >= '3.12' and sys_platform == 'emscripten'",
>     "python_full_version >= '3.12' and sys_platform != 'emscripten' and sys_platform != 'win32'",
>     "python_full_version >= '3.11.5' and python_full_version < '3.12'",
>     "python_full_version >= '3.11' and python_full_version < '3.11.5'",
< version = "0.7.0"
> version = "0.8.0"
< sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/5f/56/a8120250d128bed162cd73c76d45f6ef9991f3e068f62a8ee060afa3104a/annotated_types-0.8.0.tar.gz", hash = "sha256:13b2beaad985e05e2d6407ee4c4f35590b11f8d693a258a561055cac8f64cab7", size = 15893, upload-time = "2026-07-23T20:16:13.995Z" }
<     { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
>     { url = "https://files.pythonhosted.org/packages/99/91/8acff4f5e50511b911bbccb72b8628a49c68ce14148cd9f6431094859a90/annotated_types-0.8.0-py3-none-any.whl", hash = "sha256:f072f4d804ea359e4eaf198b1af7a8b0943881a87f31bb764f8bf219bb9419e0", size = 13427, upload-time = "2026-07-23T20:16:12.938Z" },
< version = "0.67.0"
> version = "2.3.0"
<     { name = "distro" },
<     { name = "httpx" },
>     { name = "docstring-parser" },
>     { name = "httpx2", version = "2.14.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
>     { name = "httpx2", version = "2.16.0", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
>     { name = "opentelemetry-api" },
< sdist = { url = "https://files.pythonhosted.org/packages/09/08/ee91464cd821e6fca52d9a23be44815c95edd3c1cf1e844b2c5e85f0d57f/anthropic-0.67.0.tar.gz", hash = "sha256:d1531b210ea300c73423141d29bcee20fcd24ef9f426f6437c0a5d93fc98fb8e", size = 441639, upload-time = "2025-09-10T14:47:18.137Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/3e/ba/4c91947e0d0062d66d371db371597287153f7685fbed512d3294d0cde3c7/anthropic-2.3.0.tar.gz", hash = "sha256:edfdea1e3fa7b3ce25df1511953408b2f03bfa61eb6f6268f766101a9e18ad53", size = 1869656, upload-time = "2026-10-23T23:18:47.649Z" }
<     { url = "https://files.pythonhosted.org/packages/5c/9d/9adbda372710918cc8271d089a2ceae4d977a125f90bc3c4b456bca4f281/anthropic-0.67.0-py3-none-any.whl", hash = "sha256:f80a81ec1132c514215f33d25edeeab1c4691ad5361b391ebb70d528b0605b55", size = 317126, upload-time = "2025-09-10T14:47:16.351Z" },
>     { url = "https://files.pythonhosted.org/packages/3f/29/eb3558ab6bf252a07ac41c76ac5b0ea24a0aa0c23f87a40aaf31a5f8dba4/anthropic-2.3.0-py3-none-any.whl", hash = "sha256:aa6a3984f9276f307933d42dc6f58b6efc821a5ecafbc8d1bb5993a066767622", size = 2216980, upload-time = "2026-10-23T23:18:45.779Z" },
< version = "4.10.0"
> version = "4.15.1"
<     { name = "sniffio" },
< sdist = { url = "https://files.pythonhosted.org/packages/f1/b4/636b3b65173d3ce9a38ef5f0522789614e590dab6a8d505340a4efe4c567/anyio-4.10.0.tar.gz", hash = "sha256:3f3fae35c96039744587aa5b8371e7e8e603c0702999535961dd336026973ba6", size = 213252, upload-time = "2025-08-04T08:54:26.451Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/a9/d2/f4d173e22df740bc37b1db102b386ba719b66e95b0f0d751f556b387e6d2/anyio-4.15.1.tar.gz", hash = "sha256:9f28306018cbd6d329e64a36d58256edff76dd996fe423bc957326e578b82a94", size = 276966, upload-time = "2026-09-05T10:42:39.44Z" }
<     { url = "https://files.pythonhosted.org/packages/6f/12/e5e0282d673bb9746bacfb6e2dba8719989d3660cdb2ea79aee9a9651afb/anyio-4.10.0-py3-none-any.whl", hash = "sha256:60e474ac86736bbfd6f210f7a61218939c318f43f9972497381f1c5e930ed3d1", size = 107213, upload-time = "2025-08-04T08:54:24.882Z" },
>     { url = "https://files.pythonhosted.org/packages/12/b8/4bd346e22b28902df4d651910f5242c28d84e4a5c2435ca5c3f797ed7e2e/anyio-4.15.1-py3-none-any.whl", hash = "sha256:6152fdbbf9a77fdec97731721bebf7c4c44f7c29b424b0065826173efc7ed101", size = 132079, upload-time = "2026-09-05T10:42:37.923Z" },
< version = "0.1.4"
> version = "1.0.0"
< sdist = { url = "https://files.pythonhosted.org/packages/35/5d/752690df9ef5b76e169e68d6a129fa6d08a7100ca7f754c89495db3c6019/appnope-0.1.4.tar.gz", hash = "sha256:1de3860566df9caf38f01f86f65e0e13e379af54f9e4bee1e66b48f2efffd1ee", size = 4170, upload-time = "2024-02-06T09:43:11.258Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/11/f7/a82489c2b6ebe32d3e2831895ae19c77861f0eadf3bb16034484d965dbb2/appnope-1.0.0.tar.gz", hash = "sha256:685db59cb6043c3c2e528adc0b3bce3a5f8d09bcf7492c6ea650d1b7421f3c49", size = 5454, upload-time = "2026-08-20T21:36:13.748Z" }
<     { url = "https://files.pythonhosted.org/packages/81/29/5ecc3a15d5a33e31b26c11426c45c501e439cb865d0bff96315d86443b78/appnope-0.1.4-py2.py3-none-any.whl", hash = "sha256:502575ee11cd7a28c0205f379b525beefebab9d161b7c964670864014ed7213c", size = 4321, upload-time = "2024-02-06T09:43:09.663Z" },
>     { url = "https://files.pythonhosted.org/packages/46/c7/6b687cb0f83d2a51017d47953f2ee430ffad6fec2a8ebc964e0718a33eb1/appnope-1.0.0-py3-none-any.whl", hash = "sha256:6fe0c04218aab65c54c4ff81638cdbf848d89f5653b74d68638a137f200dd16e", size = 4158, upload-time = "2026-08-20T21:36:12.444Z" },
< version = "3.3.11"
> version = "4.3.4"
< sdist = { url = "https://files.pythonhosted.org/packages/18/74/dfb75f9ccd592bbedb175d4a32fc643cf569d7c218508bfbd6ea7ef9c091/astroid-3.3.11.tar.gz", hash = "sha256:1e5a5011af2920c7c67a53f65d536d65bfa7116feeaf2354d8b94f29573bb0ce", size = 400439, upload-time = "2025-07-13T18:04:23.177Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/2d/87/5732fa68bf100a095cfcbd108f919220d995db99e1a7502b8119a869fd62/astroid-4.3.4.tar.gz", hash = "sha256:d515a105722b72098bbe82d430d65e635f742b6cbac3bdfaf8b7c188b87c5e39", size = 444627, upload-time = "2026-10-08T09:36:44.122Z" }
<     { url = "https://files.pythonhosted.org/packages/af/0f/3b8fdc946b4d9cc8cc1e8af42c4e409468c84441b933d037e101b3d72d86/astroid-3.3.11-py3-none-any.whl", hash = "sha256:54c760ae8322ece1abd213057c4b5bba7c49818853fc901ef09719a60dbf9dec", size = 275612, upload-time = "2025-07-13T18:04:21.07Z" },
>     { url = "https://files.pythonhosted.org/packages/16/d4/f23c0ac6e6de33ba5686cb21c672c95e0c2d3d4c9351f16d3b5fed818652/astroid-4.3.4-py3-none-any.whl", hash = "sha256:2bcd0d02648a443a4b818c952c3550091989daefac3c12d3b83b2289482e0818", size = 288310, upload-time = "2026-10-08T09:36:42.284Z" },
< version = "3.0.0"
> version = "3.0.2"
< sdist = { url = "https://files.pythonhosted.org/packages/4a/e7/82da0a03e7ba5141f05cce0d302e6eed121ae055e0456ca228bf693984bc/asttokens-3.0.0.tar.gz", hash = "sha256:0dcd8baa8d62b0c1d118b399b2ddba3c4aff271d0d7a9e0d4c1681c79035bbc7", size = 61978, upload-time = "2024-11-30T04:30:14.439Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/25/1e/faf0f247f6f881b98fc4d6d07e14085cb89d13665084e6d6ac1dc2c03d0b/asttokens-3.0.2.tar.gz", hash = "sha256:3ecdbd8f2cc195f53ccada3a613538bb5f9ef6f6869129f13e03c30a677b8fe2", size = 63136, upload-time = "2026-07-12T03:31:49.084Z" }
```
