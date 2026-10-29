def sunflowerArraySetup(row):
	while get_pos_x()!=0:
		move(West)
	if row==0:
		while get_pos_y()!=0:
			move(South)
	else:
		while get_pos_y()!=row:
			move(North)
	array=[]
	for i in range(5):
		if measure()==None:
			array.append(0)
		else:
			array.append(measure())
		move(East)
	return array

length=get_world_size()
topSunflowerArray=sunflowerArraySetup(0)
botSunflowerArray=sunflowerArraySetup(length-1)
sunflowerSkips=0
doSunflowerCase=True
doSunflowerCase8Skips=False
	