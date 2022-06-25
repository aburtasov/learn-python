# Вывод картинки на экран и двигать ее с помощью клавиатуры и мышки


import pygame

max_x = 800
max_y = 600
image_size = 100

game_over = False
bg_color = (0,0,0) # black rgb

pygame.init()

screen = pygame.display.set_mode((max_x,max_y),pygame.FULLSCREEN)

pygame.display.set_caption("My first pygame Game!")

# print(pygame.image.get_extended())  // проверка изображения

myimage = pygame.image.load('/home/aburtasov/python/py_git/learn-py/pygame/krot.webp').convert() # загрузка картинки

myimage = pygame.transform.scale(myimage, (image_size,image_size))



x = 500
y = 100

move_right = False
move_left = False
move_up = False
move_down = False

#-----------------------------Main game Loop---------------------------------func read_keyboard()
while game_over == False:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #game_over = True
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True  #x = x - 20
            if event.key == pygame.K_RIGHT:
                move_right = True #x = x + 20
            if event.key == pygame.K_UP:
                move_up = True    #y = y - 20 
            if event.key == pygame.K_DOWN:
                move_down = True  #y = y + 20
        
        if event.type == pygame.KEYUP:
                #game_over = True
            
            if event.key == pygame.K_LEFT:
                move_left = False  
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False    
            if event.key == pygame.K_DOWN:
                move_down = False 
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos 
        
    if move_left == True:
            x = x - 1
            if x < 0:
                x = 0
    if move_right == True:
            x = x + 1
            if x > max_x - image_size:
                x = max_x - image_size
    if move_up == True:
            y = y - 1
            if y < 0:
                y = 0
    if move_down == True:
            y = y + 1
            if y > max_y - image_size:
                y = max_y - image_size
        
                
    
    
    screen.fill(bg_color) # заполняем бэкграунд черным цветом
    
    screen.blit(myimage, (x,y)) # рисуем картинку
    
    pygame.display.flip()   # вывод на экране
    



