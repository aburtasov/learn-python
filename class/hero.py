class Hero:
    """Class to create Hero for our game"""
    def __init__(self,name,level,race):
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
        
    def show_hero(self):
        print(self.name,self.level,self.race,self.health)
        
    def level_up(self):
        """Upgrade level of Hero"""
        self.level = self.level + 1
        
    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + " start moving..." )
        
    def set_health(self,new_health):
        self.health = new_health
        