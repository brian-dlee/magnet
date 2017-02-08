from setuptools import setup

setup(
    name='sftpdownloader',
    version='0.1.0',
    description='Module used to download files over SSH',
    url='https://github.com/orionnetworksolutions/sftpdownloader',
    author='Brian Lee',
    author_email='briandl92391@gmail.com',
    license='MIT',
    packages=['sftpdownloader'],
    install_requires=['paramiko'],
    zip_safe=True
)