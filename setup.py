import setuptools

setuptools.setup(
    name='test_package',
    version='1.0.2',
    author='John Naeder',
    description='Testing installation of Package',
    url='https://github.com/jnaederSAE/test_package',
    install_requires=["pymssql==2.2.7",
                      "python-dotenv==1.0.0"],
    packages=setuptools.find_packages()
)
