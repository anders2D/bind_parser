# Bind parser
## _Simple bind parser_
Little python script to parse a BIND Server log and send it to Lumu using the Send DNS Queries method of the Custom Collector API
## Features

- Parse bind log
- Use API Collector to send DNS queries information

## Tech

Techologies used:

- Python 3.8
-- requests library
-- pandas library

## Installation

You need to have python 3.8, here installation guide [Installation guide Windows](https://blog.devgenius.io/python-for-beginners-how-to-install-python-3-8-3-for-windows-pc-a84f5d237c19) or [Installation guide Linux](https://linuxize.com/post/how-to-install-python-3-8-on-ubuntu-18-04/).

After get python3.8, if you want to install packages in your computer then use the following commands
```sh
pip3 install -e requirements.txt
```

else you can install virtualenv  to create a virtual environment
```sh
pip install virtualenv
```
or
```
pip3 install virtualenv
```
Clone or download this respository
```sh
git clone https://github.com/anders2D/bind_parser.git
```
Go to bind_parser folder, if you are are going to use virtualenv, please, use following comands

_Linux_

```sh
source bin/activate
```

Enjoy scripts :)
## Usage

Go to repository folder, an just use following to execute script.
```sh
python3 bind_log.py filename
```
example
```sh
python3 bind_log.py queries
```
output:
```sh
Sending data to lumu API
Total records 16967

Client IPs Rank
--
                                           name  counts R. frecuency
0                                  pizzaseo.com    4626    27.2647 %
1                                            sl    3408    20.0860 %
2                    MNZ-efz.ms-acdc.office.com      67     0.3949 %
3  global.asimov.events.data.trafficmanager.net      31     0.1827 %
4                                www.google.com      30     0.1768 %

Host Rank
--
         client_ip  counts R. frecuency
0   111.90.159.121    3375    19.8916 %
1      45.231.61.2    1251     7.3731 %
2     187.45.191.2    1089     6.4183 %
3  190.217.123.244     738     4.3496 %
4       5.63.14.45     634     3.7367 %
```