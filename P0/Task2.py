"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
list_of_phone_numbers = defaultdict(int)
for each in calls:
	call_time = int(each[3])
	incoming = each[0]
	sending = each[1]
	list_of_phone_numbers[incoming] +=  call_time
	list_of_phone_numbers[sending] +=  call_time
telephone_number = max(list_of_phone_numbers, key=list_of_phone_numbers.get)



print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format( telephone_number ,list_of_phone_numbers[telephone_number]))



