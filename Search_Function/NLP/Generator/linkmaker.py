
import random
import string
import csv

f = open('Search_Function\zoomlink.csv', 'w')
writer = csv.writer(f)



length = int(11) 
num = string.digits
num = string.digits
all =  num + num

zoom = "zoomlink"
i = 0
while i <= 100:
    temp = random.sample(all,length)
    password ="https://berkeley.zoom.us/j/" + "".join(temp)
    i = i + 1
    total = i,password,zoom
    writer.writerow(total)
    #print(i, password,zoom)
    #print(total)


