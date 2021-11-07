
import os
import re

def regex():
    txt = "The apples are ripe his time of year"
    x = re.search("The", txt)
    print(x)

def regex2():
    cwd = os.getcwd()
    print("Current working directory", cwd)

if __name__ == '__main__':
    regex()
    regex2()



