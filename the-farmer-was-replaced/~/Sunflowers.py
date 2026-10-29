import Globals
import Planting

def sunflowerCase(column, row):
	greatestPetals=True
	if Globals.doSunflowerCase8Skips:
		if Globals.sunflowerSkips>=8:
			harvest()
			plantCrop(column, row)
			if row==0:
				Globals.topSunflowerArray[column]=measure()
			elif row==Globals.length-1:
				Globals.botSunflowerArray[column]=measure()
	if row==0:
		for index in range(5):
			if column<5 and (Globals.topSunflowerArray[column]<Globals.topSunflowerArray[index] or Globals.topSunflowerArray[column]<Globals.botSunflowerArray[index]):
				greatestPetals=False
				break
	elif row==Globals.length-1:
		for index in range(5):
			if column<5 and (Globals.botSunflowerArray[column]<Globals.topSunflowerArray[index] or Globals.botSunflowerArray[column]<Globals.botSunflowerArray[index]):
				greatestPetals=False
				break
	if greatestPetals:
		harvest()
		Globals.sunflowerSkips=Globals.sunflowerSkips/3
		Planting.plantCrop(column, row)
		if column<5:
			if row==0:
				Globals.topSunflowerArray[column]=measure()
			elif row==Globals.length-1:
				Globals.botSunflowerArray[column]=measure()
	else:
		Globals.sunflowerSkips+=1