#-----------------------------------------
#Program by Andrey b.
#
#
# Version    Date         Info
# 1.0        2022    Initial Version
#----------------------------------------
#


from email.mime import image


enemy = {
    'loc_x':70,
    'loc_y':50,
    'color':'green',
    'health':100,
    'name':'Mudillo',
    'awards':['Za Stalina','Za Lenina'],
    'image' : ['image1.jpg','image2.jpg','image3.jpg']
}

all_enemies = []


#all_enemies.append(enemy)
#all_enemies.append(enemy)
#all_enemies.append(enemy)

for x in range(0,10):
    all_enemies.append(enemy.copy())
    
for enem in all_enemies:
    print(enem)

#print(all_enemies)

all_enemies[3]['health'] = 30
all_enemies[2]['name'] = 'Kozel'
print("=========================")