import os

default_settings_yml = """\
# This file was generated by Conan. Remove this comment if you edit this file or Conan
# will destroy your changes.
os:
    Windows:
        subsystem: [null, cygwin, msys, msys2, wsl]
    WindowsStore:
        version: ["8.1", "10.0"]
    WindowsCE:
        platform: [ANY]
        version: ["5.0", "6.0", "7.0", "8.0"]
    Linux:
    iOS:
        version: &ios_version
                   ["7.0", "7.1", "8.0", "8.1", "8.2", "8.3", "9.0", "9.1", "9.2", "9.3", "10.0", "10.1", "10.2", "10.3",
                    "11.0", "11.1", "11.2", "11.3", "11.4", "12.0", "12.1", "12.2", "12.3", "12.4",
                    "13.0", "13.1", "13.2", "13.3", "13.4", "13.5", "13.6", "13.7",
                    "14.0", "14.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7", "14.8",
                    "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6", "16.0", "16.1",
                    "16.2", "16.3", "16.4", "16.5", "16.6", "17.0", "17.1"]
        sdk: ["iphoneos", "iphonesimulator"]
        sdk_version: [null, "11.3", "11.4", "12.0", "12.1", "12.2", "12.4",
                        "13.0", "13.1", "13.2", "13.4", "13.5", "13.6", "13.7",
                        "14.0", "14.1", "14.2", "14.3", "14.4", "14.5", "15.0", "15.2", "15.4",
                        "15.5", "16.0", "16.1", "16.2", "16.4", "17.0", "17.1"]
    watchOS:
        version: ["4.0", "4.1", "4.2", "4.3", "5.0", "5.1", "5.2", "5.3", "6.0", "6.1", "6.2",
                    "7.0", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "8.0", "8.1", "8.3", "8.4",
                    "8.5", "8.6", "8.7", "9.0", "9.1", "9.2", "9.3", "9.4", "9.5", "9.6",
                    "10.0", "10.1"]
        sdk: ["watchos", "watchsimulator"]
        sdk_version: [null, "4.3", "5.0", "5.1", "5.2", "5.3", "6.0", "6.1", "6.2",
                        "7.0", "7.1", "7.2", "7.4", "8.0", "8.0.1", "8.3", "8.5", "9.0", "9.1",
                        "9.4", "10.0", "10.1"]
    tvOS:
        version: ["11.0", "11.1", "11.2", "11.3", "11.4", "12.0", "12.1", "12.2", "12.3", "12.4",
                    "13.0", "13.2", "13.3", "13.4", "14.0", "14.2", "14.3", "14.4", "14.5",
                    "14.6", "14.7", "15.0", "15.1", "15.2", "15.3", "15.4", "15.5", "15.6",
                    "16.0", "16.1", "16.2", "16.3", "16.4", "16.5", "16.6", "17.0", "17.1"]
        sdk: ["appletvos", "appletvsimulator"]
        sdk_version: [null, "11.3", "11.4", "12.0", "12.1", "12.2", "12.4",
                        "13.0", "13.1", "13.2", "13.4", "14.0", "14.2", "14.3", "14.5", "15.0",
                        "15.2", "15.4", "16.0", "16.1", "16.4", "17.0", "17.1"]
    visionOS:
        version: ["1.0"]
        sdk: ["xros", "xrsimulator"]
        sdk_version: [null, "1.0"]
    Macos:
        version: [null, "10.6", "10.7", "10.8", "10.9", "10.10", "10.11", "10.12", "10.13", "10.14", "10.15",
                    "11.0", "11.1", "11.2", "11.3", "11.4", "11.5", "11.6", "11.7",
                    "12.0", "12.1", "12.2", "12.3", "12.4", "12.5", "12.6", "12.7",
                    "13.0", "13.1", "13.2", "13.3", "13.4", "13.5", "13.6",
                    "14.0", "14.1"]
        sdk_version: [null, "10.13", "10.14", "10.15", "11.0", "11.1", "11.3", "12.0", "12.1",
                        "12.3", "13.0", "13.1", "13.3", "14.0"]
        subsystem:
            null:
            catalyst:
                ios_version: *ios_version
    Android:
        api_level: [ANY]
    FreeBSD:
    SunOS:
    AIX:
    Arduino:
        board: [ANY]
    Emscripten:
    Neutrino:
        version: ["6.4", "6.5", "6.6", "7.0", "7.1"]
    baremetal:
    VxWorks:
        version: ["7"]
arch: [x86, x86_64, ppc32be, ppc32, ppc64le, ppc64,
       armv4, armv4i, armv5el, armv5hf, armv6, armv7, armv7hf, armv7s, armv7k, armv8, armv8_32, armv8.3, arm64ec,
       sparc, sparcv9,
       mips, mips64, avr, s390, s390x, asm.js, wasm, sh4le,
       e2k-v2, e2k-v3, e2k-v4, e2k-v5, e2k-v6, e2k-v7,
       xtensalx6, xtensalx106, xtensalx7]
compiler:
    sun-cc:
        version: ["5.10", "5.11", "5.12", "5.13", "5.14", "5.15"]
        threads: [null, posix]
        libcxx: [libCstd, libstdcxx, libstlport, libstdc++]
    gcc:
        version: ["4.1", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9",
                    "5", "5.1", "5.2", "5.3", "5.4", "5.5",
                    "6", "6.1", "6.2", "6.3", "6.4", "6.5",
                    "7", "7.1", "7.2", "7.3", "7.4", "7.5",
                    "8", "8.1", "8.2", "8.3", "8.4", "8.5",
                    "9", "9.1", "9.2", "9.3", "9.4", "9.5",
                    "10", "10.1", "10.2", "10.3", "10.4", "10.5",
                    "11", "11.1", "11.2", "11.3", "11.4",
                    "12", "12.1", "12.2", "12.3",
                    "13", "13.1", "13.2"]
        libcxx: [libstdc++, libstdc++11]
        threads: [null, posix, win32]  # Windows MinGW
        exception: [null, dwarf2, sjlj, seh]  # Windows MinGW
        cppstd: [null, 98, gnu98, 11, gnu11, 14, gnu14, 17, gnu17, 20, gnu20, 23, gnu23]
    msvc:
        version: [170, 180, 190, 191, 192, 193]
        update: [null, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        runtime: [static, dynamic]
        runtime_type: [Debug, Release]
        cppstd: [null, 14, 17, 20, 23]
        toolset: [null, v110_xp, v120_xp, v140_xp, v141_xp]
    clang:
        version: ["3.3", "3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "4.0",
                  "5.0", "6.0", "7.0", "7.1",
                  "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
        libcxx: [null, libstdc++, libstdc++11, libc++, c++_shared, c++_static]
        cppstd: [null, 98, gnu98, 11, gnu11, 14, gnu14, 17, gnu17, 20, gnu20, 23, gnu23]
        runtime: [null, static, dynamic]
        runtime_type: [null, Debug, Release]
        runtime_version: [null, v140, v141, v142, v143]
    apple-clang:
        version: ["5.0", "5.1", "6.0", "6.1", "7.0", "7.3", "8.0", "8.1", "9.0", "9.1",
                  "10.0", "11.0", "12.0", "13", "13.0", "13.1", "14", "14.0", "15", "15.0"]
        libcxx: [libstdc++, libc++]
        cppstd: [null, 98, gnu98, 11, gnu11, 14, gnu14, 17, gnu17, 20, gnu20, 23, gnu23]
    intel-cc:
        version: ["2021.1", "2021.2", "2021.3"]
        update: [null, ANY]
        mode: ["icx", "classic", "dpcpp"]
        libcxx: [null, libstdc++, libstdc++11, libc++]
        cppstd: [null, 98, gnu98, "03", gnu03, 11, gnu11, 14, gnu14, 17, gnu17, 20, gnu20, 23, gnu23]
        runtime: [null, static, dynamic]
        runtime_type: [null, Debug, Release]
    qcc:
        version: ["4.4", "5.4", "8.3"]
        libcxx: [cxx, gpp, cpp, cpp-ne, accp, acpp-ne, ecpp, ecpp-ne]
        cppstd: [null, 98, gnu98, 11, gnu11, 14, gnu14, 17, gnu17]
    mcst-lcc:
        version: ["1.19", "1.20", "1.21", "1.22", "1.23", "1.24", "1.25"]
        libcxx: [libstdc++, libstdc++11]
        cppstd: [null, 98, gnu98, 11, gnu11, 14, gnu14, 17, gnu17, 20, gnu20, 23, gnu23]

build_type: [null, Debug, Release, RelWithDebInfo, MinSizeRel]
"""


def get_default_settings_yml():
    return default_settings_yml


def migrate_settings_file(cache_folder):
    from conans.client.migrations import update_file

    settings_path = os.path.join(cache_folder, "settings.yml")
    update_file(settings_path, default_settings_yml)
