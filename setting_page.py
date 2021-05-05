#settings_page
from pygame import *
from random import*
from math import*


springRect=Rect(100,25,400,75)  #themes
summerRect=Rect(550,25,400,75)
fallRect=Rect(100,125,400,75)
winterRect=Rect(550,125,400,75)
exitRect=Rect(750,575,100,100)
cancelRect=Rect(875,575,100,100)


redRect=Rect(100,575,255,20)    #allows the user to select the values of RGB himself to adjust the canvas colour
greenRect=Rect(100,615,255,20)
blueRect=Rect(100,655,255,20)
white=(255,255,255)
black=0

music1Rect=Rect(350,225,50,50)  #musics
music2Rect=Rect(450,225,50,50)
music3Rect=Rect(550,225,50,50)
music4Rect=Rect(650,225,50,50)

volumeRect=Rect(350,300,350,25)

spring_theme=image.load('springTheme.jpg')  #pictures for each theme
spring_theme=transform.scale(spring_theme,(398,73))
summer_theme=image.load('summerTheme.jpg')
summer_theme=transform.scale(summer_theme,(398,73))
fall_theme=image.load('fallTheme.jpg')
fall_theme=transform.scale(fall_theme,(398,73))
winter_theme=image.load('winterTheme.jpg')
winter_theme=transform.scale(winter_theme,(398,73))


red=image.load('red_shades.png')    #picturs to indicate shades of RGB
red=transform.scale(red,(redRect.width,redRect.height))
green=image.load('green_shades.png')
green=transform.scale(green,(greenRect.width,greenRect.height))                   
blue=image.load('blue_shades.png')
blue=transform.scale(blue,(blueRect.width,blueRect.height))
ok_button=image.load('ok.png')
ok_button=transform.scale(ok_button,(exitRect.width,exitRect.height))
cancel_button=image.load('cancel.png')
cancel_button=transform.scale(cancel_button,(cancelRect.width,cancelRect.height))

music1=image.load('note1.png')  #pictures of each music
music1=transform.scale(music1,(49,49))
music2=image.load('note2.png')
music2=transform.scale(music2,(49,49))
music3=image.load('note3.png')
music3=transform.scale(music3,(49,49))
music4=image.load('note4.png')
music4=transform.scale(music4,(49,49))
                    

def setting(screen,BackGround): #draws the basic layout of the setting page
    screen.blit(BackGround,(0,0))
    settingTheme(screen)
    settingMusic(screen)
    screen.blit(red,(redRect.x,redRect.y))
    screen.blit(green,(greenRect.x,greenRect.y))
    screen.blit(blue,(blueRect.x,blueRect.y))
    
def settingTheme(screen):   #draws the themes
    draw.rect(screen,white,springRect)
    draw.rect(screen,white,summerRect)
    draw.rect(screen,white,fallRect)
    draw.rect(screen,white,winterRect)
    draw.rect(screen,white,exitRect)
    draw.rect(screen,white,cancelRect)
    draw.rect(screen,0,springRect,3)
    draw.rect(screen,0,summerRect,3)
    draw.rect(screen,0,fallRect,3)
    draw.rect(screen,0,winterRect,3)
    screen.blit(ok_button,(exitRect.x,exitRect.y))
    screen.blit(cancel_button,(cancelRect.x,cancelRect.y))
    screen.blit(spring_theme,(101,26))
    screen.blit(summer_theme,(551,26))
    screen.blit(fall_theme,(101,126))
    screen.blit(winter_theme,(551,126))


def settingMusic(screen):   #draws the musics
    draw.rect(screen,white,music1Rect)
    draw.rect(screen,white,music2Rect)
    draw.rect(screen,white,music3Rect)
    draw.rect(screen,white,music4Rect)
    draw.rect(screen,0,music1Rect,3)
    draw.rect(screen,0,music2Rect,3)
    draw.rect(screen,0,music3Rect,3)
    draw.rect(screen,0,music4Rect,3)
    screen.blit(music1,(351,226))
    screen.blit(music2,(451,226))
    screen.blit(music3,(551,226))
    screen.blit(music4,(651,226))

def volumeBar(screen):  #draws the rect that allows the user to change the volume
    draw.rect(screen,white,volumeRect)
    draw.rect(screen,0,volumeRect,3)
    
def setting_main(screen,BackGround,background,background_picture,canvas_colour,eraser_frame,music,volume):  #this is the part where the setting works
    setting(screen,BackGround)  
    settingMusic(screen)
    volumeBar(screen)
    run=True
    new_music=music     #first, everything set from before will be copied into the settings
    new_volume=volume
    canvas_colour_change=False
    new_canvas_colour=canvas_colour
    R,G,B=canvas_colour
    new_eraser_frame=eraser_frame
    low_Rcolour=False
    low_Gcolour=False
    low_Bcolour=False
    BackG=background_picture
    other=0
    draw.rect(screen,(100,255,100),(355,305,int(volume*100/(100/350)),15))
    if R>250:
        draw.rect(screen,(75,75,75),(100+R-5,575,5,20))
    else:
        draw.rect(screen,(75,75,75),(100+R,575,5,20))
    if G>250:
        draw.rect(screen,(75,75,75),(100+G-5,615,5,20))
    else:
        draw.rect(screen,(75,75,75),(100+G,615,5,20))
    if B>250:
        draw.rect(screen,(75,75,75),(100+B-5,655,5,20))
    else:
        draw.rect(screen,(75,75,75),(100+B,655,5,20))
       
    while run:
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        for e in event.get():   
            if e.type==MOUSEBUTTONDOWN:
                if e.button==1:
                    LeftClick=True
                    if springRect.collidepoint((mx,my)):    #if the user clicks on one of the four themes, the rect of the theme will be highlighted and the theme will change to the selected theme
                        BackG,other1=background(1)
                        settingTheme(screen)
                        draw.rect(screen,(255,0,0),(springRect),3)
                    elif summerRect.collidepoint((mx,my)):
                        BackG,other1=background(2)
                        settingTheme(screen)
                        draw.rect(screen,(255,0,0),(summerRect),3)
                    elif fallRect.collidepoint((mx,my)):
                        BackG,other1=background(3)
                        settingTheme(screen)
                        draw.rect(screen,(255,0,0),(fallRect),3)
                    elif winterRect.collidepoint((mx,my)):
                        BackG,other=background(4)
                        settingTheme(screen)
                        draw.rect(screen,(255,0,0),(winterRect),3)

                    if music1Rect.collidepoint((mx,my)):    # if the user clicks on the music rects, it will be highlighted and music will change
                        settingMusic(screen)
                        draw.rect(screen,(255,0,0),music1Rect,3)
                        mixer.music.load('KissTheRain.mp3')
                        mixer.music.play(-1)
                        new_music='play'
                    elif music2Rect.collidepoint((mx,my)):
                        settingMusic(screen)
                        draw.rect(screen,(255,0,0),music2Rect,3)
                        mixer.music.load('Cotan.mp3')
                        mixer.music.play(-1)
                        new_music='play'
                    elif music3Rect.collidepoint((mx,my)):
                        settingMusic(screen)
                        draw.rect(screen,(255,0,0),music3Rect,3)
                        mixer.music.load('加州旅馆.mp3')
                        mixer.music.play(-1)
                        new_music='play'
                    elif music4Rect.collidepoint((mx,my)):
                        settingMusic(screen)
                        draw.rect(screen,(255,0,0),music4Rect,3)
                        mixer.music.load('天空之城.mp3')
                        mixer.music.play(-1)
                        new_music='play'
                        
                    if volumeRect.collidepoint((mx,my)):    
                        screen.set_clip(volumeRect.x+5,volumeRect.y+5,volumeRect.width-10,volumeRect.height-10)
                        volumeBar(screen)
                        draw.rect(screen,(100,255,100),(355,305,mx-355,15))
                        new_volume=round((100/350*(mx-350)/100),2)  #finds the ratio of the mouse position and the length of the volume rect
                        mixer.music.set_volume(new_volume)  #new volume is set
                        screen.set_clip(None)
                        
                    if exitRect.collidepoint((mx,my)):  #if user exits, this function stops
                        run=False
                        return canvas_colour_change,(R,G,B),new_eraser_frame,BackG,new_music,new_volume
                    
                    if cancelRect.collidepoint((mx,my)):    #if user exits by cancelling, everything will be changed back to what it was when it began, then the function stops
                        new_music=music
                        new_volume=volume
                        canvas_colour_change=False
                        new_canvas_colour=canvas_colour
                        R,G,B=canvas_colour
                        new_eraser_frame=eraser_frame
                        low_Rcolour=False
                        low_Gcolour=False
                        low_Bcolour=False
                        BackG=background_picture
                        mixer.music.set_volume(new_volume)
                        run=False
                        return canvas_colour_change,(R,G,B),new_eraser_frame,BackG,new_music,new_volume

        
        draw.rect(screen,(R,G,B),(400,615,60,60))   #a sample of the colour that the user selected will be displayed to the user
        if mb[0]==1:                                
            if redRect.collidepoint((mx,my)):   
                screen.set_clip(redRect)
                R=mx-100
                canvas_colour_change=True
                if 102<mx<353:
                    screen.blit(red,(redRect.x,redRect.y))
                    draw.rect(screen,(75,75,75),(mx-2,575,5,20))    #if the user clicks on the colour rects, a grey bar will show up at the place that is pressed
                if R<56:
                    low_Rcolour=True
                else:
                    low_Rcolour=False
            elif greenRect.collidepoint((mx,my)):
                screen.set_clip(greenRect)
                G=mx-100
                canvas_colour_change=True
                if 102<mx<353:
                    screen.blit(green,(greenRect.x,greenRect.y))
                    draw.rect(screen,(75,75,75),(mx-2,615,5,20))
                if G<56:
                    low_Gcolour=True
                else:
                    low_Gcolour=False
            elif blueRect.collidepoint((mx,my)):
                screen.set_clip(blueRect)
                B=mx-100
                canvas_colour_change=True
                if 102<mx<353:
                    screen.blit(blue,(blueRect.x,blueRect.y))
                    draw.rect(screen,(75,75,75),(mx-2,655,5,20)) 
                if B<56:
                    low_Bcolour=True
                else:
                    low_Bcolour=False
            screen.set_clip(None)
            if low_Rcolour and low_Gcolour and low_Bcolour:
                new_eraser_frame=white
            else:
                new_eraser_frame=black
            
        display.flip()

