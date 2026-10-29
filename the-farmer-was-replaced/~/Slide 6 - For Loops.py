while True:
	for column in range(get_world_size()):
		for row in range(get_world_size()):
			if (can_harvest()):
				harvest()
				plant(Entities.Grass)
			move(South)
		move(East)