import setuptools

setuptools.setup(
    name='travis-exec',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/travis-exec']
)
