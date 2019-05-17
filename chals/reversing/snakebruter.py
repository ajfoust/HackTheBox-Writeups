#!/usr/bin/python2.7
chains = [0x74, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x74, 0x72, 0x6f, 0x6c, 0x6c]
keys = [0x70, 0x61, 0x73, 0x73, 0x77, 0x6f, 0x72, 0x64, 0x21, 0x21]
chars = []
'''
for i in range(1000):
    lock = i * 2
    lock = lock + 10
    lock = lock /2
    lock = lock - i
    #print('lock: ' + str(i) + " " + str(lock))
'''   
lock = 5

for key in keys:
	keys_encrypt = lock ^ key
	chars.append(keys_encrypt)
for chain in chains:
	chains_encrypt = chain + 0xA
	chars.append(chains_encrypt)
#pass_input = raw_input('enter pass')
#print(pass_input)
correct = []
for char in chars:
	for keyboi in range(255): 
		passes = str(unichr(keyboi))
		#print(str(char) +":"+ str(keyboi))
		#print(passes)
		if passes == str(chr(char)):
			
			correct.append(passes)
			
			
			break
		
for let in correct:
	print(correctlet]),