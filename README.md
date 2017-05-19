# Website & Email checker
[![Build Status](https://travis-ci.org/capJavert/is-it-safe.svg?branch=master)](https://travis-ci.org/capJavert/is-it-safe)
## Utility for website or email danger checking
### Install
You will need pip tool for python to install this utility into your shell environment.

Pip is included in python 3.x+

Utility is compatible with python 2.7+

$ git clone https://github.com/capJavert/is-it-safe.git is-it-safe

$ cd is-it-safe

$ pip install --editable . (you have to be root user on linux or use sudo)

After install you can use script as:

$ iisafe --website=google.com or shorter $ iisafe -w google.com
### Usage
Usage: iisafe [OPTIONS]

Options:

  -w, --website TEXT  Website that you wish to check. Default is None
  
  -e, --email TEXT  Email address that you wish to check. Default is None
  
  --help       Show this message and exit.
### To do
- Add more websites checking sources
- Add more email checking sources

### Notice
- Please to not abuse API keys or they will be blocked, thanks
