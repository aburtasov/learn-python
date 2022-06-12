#-----------------------------------------
#Program by Andrey b.
#
#
# Version    Date         Info
# 1.0        2022    Initial Version
#----------------------------------------
#
# 

enemy = {
    'loc_x':70,
    'loc_y':50,
    'color':'green',
    'health':100,
    'name':'Mudillo'
}

print(enemy)

print(enemy['name'])
print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))

#--------------------------------------------

enemy['rang'] = 'admiral'
print(enemy)

#--------------------------------------------

del enemy['rang']
print(enemy)

#-------------------------------------------

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['loc_y'] = enemy['loc_y'] + 5
enemy['health'] = enemy['health'] - 30

if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())