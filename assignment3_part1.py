#include<bits/stdc++.h>
from numpy import random, sqrt
import matplotlib.pyplot as plt
import numpy as np
import math

def increase_square_size (diameter_bigcircle_o, radius):
  diameter_bigcircle_2 = (2*diameter_bigcircle_o)
  square = plt.Rectangle((0,0), diameter_bigcircle_2, diameter_bigcircle_2,fc='black',ec="red")
  plt.gca().add_patch(square)
  plt.axis('scaled')
  return[diameter_bigcircle_2]






PI = 3.14
N = int(input("Enter number of spheres: "))
x = random.normal(size= N)
area = np.zeros(N)
total_area=0;
for i in range(N):
 print(i)
 area[i] = PI * x[i] * x[i]
 print("Area of circle is = %.2f" %area[i] )
 
for n in area:
    total_area = total_area + n
    


print("Total area of all circles is = %.2f" %total_area)
#to find approximate size of square taking the area of total circles as one circle's area
diameter_bigcircle = 2*sqrt(total_area/PI)
print("diameter of bigcircle is = %.2f" %diameter_bigcircle)
area_square = diameter_bigcircle*diameter_bigcircle
print("Approximate area of square is = %.2f" %area_square)

# plt.axes()
def area_square(diameter_bigcircle):
 square = plt.Rectangle((0,0), diameter_bigcircle, diameter_bigcircle,fc='black',ec="red")
 plt.gca().add_patch(square)
 plt.axis('scaled')

area_square(diameter_bigcircle)
print(area)
temp =0;
for k in range(0, N):    
    for j in range(k+1, N):    
        if(area[k] < area[j]):    
            temp = area[k];    
            area[k] = area[j];    
            area[j] = temp;  

print(area)



p=0;
for m in area:
    
    diameter = 2*sqrt(m/PI)
    radius = diameter/2
    center = sqrt(diameter*diameter)/2
    if p==0:
      circle1 = plt.Circle((center,center),radius,fc='white',ec='red')
      plt.gca().add_patch(circle1)
      radius1 = radius;
    elif p==1:
       if (((radius1+radius) <= sqrt(8*(center*center) + 2*(diameter_bigcircle*diameter_bigcircle))) == 1):
        circle2 = plt.Circle((diameter_bigcircle - center,diameter_bigcircle - center),radius,fc='white',ec='red')
        plt.gca().add_patch(circle2)
       else: 
             diameter_bigcircle_1 = increase_square_size(diameter_bigcircle,radius)
             area_square(diameter_bigcircle_1)
             circle2 = plt.Circle((diameter_bigcircle - center,diameter_bigcircle - center),radius,fc='white',ec='red')
             plt.gca().add_patch(circle2)
             
             break
    elif p==2:
       circle3 = plt.Circle((center,diameter_bigcircle - center),radius,fc='white',ec='red')
       plt.gca().add_patch(circle3)
    elif p==3:
        circle4 = plt.Circle((diameter_bigcircle - center, center),radius,fc='white',ec='red')
        plt.gca().add_patch(circle4)
       
    p +=1;
    
     
plt.show()



