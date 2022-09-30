# import libraries
import time
import csv
import os

# timer starts as soon as script runs
starttime = time.time()
lasttime = starttime
lapnum = 0

# create empty lists to store values
laptimes = []
lapnums = []

print("\nENTER drücken, um Runden zu zählen.\nSTRG+C um abzubrechen")

try:
	while True:

		# Input for the ENTER key press
		input()

		# total time
		totaltime = round((time.time() - starttime), 2)

		minutes = round((totaltime / 60), 0)
		seconds = round((totaltime % 60), 0)

		# current laptime
		laptime = round((time.time() - lasttime), 2)

		# print times in terminal
		print("Runde: " + str(lapnum))

		if totaltime < 60:
			print("Gesamtzeit: " + str(totaltime))
		else:
			print("Gesamtzeit: " + str(minutes) + ":" + str(seconds))

		print("Rundenzeit: " + str(laptime))

		print("-" * 20)

		# add laptime to laptimes list
		# add lapnumber to lapnums list
		laptimes.append(str(laptime))
		lapnums.append(lapnum)

		# update lasttime and increment lapnum
		lasttime = time.time()
		lapnum += 1

# Stop counting when CTRL+C is pressed
except KeyboardInterrupt:

	# convert decimal point to comma for Excel (german version!)
	# save lapnums and laptimes as list of tuples
	# get cwd to show user where output is saved
	laptimes_comma = [s.replace('.', ',') for s in laptimes]
	xy_values = list(zip(lapnums, laptimes_comma))
	cwd = os.getcwd()

	# create and write to output csv file
	with open('laptimer.csv', 'w', newline='') as f:
		write = csv.writer(f)
		write.writerow(["Runde", "Zeit [s]"])
		for element in xy_values:
			write.writerow(element)
		print("laptimer.csv wurde hier abgespeichert:\n" + cwd + "\n")
