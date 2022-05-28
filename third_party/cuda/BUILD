package(default_visibility = ["//visibility:public"])

config_setting(
    name = "windows",
    constraint_values = [
        "@platforms//os:windows",
    ],
)

cc_library(
    name = "cudart",
    srcs = select({
        ":windows": [
            "lib/x64/cudart.lib",
        ],
        "//conditions:default": [
            "cuda/lib64/libcudart.so",
        ],
    }),
    hdrs = glob([
        "cuda/include/**/*.h",
        "cuda/include/**/*.hpp",
        "cuda/include/**/*.inl",
    ]),
    includes = ["include/"],
)

cc_library(
    name = "nvToolsExt",
    srcs = select({
        ":windows": [
            "bin/nvToolsExt64_1.dll",
        ],
        "//conditions:default": [
            "cuda/lib64/libnvToolsExt.so.1",
        ],
    }),
)

cc_library(
    name = "cuda",
    srcs = select({
        ":windows": [
            "bin/*.dll",
        ],
        "//conditions:default": glob([
            "cuda/lib64/**/lib*.so",
        ]),
    }),
    hdrs = glob([
        "cuda/include/**/*.h",
        "cuda/include/**/*.hpp",
        "cuda/include/**/*.inl",
    ]),
    includes = ["include/"],
    linkopts = ["-Wl,-rpath,lib/"],
)

cc_library(
    name = "cublas",
    srcs = select({
        ":windows": glob([
            "lib/x64/cublas.lib",
        ]),
        "//conditions:default": glob([
            "cuda/lib64/**/*libcublas.so",
        ]),
    }),
    hdrs = glob([
        "cuda/include/**/*cublas*.h",
        "cuda/include/**/*.hpp",
        "cuda/include/**/*.inl",
    ]),
    includes = ["include/"],
    linkopts = ["-Wl,-rpath,lib/"],
)
