'''
this tool will get your clipboard.
if there is any we can do, we will do it.
'''
from rule import rule
#from tools import detect_change
import pyperclip as clip
from time import sleep

# global var defined
detent_time = 2 # some seconds
FLAG = 1 # loop FLAG
old_str = ""

# main loop
while(FLAG):
    sleep(detent_time)
    a = clip.paste()
    if a==old_str:
        continue
    print('get new paster board value: ' + a + '\n')
    a = rule(a)
    print('revised: ' + a + '\n')
    clip.copy(a)
    old_str = a
