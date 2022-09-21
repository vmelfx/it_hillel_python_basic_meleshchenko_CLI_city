# CLI City - limited data about cities

## Description
Application for getting info about cities using python.  
This application was created as part of my thesis in IT Hillel school.

## Requirements
Python 3.10+  
click module  
requests module  
pycountry-convert module

## Installation
```
pip install requests
```
```
pip install click
```
```
pip install pycountry-convert
```
```
git clone https://github.com/vmelfx/it_hillel_python_basic_meleshchenko_CLI_city.git
```

## Usage
To use this application, go to the directory you cloned repo to and run main.py, with the name of the city as parameter:
```
>>> python main.py Brest
>>> 
--------------
Brest

Belarus
BYN
339700
==============
--------------
Brest

France
EUR
300300
==============
```
## Features of use
If there are several cities, information will be displayed for each of them.

## License
[MIT](https://choosealicense.com/licenses/mit/)