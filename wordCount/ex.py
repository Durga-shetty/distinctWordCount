import re
import unicodedata
from unidecode import unidecode
import sys


list1=[]
with open("symbols.txt","r") as f:
    for x in f:
            stripline=x.strip()
            list2=stripline.split()
            list1+=list2
    print(list1)
    numbers=re.compile('[0-9]+(\.[0-9][0-9]?)?')
    symbol=re.compile('\$')
    unit=re.compile('Rs|million|millions|billion|billions|crore|thousand|thousands|crores|lakh|lkhs')
    for i, ele in enumerate(list1):
        if numbers.search(ele):
            if ele[-2].isdigit():
              print(list1[i])
        if symbol.search(ele):
            if not re.search('\d',ele):
                print(list1[i])
        if unit.search(ele):
            print(list1[i])
#h=re.findall("([0][0-9]|[1][0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/([0-9]{4})",x)'''


