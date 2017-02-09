from setuptools import setup

setup(
    name='tractor',
    version='0.1.0',
    description='Module used to download files over SSH',
    url='https://github.com/orionnetworksolutions/tractor',
    author='Brian Lee',
    author_email='briandl92391@gmail.com',
    license='MIT',
    packages=['tractor'],
    install_requires=['paramiko'],
    zip_safe=True
)
