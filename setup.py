import os
from setuptools import setup, Extension
import pybind11

LBH_ROOT = os.environ.get("LBH_BIN_ROOT", "lbh_bin_module")

lbh_module = Extension(
    "lbh_module",
    sources=[os.path.join(LBH_ROOT, "src", "lbh_module.cpp")],
    include_dirs=[pybind11.get_include(), os.path.join(LBH_ROOT, "include")],
    language="c++",
    extra_compile_args=["-O2", "-std=c++17"]
)

setup(
    name="xoxo-lbh-adapter",
    version="0.1.0",
    description="Adapter XOXO <-> LBH-M2M con módulo nativo C++",
    ext_modules=[lbh_module],
    zip_safe=False
)
