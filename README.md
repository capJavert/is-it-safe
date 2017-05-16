<h1>Website & Email checker</h1>[![Build Status](https://travis-ci.org/capJavert/is-it-safe.svg?branch=master)](https://travis-ci.org/capJavert/is-it-safe)
<h2>Utility for website or email danger checking.</h2>
<h3>Install</h3>
<p>
You will need pip tool for python to install this utility into your shell environment.<br />
Pip is included in python 3.x+<br />
Utility is compatible with python 2.7+<br />
<br />
$ git clone https://github.com/capJavert/is-it-safe.git is-it-safe<br />
$ cd is-it-safe <br />
$ pip install --editable .<br />
(you have to be root on linux or sudo <b>pip install --editable .</b> )<br />
<br />
After install you can use script as: <br />
<b>$ iisafe --website=google.com</b> or shorter <b>$ iisafe -w google.com</b>
</p>
<h3>Usage</h3>
<p>
Usage: iisafe [OPTIONS]<br />
<br />
Options:<br />
  -w, --website TEXT  Website that you wish to check. Default is None<br />
  -e, --email TEXT  Email address that you wish to check. Default is None<br />
  --help       Show this message and exit.<br />

<h3>To do</h3>
- Add more websites checking sources
- Add more email checking sources
