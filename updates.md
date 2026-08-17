## Dependency Updates

```diff
<     "python_full_version >= '3.12'",
>     "python_full_version >= '3.12' and sys_platform == 'win32'",
>     "python_full_version >= '3.12' and sys_platform == 'emscripten'",
>     "python_full_version >= '3.12' and sys_platform != 'emscripten' and sys_platform != 'win32'",
< version = "0.7.0"
> version = "0.8.0"
< sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/5f/56/a8120250d128bed162cd73c76d45f6ef9991f3e068f62a8ee060afa3104a/annotated_types-0.8.0.tar.gz", hash = "sha256:13b2beaad985e05e2d6407ee4c4f35590b11f8d693a258a561055cac8f64cab7", size = 15893, upload-time = "2026-07-23T20:16:13.995Z" }
<     { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
>     { url = "https://files.pythonhosted.org/packages/99/91/8acff4f5e50511b911bbccb72b8628a49c68ce14148cd9f6431094859a90/annotated_types-0.8.0-py3-none-any.whl", hash = "sha256:f072f4d804ea359e4eaf198b1af7a8b0943881a87f31bb764f8bf219bb9419e0", size = 13427, upload-time = "2026-07-23T20:16:12.938Z" },
< version = "0.67.0"
> version = "0.122.0"
>     { name = "docstring-parser" },
< sdist = { url = "https://files.pythonhosted.org/packages/09/08/ee91464cd821e6fca52d9a23be44815c95edd3c1cf1e844b2c5e85f0d57f/anthropic-0.67.0.tar.gz", hash = "sha256:d1531b210ea300c73423141d29bcee20fcd24ef9f426f6437c0a5d93fc98fb8e", size = 441639, upload-time = "2025-09-10T14:47:18.137Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/fa/23/9987d70b74e3481d5bc5d2021d3e10fd5f60c1f7b54088ea86506d9b7f2b/anthropic-0.122.0.tar.gz", hash = "sha256:ffec56ae96657c8d19fa575ec96f140f380c353a07ab7d61b92eb18ee6536601", size = 1021535, upload-time = "2026-08-13T18:36:00.307Z" }
<     { url = "https://files.pythonhosted.org/packages/5c/9d/9adbda372710918cc8271d089a2ceae4d977a125f90bc3c4b456bca4f281/anthropic-0.67.0-py3-none-any.whl", hash = "sha256:f80a81ec1132c514215f33d25edeeab1c4691ad5361b391ebb70d528b0605b55", size = 317126, upload-time = "2025-09-10T14:47:16.351Z" },
>     { url = "https://files.pythonhosted.org/packages/26/5b/f5c87e71097a9f89f1b414d1ef7ae8439051fae57d5e4ee90946082982b8/anthropic-0.122.0-py3-none-any.whl", hash = "sha256:45ec906452ffae6b5f7f0c53d01f50bfb7e4ce878d7ae8e4309d13171e557e67", size = 1041853, upload-time = "2026-08-13T18:36:01.831Z" },
< version = "4.10.0"
> version = "4.14.2"
<     { name = "sniffio" },
< sdist = { url = "https://files.pythonhosted.org/packages/f1/b4/636b3b65173d3ce9a38ef5f0522789614e590dab6a8d505340a4efe4c567/anyio-4.10.0.tar.gz", hash = "sha256:3f3fae35c96039744587aa5b8371e7e8e603c0702999535961dd336026973ba6", size = 213252, upload-time = "2025-08-04T08:54:26.451Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/61/cc/a381afa6efea9f496eff839d4a6a1aed3bfafc7b3ab4b0d1b243a12573dd/anyio-4.14.2.tar.gz", hash = "sha256:cfa139f3ed1a23ee8f88a145ddb5ac7605b8bbfd8592baacd7ce3d8bb4313c7f", size = 260176, upload-time = "2026-07-12T20:29:07.082Z" }
<     { url = "https://files.pythonhosted.org/packages/6f/12/e5e0282d673bb9746bacfb6e2dba8719989d3660cdb2ea79aee9a9651afb/anyio-4.10.0-py3-none-any.whl", hash = "sha256:60e474ac86736bbfd6f210f7a61218939c318f43f9972497381f1c5e930ed3d1", size = 107213, upload-time = "2025-08-04T08:54:24.882Z" },
>     { url = "https://files.pythonhosted.org/packages/da/35/f2287558c17e29fafc8ef3daf819bb9834061cfa43bff8014f7df7f63bdc/anyio-4.14.2-py3-none-any.whl", hash = "sha256:9f505dda5ac9f0c8309b5e8bd445a8c2bf7246f3ce950121e45ea15bc41d1494", size = 125813, upload-time = "2026-07-12T20:29:05.763Z" },
< version = "3.3.11"
> version = "4.0.4"
< sdist = { url = "https://files.pythonhosted.org/packages/18/74/dfb75f9ccd592bbedb175d4a32fc643cf569d7c218508bfbd6ea7ef9c091/astroid-3.3.11.tar.gz", hash = "sha256:1e5a5011af2920c7c67a53f65d536d65bfa7116feeaf2354d8b94f29573bb0ce", size = 400439, upload-time = "2025-07-13T18:04:23.177Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/07/63/0adf26577da5eff6eb7a177876c1cfa213856be9926a000f65c4add9692b/astroid-4.0.4.tar.gz", hash = "sha256:986fed8bcf79fb82c78b18a53352a0b287a73817d6dbcfba3162da36667c49a0", size = 406358, upload-time = "2026-02-07T23:35:07.509Z" }
<     { url = "https://files.pythonhosted.org/packages/af/0f/3b8fdc946b4d9cc8cc1e8af42c4e409468c84441b933d037e101b3d72d86/astroid-3.3.11-py3-none-any.whl", hash = "sha256:54c760ae8322ece1abd213057c4b5bba7c49818853fc901ef09719a60dbf9dec", size = 275612, upload-time = "2025-07-13T18:04:21.07Z" },
>     { url = "https://files.pythonhosted.org/packages/b0/cf/1c5f42b110e57bc5502eb80dbc3b03d256926062519224835ef08134f1f9/astroid-4.0.4-py3-none-any.whl", hash = "sha256:52f39653876c7dec3e3afd4c2696920e05c83832b9737afc21928f2d2eb7a753", size = 276445, upload-time = "2026-02-07T23:35:05.344Z" },
< version = "3.0.0"
> version = "3.0.2"
< sdist = { url = "https://files.pythonhosted.org/packages/4a/e7/82da0a03e7ba5141f05cce0d302e6eed121ae055e0456ca228bf693984bc/asttokens-3.0.0.tar.gz", hash = "sha256:0dcd8baa8d62b0c1d118b399b2ddba3c4aff271d0d7a9e0d4c1681c79035bbc7", size = 61978, upload-time = "2024-11-30T04:30:14.439Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/25/1e/faf0f247f6f881b98fc4d6d07e14085cb89d13665084e6d6ac1dc2c03d0b/asttokens-3.0.2.tar.gz", hash = "sha256:3ecdbd8f2cc195f53ccada3a613538bb5f9ef6f6869129f13e03c30a677b8fe2", size = 63136, upload-time = "2026-07-12T03:31:49.084Z" }
<     { url = "https://files.pythonhosted.org/packages/25/8a/c46dcc25341b5bce5472c718902eb3d38600a903b14fa6aeecef3f21a46f/asttokens-3.0.0-py3-none-any.whl", hash = "sha256:e3078351a059199dd5138cb1c706e6430c05eff2ff136af5eb4790f9d28932e2", size = 26918, upload-time = "2024-11-30T04:30:10.946Z" },
>     { url = "https://files.pythonhosted.org/packages/d4/2b/04b8a15f3a1c77bc79ddf5c73875327f34b4fa75982df2b76e45e402d364/asttokens-3.0.2-py3-none-any.whl", hash = "sha256:9da13157f5b28becde0bd374fc677dcd3c290614264eff096f167c469cd9f933", size = 28702, upload-time = "2026-07-12T03:31:47.542Z" },
< version = "25.3.0"
> version = "26.1.0"
< sdist = { url = "https://files.pythonhosted.org/packages/5a/b0/1367933a8532ee6ff8d63537de4f1177af4bff9f3e829baf7331f595bb24/attrs-25.3.0.tar.gz", hash = "sha256:75d7cefc7fb576747b2c81b4442d4d4a1ce0900973527c011d1030fd3bf4af1b", size = 812032, upload-time = "2025-03-13T11:10:22.779Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/9a/8e/82a0fe20a541c03148528be8cac2408564a6c9a0cc7e9171802bc1d26985/attrs-26.1.0.tar.gz", hash = "sha256:d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32", size = 952055, upload-time = "2026-03-19T14:22:25.026Z" }
<     { url = "https://files.pythonhosted.org/packages/77/06/bb80f5f86020c4551da315d78b3ab75e8228f89f0162f2c3a819e407941a/attrs-25.3.0-py3-none-any.whl", hash = "sha256:427318ce031701fea540783410126f03899a97ffc6f61596ad581ac2e40e3bc3", size = 63815, upload-time = "2025-03-13T11:10:21.14Z" },
>     { url = "https://files.pythonhosted.org/packages/64/b4/17d4b0b2a2dc85a6df63d1157e028ed19f90d4cd97c36717afef2bc2f395/attrs-26.1.0-py3-none-any.whl", hash = "sha256:c647aa4a12dfbad9333ca4e71fe62ddc36f4e63b2d260a37a8b83d2f043ac309", size = 67548, upload-time = "2026-03-19T14:22:23.645Z" },
< version = "2.17.0"
> version = "2.18.0"
< sdist = { url = "https://files.pythonhosted.org/packages/7d/6b/d52e42361e1aa00709585ecc30b3f9684b3ab62530771402248b1b1d6240/babel-2.17.0.tar.gz", hash = "sha256:0c54cffb19f690cdcc52a3b50bcbf71e07a808d1c80d549f2459b9d2cf0afb9d", size = 9951852, upload-time = "2025-02-01T15:17:41.026Z" }
> sdist = { url = "https://files.pythonhosted.org/packages/7d/b2/51899539b6ceeeb420d40ed3cd4b7a40519404f9baf3d4ac99dc413a834b/babel-2.18.0.tar.gz", hash = "sha256:b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d", size = 9959554, upload-time = "2026-02-01T12:30:56.078Z" }
<     { url = "https://files.pythonhosted.org/packages/b7/b8/3fe70c75fe32afc4bb507f75563d39bc5642255d1d94f1f23604725780bf/babel-2.17.0-py3-none-any.whl", hash = "sha256:4d0b53093fdfb4b21c92b5213dba5a1b23885afa8383709427046b21c366e5f2", size = 10182537, upload-time = "2025-02-01T15:17:37.39Z" },
>     { url = "https://files.pythonhosted.org/packages/77/f5/21d2de20e8b8b0408f0681956ca2c69f1320a3848ac50e6e7f39c6159675/babel-2.18.0-py3-none-any.whl", hash = "sha256:e2b422b277c2b9a9630c1d7903c2a00d0830c409c59ac8cae9081c92f1aeba35", size = 10196845, upload-time = "2026-02-01T12:30:53.445Z" },
< version = "4.13.5"
> version = "4.15.0"
```
