import canvass
from setuptools import setup

setup(
    name='canvass',
    version=canvass.__version__,
    description='Ask a tree-based series of questions, using inquirer',
    license='MIT',
    author='Dominic Fitzgerald',
    author_email='dominicfitzgerald11@gmail.com',
    url='https://github.com/djf604/canvass',
    py_modules=['canvass'],
    install_requires=['inquirer'],
    dependency_links=['git+https://github.com/djf604/python-inquirer'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ]
)
