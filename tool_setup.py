#tool setup
#tool setup

from random import*
from pygame import*

canvasRect=Rect(250,100,550,400)
                                   
colours=[(0,0,0)]
eraserSize=[]
shades=5

redoPic=image.load('redo.png')
redoPic=transform.scale(redoPic,(100,60))
undoPic=image.load('undo.png')
undoPic=transform.scale(undoPic,(100,60))
mirror_tool=image.load('mirror.jpg')
mirror_tool=transform.scale(mirror_tool,(82,68))

#stamps:
stamp0=image.load('leaf.png')
stamp1=image.load('water.png')
stamp2=image.load('sun.png')
stamp3=image.load('tree.png')
stamp4=image.load('maple.png')
stamp5=image.load('corn.png')
stamp6=image.load('snow.png')
stamp7=image.load('snowman.png')

for i in range(shades):     #gets the shades of 9 different colours that will be used in the pencil tool
    mix=255/shades+i*255/shades
    colours.append((0,0,mix)) #blue
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((0,mix,mix)) #neon green
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((0,mix,0))   #green
for i in range (shades):
    mix=255/shades+i*255/shades
    colours.append((255,mix/2,i)) #orange  
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((mix,mix,0)) #yellow
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((mix,0,0))   #red
for i in range (shades):
    mix=255/shades+i*255/shades
    colours.append((200+i*10,i*35,120+i*10)) #pink
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((mix,0,mix)) #purple
for i in range(shades):
    mix=255/shades+i*255/shades
    colours.append((mix,mix,mix)) #grey
    
for i in range(5):
    eraserSize.append(i*4+4)

lenC=len(colours)


def pencil(screen):#draw the tools when "pencil" tool is selected 
    for i in range(lenC):
        draw.rect(screen,colours[i],(250+i*int(550/lenC),520,550/lenC,70))
        draw.rect(screen,0,(250+i*int(550/lenC),520,550/lenC,70),1)


def spray(screen,colour,diameter,mx,my):   #spray paint 

    if diameter<10:
        diameter=10
    pre_x,pre_y=mx,my
    drip_pos=[]
    draw.circle(screen,colour,(mx,my),int(diameter/2))  #draws a circle at the click point
    for i in range (diameter):  
                drip_pos.append([mx-int(diameter/2)+i,int(((diameter/2)**2-(mx-diameter/2+i-mx)**2)**(1/2)+my-3)])  #gets the positions of the lower arc of the circle
    while True:
        for e in event.get():
            if e.type==MOUSEBUTTONUP:
                return mouse.get_pos()
        x,y=mouse.get_pos()
        
        if pre_x!=x or pre_y!=y:        #if mouse moved, the points are rechosen
            draw.line(screen,colour,(pre_x,pre_y),(x,y),diameter)
            drip_pos=[]
            draw.circle(screen,colour,(x,y),int(diameter/2))
            
            for i in range (diameter):
                drip_pos.append([x-int(diameter/2)+i,int(((diameter/2)**2-(x-diameter/2+i-x)**2)**(1/2)+y-3)])  #makes a list of random points from the edge of circle to start dripping 
        drip_point=choice(drip_pos) #choses a random point from list
        pre_x,pre_y=x,y
        if drip_point[1]<500:   #500 is the size of the drawing area
            if diameter<10:
                time.wait(10)
            else:
                time.wait(0)                                                                                
            draw.line(screen,colour,(drip_point[0],drip_point[1]),(drip_point[0],drip_point[1]+3),1)       #draw lines to make the spray have a dripping downwards motion
            drip_point[1]+=3    #the lines drawn each has a length of 3, can also be changed to adjust speed of the drip
        display.flip()



def eraser(screen):       #draw the rects and pictures when "eraser" is selected       
    for i in range(5):
        draw.rect(screen,(255,255,255),(250+i*110,520,110,70))
        draw.rect(screen,0,(250+i*110,520,110,70),1)
        draw.circle(screen,0,(305+i*110,555),i*4+4,1)


    
def shape(screen):                #draw the rects and pictures when "shape" is selected
    for i in range(6):
        draw.rect(screen,(255,255,255),(250+i*int(550/6),520,550/6,70))
        draw.rect(screen,0,(250+i*int(550/6),520,550/6,70),1)
    draw.line(screen,0,(255,580),(335,530))
    draw.rect(screen,0,(351,530,70,50),1)
    draw.ellipse(screen,0,(443 ,530,70,50),1)
    for i in range(5):
        draw.line(screen,0,(530+i*15,555),(540+i*15,555),3)
    for i in range(4):
        draw.line(screen,0,(621+i*25,555),(626+i*25,555),3)
    for i in range(3):
        draw.circle(screen,0,(636+25*i,555),3)
    screen.blit(mirror_tool,(709,521))



def stamps(screen):     #draw the rects and pictures when "stamp" is selected
    for i in range(8):
        draw.rect(screen,(255,255,255),(250+i*int(550/8),520,int(550/8),70))
        draw.rect(screen,0,(250+i*int(550/8),520,550/8,70),1)
        image=eval('stamp'+str(i))
        image=transform.scale(image,(int(550/8)-2,70-2))
        screen.blit(image,(250+i*int(550/8),519))


                    
def undo_redo_setup(screen):    #draw the rects and pictures when undo/redo is selected
    for i in range(2):
        draw.rect(screen,(255,255,255),(250+i*int(550/2),520,550/2,70))
        draw.rect(screen,0,(250+i*int(550/2),520,550/2,70),1)
    screen.blit(undoPic,(350,525))
    screen.blit(redoPic,(600,525))




def undo_redo(screen,undo_list):
        if len(undo_list)<20:
            undo_list.append(screen.subsurface(canvasRect).copy())
        else:
            del undo_list[0]
            undo_list.append(screen.subsurface(canvasRect).copy())
        return


    
def undo(screen,undo_list,redo_list):
    if len(undo_list)>0:
        pic=(undo_list).pop()
        if len(redo_list)<21:
            redo_list.append(screen.subsurface(canvasRect).copy())
            screen.blit(pic,(250,100))
        else:
            del redo_list[0]
            redo_list.append(screen.subsurface(canvasRect).copy())
            screen.blit(pic,(250,100))
        return



def redo(screen,undo_list,redo_list):
    if len(redo_list)>0:
        pic=(redo_list).pop()
        if len(undo_list)<20:
            undo_list.append(screen.subsurface(canvasRect).copy())
            screen.blit(pic,(250,100))
        else:
            del undo_list[0]
            undo_list.append(screen.subsurface(canvasRect).copy())
            screen.blit(pic,(250,100))
    

