#progrm started
length = eval(input("enter length of floor"))
breadth = eval(input("enter breath of floor"))
area = length*breadth
l_tile = eval(input("enter length of tile"))
b_tile = eval(input("enter breath of tile"))
area_tile = l_tile*b_tile
total_tile = area//area_tile
print("The total tile require for floor =",total_tile)
                    
