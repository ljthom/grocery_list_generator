# Pantry
## CMCS495 Capstone - Grocery List Generator
### Development Team:
- Nixon Aguilar - Database Design/Implementation
- Zach Burson - Back End Development
- Andres Canos - Project Management
- Cameron Hayes - Content Generation/Scraper Implementation
- Carleton Swartz - Quality Assurance/Testing
- Lukas Thomas - Front End Development

## Requirements before using:  
- Pantry works on a PC running Linux, Windows, and macOS but has not yet been tested on macOS at the time of this user guide entry.
- Must have Python 3.3 or greater installed: https://www.python.org/downloads/
- Must have installed pip: https://pip.pypa.io/en/stable/installation/
- Flask version 2.2.2+




### Installing the application:
- Download the application as a zip file from https://github.com/ljthom/grocery_list_generator
- Unzip grocery_list_generator-main into directory of preference
- Windows: Open a command prompt
- Linux & macOS: Open a terminal
- Navigate to the grocery_list_generator directory 

- Enter 'python -m pip install -e .'


### Starting the application:  

- Windows: Open a command prompt
- Linux & macOS: Open a terminal
- Navigate to the grocery_list_generator directory 
- Enter “python -m flask –-app pantry run” to run the program at the localhost.
- Open a browser of choice and enter 127.0.0.1:5000 as the URI to open the graphical user interface.

### Running the Scraper:  

- Windows: Open a command prompt
- Linux & macOS: Open a terminal
- Navigate to the grocery_list_generator/pantry/db directory 
- Enter “python3 db_scraper.py -u \<URL1\> [\<URL2\>] [-n \<Num Results\>]”.
- ```usage: db_scraper.py [-h] [-u URL [URL ...]] [-n NUM]

optional arguments:
  -h, --help            show this help message and exit
  -u URL [URL ...], --url URL [URL ...]
                        Enter any number of URLs
  -n NUM, --num NUM     Number of results to return
- Information for populating DB will come soon ...
