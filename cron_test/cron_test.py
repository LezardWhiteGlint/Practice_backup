#!/usr/bin/env python3

import time
import os
os.chdir('/Users/lezardvaleth/Documents/Python/cron_test')

f = open(time.asctime() + '.txt','w')
f.close()
