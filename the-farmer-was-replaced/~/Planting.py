import Globals
import Sunflowers

def plantCrop(column, row):
	ground=get_ground_type()
	if (row==0 or row==(Globals.length-1)) and column<5:
		if ground!=Grounds.Soil:
			till()
		plant(Entities.Sunflower)
		if row==0:
			Globals.topSunflowerArray[column]=measure()
		else:
			Globals.botSunflowerArray[column]=measure()
	elif row>0 and row<(((Globals.length//3)*2)):
		if (ground!=Grounds.Grassland):
			till()
		if row%2==0:
			if column%2==0:
				plant(Entities.Grass)
			else:
				plant(Entities.Tree)
		else:
			if column%2==0:
				plant(Entities.Tree)
			else:
				plant(Entities.Grass)
	elif row>=(Globals.length//3)*2 and row<(Globals.length-1):
		if ground!=Grounds.Soil:
			till()
		plant(Entities.Carrot)
	else:
		if ground!=Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		


def harvestCrop(column, row):
	crop=get_entity_type()
	if crop!=Entities.Sunflower:
		harvest()
	elif crop==Entities.Sunflower:
		if Globals.doSunflowerCase:
			Sunflowers.sunflowerCase(column, row)
		else:
			harvest()
	