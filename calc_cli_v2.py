wall_param=[
    {"length":3, "height":2.5},
    {"length":3, "height":2.5},
    {"length":4, "height":2.5},
    {"length":4, "height":2.5},
]

del_wall_param=[
    {"length":1.5, "height":1.3},
    {"length":2, "height":1.5},
    {"length":0.9, "height":2.3},
    {"length":0.8, "height":2.3},
]

wallpaper_param={"width":1.06, "length":10, "raport":0.32, "height_room":2.65}    

def room_area(wall):
    area_wall=0
    for x in range(len(wall)):
        area_wall += (wall[x]["length"]) * (wall[x]["height"])
    return area_wall

def del_wall_area(free_wall):
    area_del=0
    for x in range(len(free_wall)):
        area_del += (free_wall[x]["length"]) * (free_wall[x]["height"])
    return area_del

def room_area_total(wall, free_wall):
    area_wall=0
    area_del=0
    for x in range(len(wall)):
        area_wall += (wall[x]["length"]) * (wall[x]["height"])    
    for x in range(len(free_wall)):
        area_del += (free_wall[x]["length"]) * (free_wall[x]["height"])
    
    return (area_wall-area_del)

def wallp_area(wallpaper):
    wallpaper_area=wallpaper["width"] * wallpaper["length"]
    raport_area=wallpaper["width"] * wallpaper["raport"]
    strip=wallpaper["length"] // wallpaper["height_room"] 
    total_wallpaper_area=(wallpaper_area-(raport_area*strip))
    return total_wallpaper_area

def needroll(room_area, wallpaper_area):
    return room_area / wallpaper_area

only_room=room_area(wall_param)
only_del=del_wall_area(del_wall_param)
total_area=room_area_total(wall_param,del_wall_param)
wallpaper_area=wallp_area(wallpaper_param)
roll=needroll(total_area,wallpaper_area)
print("***needroll-CLI***")
print("Room area:",only_room)
print("Delete area:",only_del)
print("Total area:",total_area)
print("Wallpaper area:",wallpaper_area)
print("***ROLL***",roll)
