# Вывод картинки на экран и двигать ее с помощью клавиатуры и мышки


import pygame

max_x = 800
max_y = 600
game_over = False
bg_color = (0,0,0) # black rgb

pygame.init()

screen = pygame.display.set_mode((max_x,max_y),pygame.FULLSCREEN)

pygame.display.set_caption("My first pygame Game!")

# print(pygame.image.get_extended())  // проверка изображения

myimage = pygame.image.load('/home/aburtasov/python/py_git/learn-py/pygame/krot.webp').convert() # загрузка картинки

myimage = pygame.transform.scale(myimage, (100,100))



x = 500
y = 100

#-----------------------------Main game Loop---------------------------------
while game_over == False:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #game_over = True
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x = x - 20
            if event.key == pygame.K_RIGHT:
                x = x + 20
            if event.key == pygame.K_UP:
                y = y - 20 
            if event.key == pygame.K_DOWN:
                y = y + 20
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    
    screen.fill(bg_color) # заполняем бэкграунд черным цветом
    
    screen.blit(myimage, (x,y)) # рисуем картинку
    
    pygame.display.flip()   # вывод на экране
    



