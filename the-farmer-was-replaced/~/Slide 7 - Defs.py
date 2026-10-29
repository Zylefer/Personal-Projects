def reset():
	while get_pos_x()!=0:
		move(West)
	while get_pos_y()!=get_world_size()-1:
		move(North)
	for i in range(get_world_size()):
		for l in range(get_world_size()):
			harvest()
			if get_ground_type!=Grounds.Grassland:
				till()
			move(South)
		move(East)

def main():
	reset()
	while True:
		for column in range(get_world_size()):
			for row in range(get_world_size()):
				if (can_harvest()):
					harvest()
					plant(Entities.Grass)
				move(South)
			move(East)

if __name__=='__main__':
	main()