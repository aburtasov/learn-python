cars = ["volvo","skoda","lada","bmw","porshe"]

for car in cars:
    print(car.upper())
    
    
for x in range(1,6):
    print(x)
    
print("================================")
#-----------------------------------------------------   
mynumber_list = list(range(0,10))
print(mynumber_list)
print("================================")
#-----------------------------------------------------

for x in mynumber_list:
    x = x * 2
    print(x)
    
print("================================")

mynumber_list.reverse()
print(mynumber_list)

print("================================")

print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum number is: " + str(sum(mynumber_list)))

print("================================")

new_cars = cars[0:3]
print(new_cars)

new_cars = cars[:2]
print(new_cars)

new_cars = cars[-3:-1]
print(new_cars)

print("================================")

new_cars = cars # link to list, not a new list
new_cars = cars[:] # full copy