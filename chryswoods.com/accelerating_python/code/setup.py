try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from Cython.Build import cythonize

from distutils.extension import Extension

cyslow = Extension(
    "cyslow",
    sources=["cyslow.pyx"],
    extra_compile_args=['-O3'],
    extra_link_args=['-O3']
)

setup(
    ext_modules = cythonize(cyslow)
)
