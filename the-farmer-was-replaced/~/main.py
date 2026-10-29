import Globals
import Reset
import Init
import Planting

def main():
	Reset.reset(Globals.length)
	Init.ABSOLUTELY_MUST_DO()
	
	while True:
		for column in range(Globals.length):
			for row in range(Globals.length):
				if can_harvest():
					if column%2==0:
						Planting.harvestCrop(get_pos_x(), get_pos_y())
					else:
						Planting.harvestCrop(get_pos_x(), get_pos_y())
				if column%2==0:
					Planting.plantCrop(get_pos_x(), get_pos_y())
				else:
					Planting.plantCrop(get_pos_x(), get_pos_y())
				use_item(Items.Water) 
				if column%2==0 and row!=Globals.length-1:
					move(South)
				elif column%2==1 and row!=0:
					move(North)
			move(East)
			
if __name__=='__main__':
	main()