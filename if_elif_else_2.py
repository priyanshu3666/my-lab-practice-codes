#Program started
'''The input should be enter by user
x,y are the centre of circle.
r is the radius of circle
x1,y1 are the cordinates of point'''
x = int(input("Enter the x cordinate of centre"))
y = int(input("Enter the y cordinate of centre"))
r = int(input("Enter the radius of circle"))
x1 = int(input("Enter the x cordinate of point"))
y1 = int(input("Enter the y cordinate of point"))
d = ((x-x1)**2 + (y-y1)**2)**0.5  #d is the distance of point from centre of circle
if d < r :      #logic of checking point position start
    print("Point is inside the circle")
elif d == r :
    print("Point is on the circle")
else :
    print("Point is outside the circle")     #logic ends
#Program Ends
