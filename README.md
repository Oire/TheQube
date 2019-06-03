# Welcome to TheQube
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Oire/TheQube/blob/master/LICENSE)

TheQube is an accessible social networking client developed mainly for the blind and visually impaired users.
© Original idea and code by [Christopher Toth](http://q-continuum.net/)  
© Main fork implementation and various new features and bugfixes by [Quartizer projects](http://quartzprojects.co.uk/)  
© Currently developed and maintained by [Andre Polykanine and TheQube Contributors](http://theqube.oire.org/).  

## Running TheQube from source

This document describes how to run TheQube from source and how to build a binary version.

### Dependencies

To be able to build TheQube you need to install a few programs first. Most of them are included in the dependencies directory in the root of this repo. The only exception is Python. Download and install [Python 2.7 32-bit](https://www.python.org/downloads/). Be sure to add Python directory to your path during installation.

#### Dependencies included in the dependencies directory

* [Durus version 3.9](https://www.mems-exchange.org/software/)
* [Python Imaging Library version 1.1.7](http://www.pythonware.com/products/pil/)
* [Py2exe version 0.6.9](http://www.py2exe.org/) (required only if you want to build an executable version of TheQube)
* [PyCURL version 7.19.0](http://pycurl.io/)
* [Pywin32 version 214](https://github.com/mhammond/pywin32)
* [WXPython version 2.9.1.1](https://wxpython.org/)

#### Dependencies installed with pip

The rest of the needed packages could be installed with Python package manager called pip. Before using it is a good idea to update pip to the latest version with the following two commands:

```shell
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
````

To make installation easier, all required packages are listed in the text file called *requirements.txt*. To install them move to the root directory of this repo, make sure that Python and Git are in your path and execute the following command:

```shell
pip install -r requirements.txt
```

### Running TheQube

When all of the above mentioned packages are installed, you can finally start TheQube. Move to the *src* directory of this repo and execute:

```shell
python main.pyw
```

Alternatively you can start TheQube by simply pressing **Enter** on the *main.pyw* file as long as Pythonw is associated with .pyw files.

### Building a Binary Version

A binary version doesn’t need Python nor other dependencies to run. To build it you need to install Py2exe included in the *dependencies* directory and two more packages with Pip by executing the following commands:

```shell
pip install packaging
pip install appdirs
```

After that, from the *src* directory execute:

```shell
python setup.py py2exe
```

You will find the binaries in the *dist* directory.
