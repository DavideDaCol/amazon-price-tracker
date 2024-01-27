# Amazon Price Tracker
This Python script was built using Beautiful Soup 4 and it can be used to track multiple prices with a single scan.

### Features
- Add products using an input file: the links can be added either from the program or from the file (make sure you follow the format the program uses, **first the nickname then the link to trace on another line**)
- Scan the added products: the program will return the current price of every product in the input file, alongside the date of the scan
- list all added products: prints to the command line all the links in the input file
- remove a product: simply deletes one of the products from the input file

### Install
- Make sure Python3 is installed
- In the directory where you intend to run the program, run the following command:

`pip install -r requirements.txt`
- Execute the script from the terminal (make sure you have an internet connection):

`python3 tracker.py`

### Future features
- Add a perpetual scan option
- Output scans to file
- Functional GUI (Maybe in a separate fork)
