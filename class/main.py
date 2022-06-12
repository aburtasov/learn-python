from hero import Hero
# from hero import *
#--------------------------------------------------------------
        
myhero1 = Hero("Johnny", 80, "white")
myhero2 = Hero("Alex", 81, "black")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()

#  Can be: myhero2.health = 70

myhero2.set_health(70)
myhero2.show_hero()