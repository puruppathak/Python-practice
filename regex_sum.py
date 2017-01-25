import re


list_sum = 0           # Initializing sum variable
hand = open ('trial.txt')      # Opening text file
for line in hand:
    line = line.rstrip()
    y=re.findall('[0-9]+',line)  #Extracting digits from the file
    if y:
    	
        for x in y:
         list_sum += int(x)      # int(x) converts string to numbers

if (list_sum == 0):
	print "No numbers found in the text file. Update the file"
else:
    print list_sum         
