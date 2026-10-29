def reset():
	while get_pos_x()!=0:
		move(West)
	while get_pos_y()!=get_world_size()-1:
		move(North)
	for i in range(get_world_size()):
		for l in range(get_world_size()):
			harvest()
			if get_water()<.9:
				use_item(Items.Water)
			if get_ground_type()!=Grounds.Grassland:
				till()
			move(South)
		move(East)

def main():
	reset()
	while True:
		for column in range(get_world_size()):
			for row in range(get_world_size()):
				if get_water()<.9:
					use_item(Items.Water)
				if can_harvest():
					harvest()
				if column==0 or column==1:
					plant(Entities.Grass)
				elif column==2 or column==3:
					if column%2==0:
						if row%2==0:
							plant(Entities.Tree)
						else:
							plant(Entities.Grass)
					else:
						if row%2!=0:
							plant(Entities.Tree)
						else:
							plant(Entities.Grass)
				elif column==4 or column==5:
					if get_ground_type()!=Grounds.Soil:
						till()
					plant(Entities.Carrot)
				move(South)
			move(East)

if __name__=='__main__':
	main()