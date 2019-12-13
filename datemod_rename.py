import sys
import os
import datetime
import time

path = sys.argv[1]
target = os.listdir(path)


for filename in target:
	if not filename[0] == '.':
		old_filename = path + filename
		ext = os.path.splitext(filename)[1]
		created_date = time.ctime(os.path.getmtime(old_filename))
		formatted_date = datetime.datetime.strptime(created_date, '%a %b %d %H:%M:%S %Y').strftime('%Y-%m-%d-%H.%M.%S')
		new_filename = path + formatted_date + ext
		os.rename(old_filename, new_filename)
			