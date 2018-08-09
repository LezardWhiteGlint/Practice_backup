#!/usr/bin/env python3

import subprocess

parts = ['phl','tw','sakura','jp','jp2','kt','st','st2','hk3','sgp','us',
        'us2','us3','down','down2','test']

for head in parts:
    Url = head + '.cn2ss.xyz'
    ping = subprocess.Popen(
        ['ping','-t','5',Url],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE)
    for line in ping.stdout.readlines():
        print(line)
    print('\n')
    ping.stdout.close()
    

