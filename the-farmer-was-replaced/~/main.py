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
					Planting.harvestCrop(column, row)
				Planting.plantCrop(column, row)
				if (get_water()<=.99):
					use_item(Items.Water) 
				move(South)
			move(East)
			
if __name__=='__main__':
	main()