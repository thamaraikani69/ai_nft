import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage,Projection
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def f1(x,y):
	result=random.uniform(-1,1) * x**2 - math.sin(y**2) + abs(y-x)
	return result

def f2(x,y):
	result=random.uniform(-1,1) * x**3 - math.cos(y**3) + 2*x
	return result

total_generation=input('Enter No of nft images')

if total_generation=="":
	total_generation=1

bg_color=input("Enter Back Ground color ")
if bg_color=="":
	bg_color='white'

color=input("Enter color ")
if color=="":
	color='black'

for i in range(int(total_generation)):
	g=GenerativeImage(f1,f2)

	# Range of image & previous image seed 
	# g.generate(start=-2*math.pi, step=0.01, stop=0,seed=1018273)
	# g.generate(start=-2*math.pi, step=0.01, stop=0)
	g.generate()

	seed_=g.seed
	print(seed_)

	# RECTILINEAR, POLAR, AITOFF, HAMMER, LAMBERT and MOLLWEIDE
	# g.plot(projection=Projection.RECTILINEAR)
	project=[Projection.RECTILINEAR, Projection.POLAR]
	count=0
	for i in project:
		count+=1
		g.plot(color=color, bgcolor=bg_color,projection=i)

		# plt.show()

		g.save_image(file_adr=dir_path+'//image//'+str(seed_)+'_'+str(count)+'.png',depth=5)

		# save data and regenrate image
		g.save_data(file_adr=dir_path+'//data//'+str(seed_)+'_'+str(count)+".json")
		# g = GenerativeImage(data=open('nft.json', 'r'))

		# g.plot(color="red", bgcolor="black",projection=Projection.RECTILINEAR)

		# plt.show()