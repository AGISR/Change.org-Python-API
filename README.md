# Change.org Python API

This is a Python interface for the http://change.org REST API.

This package uses [Requests](http://docs.python-requests.org/en/latest/) as its HTTP request engine, and returns data in regular Python data structures (lists and dicts).

## Installation

- Clone this project on to your local computer using the following command
```bash
$ git clone https://github.com/rukmal/Change.org-Python-API
```
- Install requirements using [pip](https://pypi.python.org/pypi) (Note: the ```sudo``` may be required)
```bash
$ [sudo] pip install -r requirements.txt
```
- Install using setup.py (Note: the ```sudo``` may be required)
```bash
$ [sudo] python setup.py install
```

### Running tests

To run all tests, use [py.test](http://pytest.org/latest/) (installed by default with project dependencies):
```bash
$ py.test tests/*
```

Or alternatively, use the Makefile function as follows:
```bash
$ make test
```

## Contact

This is an open source project released under the [MIT License](LICENSE). Contact me if you want to suggest an improvement, or fork and send a pull request!

Follow me on Twitter ([@rukmal](http://twitter.com/rukmal_w)) and [GitHub](http://github.com/rukmal).

http://rukmal.me
