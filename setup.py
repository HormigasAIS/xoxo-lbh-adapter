import os
from setuptools import setup, find_packages, Extension
import pybind11

# Configuración del módulo nativo
LBH_ROOT = os.environ.get("LBH_BIN_ROOT", "lbh_bin_module")
lbh_module = Extension(
    "lbh_module",
    sources=[os.path.join(LBH_ROOT, "src", "lbh_module.cpp")],
    include_dirs=[pybind11.get_include(), os.path.join(LBH_ROOT, "include")],
    language="c++",
    extra_compile_args=["-O2", "-std=c++17"]
)

# Setup combinando Python y módulo C++
setup(
    name="xoxo-lbh-adapter",
    version="1.0.0",
    packages=find_packages(),
    ext_modules=[lbh_module],
    zip_safe=False,
    install_requires=[
        # "uvloop",  # solo Linux
    ],
    entry_points={
        "console_scripts": [
            # Esto crea el comando ejecutable 'xoxo-init'
            "xoxo-init = xoxo_init:main",
        ]
    },
    python_requires=">=3.12",
)
