import os
import glob
from setuptools import setup, find_packages
from setuptools.command.install import install


VERSION = '0.0.1'
DESCRIPTION = 'Panduza Python Platform'
LONG_DESCRIPTION = 'The Panduza '


class CustomInstallCommand(install):
    
  def run(self):
    install.run(self)
    current_dir_path = os.path.dirname(os.path.realpath(__file__))
    print(">>>>>>>>>>>>>>><", current_dir_path)
    
    # create_service_script_path = os.path.join(current_dir_path, 'super_project', 'install_scripts', 'create_service.sh')
    # subprocess.check_output([create_service_script_path])


# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pza_platform", 
    version=VERSION,
    author="Panduza Team",
    author_email="panduza.team@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    cmdclass={'install': CustomInstallCommand},
    
    # install_requires=['django', 'djangorestframework', 'django-cors-headers'],

    # package_data={
    #     'panduza_server': [
    #         'static/css/*.css',
    #         'static/img/*.png',
    #         'static/js/*.js',
    #         'templates/*.html'
    #     ]
    # },

    # entry_points = {
    #     'console_scripts': ['pza-run-server=panduza_server.scripts.server:run_server'],
    # },

    keywords=['python', 'first package'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


