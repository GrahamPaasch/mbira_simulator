# all possible notes
# possible x coordinates
#  | 15 45 75 | 105 135 165 | 195 225 255 | 285 315 345 |
# possible y coordinates
#  15, 45, 75, 105
# only y value 15 can be associated with register R1
# only y value 45 can be associated with register R2
# only y value 75 can be associated with register L1
# only y value 105 can be associated with register L2
# R2-1@(15,15)
# R2-2@(15,15)
# R2-3@(15,15)
# R2-4@(15,15)
# R2-5@(15,15)
# R2-6@(15,15)
# R2-7@(15,15)

register = 'L2' 
key = '7'
x = '15'
y = '105'
note = register + '-' + key + '@(' + x + ',' + y + ')'

while note != 'L2-1@(345,105)':
	
	print(note)
	key = str(int(key) - 1)
	note = register + '-' + key + '@(' + x + ',' + y + ')'
	if key == '1':
		x = str(int(x) + 30)
		key = '8'
else:
	
	print(note)