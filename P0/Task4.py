"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
correct_nos = set()
for phone in texts:
	correct_nos.add(phone[0])
	correct_nos.add(phone[1])
for each in calls:
	correct_nos.add(each[1])

scam_nos = set()
print("These numbers could be telemarketers: ")
for each in calls:
	if each[0] not in  correct_nos :
		scam_nos.add(each[0])
print(sorted(scam_nos))