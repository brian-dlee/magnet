from setuptools import setup

setup(
    name='magnet',
    version='0.1.1',
    description='Module used to download files over SSH',
    url='https://github.com/brian-dlee/magnet',
    author='Brian Lee',
    author_email='briandl92391@gmail.com',
    license='MIT',
    packages=['tractor'],
    install_requires=['paramiko', 'bunch'],
    zip_safe=True
)
