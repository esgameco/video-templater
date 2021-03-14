from setuptools import setup

# TODO: Finish setup.py

NAME = 'video-templater'
DESCRIPTION = 'A video templating package'
URL = 'https://github.com/esgameco/video-templater/'
EMAIL = 'esgameco@gmail.com'
AUTHOR = 'Chance Vodnoy'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

with open("README.rst", "r", "utf-8") as file:
    readme = file.read()

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Documentation :: Sphinx',
        'Operating System :: OS Independent',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)