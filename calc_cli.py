area_room_list=[]
area_del_list=[]
wallpaper_list=[]
raport=-1

area_list=[]
def area_total(length, height, raport=-1):    
    if(raport!=-1):        
        return (length*height)-((height*raport)*((int(length/height))-1))

    perimeter={}    
    perimeter["length"]=length
    perimeter["height"]=height
    perimeter["area"]=(perimeter["length"]*perimeter["height"])
    area_list.append(perimeter)
    

def print_list(list_val):
    for x in range(len(list_val)):
        print(list_val[x])


#Room   
while(True):
    print("__Room__")
    length=float(input("length: "))
    height=float(input("height: "))
    area_total(length, height)
    choice=input("continue?: (y/n)")
    if(choice=='n'):
        area_room_list = area_list.copy()
        break

#del
while(True):
    print("__Del__")
    length=float(input("length: "))
    height=float(input("height: "))
    area_total(length, height)
    choice=input("continue?: (y/n)")
    if(choice=='n'):
        area_del_list=area_list.copy()
        break

print_list(area_room_list)
print_list(area_del_list)

#Wallpaper 
print("__Wallpaper__")
length=float(input("width: "))
height=float(input("length: "))
height=float(input("height`s room : "))
    
choice=input("Wallpaper with raport?: ")
if(choice=='y'):
    raport=float(input("raport: "))
        
areaWallpaper=area_total(length, height, raport)
print(areaWallpaper)


    