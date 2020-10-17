from setuptools import setup, find_packages

setup(
    name='dagpipy',
    author='niztg',
    url='https://github.com/niztg/dagpipy',
    version='1.0.1',
    license='MIT',
    project_urls={'Discord Server': 'https://discord.com/invite/2fxKxJH'},
    description='A Python API Wrapper for https://dagpi.xyz/, the fast and free image API.',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests'],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
)