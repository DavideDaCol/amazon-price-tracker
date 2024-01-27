import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import date


def input_file(arg):
    try:
        inp = open("input.txt", arg)
    except OSError:  # creates file if it doesn't exist using the OSError exception
        inp = open("input.txt", "x")
        print("no input file was present. An input file has just been created in this directory.\n")
    return inp


def check_not_empty(inpfile):
    inpfile.seek(0, os.SEEK_END)  # goes to EOF
    if inpfile.tell():  # if the file has contents it goes back to the beginning and returns true
        inpfile.seek(0)
        return True
    else:
        return False


def eof(file):
    pos=file.tell()
    char = file.read(1)
    file.seek(pos)
    if not char:
        return True
    else:
        return False


def file_scan(inpFile):
    if check_not_empty(inpFile):
        while not eof(inpFile):
            nickname = inpFile.readline()[:-1]
            url = inpFile.readline()
            timeReq = date.today()
            try:
                urlReq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})  # gets the html from the given url as "firefox"
            except ValueError: # skips scan if url is not valid
                print(f"the URL for {nickname} could not be resolved.\n")
                break
            page = urlopen(urlReq).read()  # puts html in a page element
            soup = BeautifulSoup(page, 'lxml')  # creates a soup element for web scraping with lxml parsing
            priceTag = soup.find_all('span', class_="a-price-whole")  # using find all because find cannot be iterated
            if not priceTag: # skips scan if the url doesn't have a price in it
                print(f"The URL for {nickname} is not a valid Amazon URL.\n")
                break
            for printPrice in priceTag:
                string = printPrice.text
                print(f'{nickname} costs {string} as of {timeReq}\n')
                break  # stops at first occurrence. bs4 is kinda weird, but it works, so...
    else:
        print("sorry! the supplied file is empty!")


while True:
    print("welcome to the Amazon price tracker! Please insert your choice:")
    print("a - add Amazon URL \ns - scan the present products \nr - remove a URL from the list \nl - list all links in"+ 
    " the input file \ne - exit the program")
    choice = input("your choice here -> ")
    print(" ")
    match choice:
        case 'a': # simply writes to file
            list = input_file("a")
            nick = input("please give this product a nickname: ")
            url = input("please insert the Amazon URL you would like to add: ")
            list.write(nick+"\n")
            list.write(url + "\n")
            list.close()
        case 'l': # reads off the input file
            list= input_file("r")
            print(list.read())
            list.close()
        case 's': # scans using bs4
            list = input_file("r")
            file_scan(list)
            list.close()
        case 'r': # lists input file, asks the nick, removes said line and the following
            list = input_file("r")
            lines=list.readlines()
            list.close()
            list = input_file("r") # had to separate this to avoid I/O issues
            print(list.read())
            list.close()
            list = input_file("w")
            remove=input("insert the product you would like to remove: ")
            check = False
            for line in lines:
                if (line.strip("\n")!=remove and not check): # deletes 2 adjacent lines
                    list.write(line)
                    check = False
                else:
                    check = not check # else makes the delete condition run twice if triggered
        case 'e':
            print("exiting...")
        case _:
            print("that option isn't present! please try again.")
    if choice == 'e': # exit contition
        break
