import os
import sys
from time import sleep

def calldir(dom):
    sleep(3)
    os.system('python3 dirsearch/dirsearch.py -u '+ dom +' -e php --simple-report=txt/DIRECT.txt')

