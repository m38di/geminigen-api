from setuptools import setup, find_packages

setup(
    name="geminigen_api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "curl_cffi"
    ],
    python_requires=">=3.8",
)
