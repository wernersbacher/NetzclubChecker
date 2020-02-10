#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import random
import os
import datetime

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
CHECKER_PATH = "Checker.py"
CHECKER_PATH_ABS = os.path.join(DIR_PATH, CHECKER_PATH)

STATUS_PATH = "status.log"
STATUS_PATH_ABS = os.path.join(DIR_PATH, STATUS_PATH)

LOG_PATH = "error.log"
LOG_PATH_ABS = os.path.join(DIR_PATH, LOG_PATH)

while True: 
	cmd = ['python3', CHECKER_PATH_ABS]

	with open(STATUS_PATH_ABS, "w+") as f:
		print("Start Login, see the log file {} for the program output".format(STATUS_PATH_ABS))
		proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.PIPE)
		
		with open(LOG_PATH_ABS, "a+") as errfile:

			errfile.write("------------- NEW ERROR FROM EXCECUTION ---------------")
			for line in proc.stderr:
				sys.stdout.write(line)
				errfile.write(line)

		proc.wait()



	waittime = random.randint(10, 3600)
	print("Wait for {} seconds ({:.2f} hours)".format(waittime, waittime/60/60))
	time.sleep(waittime)

