from setuptools import setup, find_packages

try:
    long_desc = open('README.md').read()
except:
    long_desc = ''

setup(
    name="jupyterliveshare",
    url="https://github.com/mishra14",
    author="Ankit Mishra",
    author_email="mishra14@gmail.com",
    version="0.0.1dev0",
    packages=find_packages(),
    install_requires=[
        "jupyter==1",
        "argparse==1.1",
        "msgpack==0.5.6"
    ],
    include_package_data=True,
    description="A button on Jupyter's toolbar for LiveShare",
    long_description=long_desc,
)
