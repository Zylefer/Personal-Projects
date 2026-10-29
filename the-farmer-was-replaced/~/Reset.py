def reset(worldDepth):
	while get_pos_x()!=0:
		move(West)
	while get_pos_y()!=worldDepth-1:
		move(North)