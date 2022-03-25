from setuptools import setup, find_packages
from setuptools.command.install import install


VERSION = '0.0.1'
DESCRIPTION = 'Panduza Python Platform'
LONG_DESCRIPTION = 'The Panduza '


class CustomInstallCommand(install):
    def run(self):
        install.run(self)


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="panduza_platform",
    version=VERSION,
    author="Panduza Team",
    author_email="panduza.team@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    cmdclass={'install': CustomInstallCommand},

    install_requires=['loguru', 'paho-mqtt', 'pyserial'],

    # keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
