# Change.org Python API

This is a Python interface for the http://change.org REST API.

This package uses [Requests](http://docs.python-requests.org/en/latest/) as its HTTP request engine, and returns data in regular Python data structures (lists and dicts).

## Local Installation

- Clone this project on to your local computer using the following command
```bash
$ git clone https://github.com/rukmal/Change.org-Python-API
```
- Export the location of your project as an environment variable to make the installation process easier
```bash
$ export PROJECT_LOCATION=[Your project location goes here]
```
- Copy the ```change_org``` directory into your project directory
```bash
cp -r change_org $PROJECT_LOCATION
```
- Append the dependencies to existing ```requirements.txt``` file, or create a new one and append it if it does not exist
```bash
$ if [ -e $PROJECT_LOCATION/requirements.txt ]; then cat requirements.txt >> $PROJECT_LOCATION/requirements.txt; else cp requirements.txt $PROJECT_LOCATION; fi;
```
- Install requirements
```bash
$ cd $PROJECT_LOCATION; pip install -r requirements.txt;
```

## Contact

This is an open source project released under the [MIT License](LICENSE). Contact me if you want to suggest an improvement, or fork and send a pull request!

Follow me on Twitter ([@rukmal](http://twitter.com/rukmal_w)) and [GitHub](http://github.com/rukmal).

http://rukmal.me
