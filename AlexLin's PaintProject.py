#Header Comments
# individual features:

'''
-Spray paint
-double click to clear screen
-dash lines
-dash+dot line
-mirror pencil
-undo+redo
-thickness+colour display
-music+pause/play
-setting page:
    change background
    change music
    music volume
    change paint palet colour
screen saver

'''
# attention to detail
'''
-when the selected colour is white,the background for the display of colour will change to black
-draws a line to show that music is paused
-spray paint has a dripping effect
-each season had a song to it
-the background image is a random picture chosen from 16 differen images
-if user enters a invaild message when saving, an error message will pop up
-if user enters a non-existent image when loading, an error message will pop up
-eraser frame
'''

from pygame import *
from random import*
from math import*
from getname import *
from backgrounds import*
from setting_page import*
from tool_setup import*


screen = display.set_mode((1000,700))

display.set_caption("Season's Art Class")

font.init()                                 

comicFont = font.SysFont("Comic Sans MS", 20)

pre_x,pre_y=0,0




undo_list=[]
redo_list=[]
white=(255,255,255)
music='play'
size=0 #eraser size
LineSize=3 #distance between dash lines in shape mode
sleepMode=0
colour_change=0
pressed=0   # a flag set for the scroller
UndoScreen=[]
canvasColour=(255,255,255)
eraser_frame=0
DoubleClick=0
running =True
tick=0
idle=0
mx2,my2=0,0
screen_saver=0
thickness=1
tool=0
tool='pencil'   #defaulted to pencil tool
c=colours[0]    #and the colour black (c is set as current colour)
topic=randint(1,4)

background_picture,season=background(topic)

BackGround=image.load(background_picture)

BackGround=transform.scale(BackGround,(1000,700))

init()
if season=='spring':
    mixer.music.load('KissTheRain.mp3')
if season=='summer':
    mixer.music.load('Cotan.mp3')
if season=='fall':
    mixer.music.load('加州旅馆.mp3')
if season=='winter':
    mixer.music.load('天空之城.mp3')

mixer.music.play(-1)
mixer.music.set_volume(0.5)
volume=0.5


canvasRect=Rect(250,100,550,400)    #the place where the user can draw on


#load pictures-------------------------------------------------------------------------

#add '1' after each picture just to distinguish it from other variables that might be used later on
#the picture for each tool is loaded then blited
pencil_1=image.load('pencils.jpg')              
pencil_1=transform.scale(pencil_1,(108,68))
eraser_1=image.load('eraser.jpg')
eraser_1=transform.scale(eraser_1,(108,68))
shapes_1=image.load('shapes.jpg')
shapes_1=transform.scale(shapes_1,(108,68))
stamps_1=image.load('stamp.png')
stamps_1=transform.scale(stamps_1,(108,68))
undoRedo_1=image.load('undoRedo.png')
undoRedo_1=transform.scale(undoRedo_1,(108,68))
music_icon=image.load('music.png')
music_icon=transform.scale(music_icon,(73,73))
save_icon=image.load('save.png')
save_icon=transform.scale(save_icon,(71,71))
setting_icon=image.load('settings.png')
setting_icon=transform.scale(setting_icon,(71,71))
load_icon=image.load('load.png')
load_icon=transform.scale(load_icon,(71,71))
#-------------------------------------------------------------------------------------------------

typing=0
loadPic=0

def tools():        #draw the layout
    screen.blit(BackGround,(0,0))
    draw.rect(screen,canvasColour,canvasRect)
    for i in range(5):  #these are the main tools for drawing
        draw.rect(screen,(255,255,255),(250+i*110,10,110,70))
        
    settingsRect=Rect(850,100,73,73)    #these are made for the user to chose what is suitable for him or herself
    musicRect=Rect(850,209,73,73)
    saveRect=Rect(850,318,73,73)
    loadRect=Rect(850,427,73,73)
    
    draw.rect(screen,(255,255,255),settingsRect)
    draw.rect(screen,(0,0,0),settingsRect,1)
    draw.rect(screen,(255,255,255),musicRect)
    draw.rect(screen,(0,0,0),musicRect,1)
    draw.rect(screen,(255,255,255),saveRect)
    draw.rect(screen,(20,0,0),saveRect,1)
    draw.rect(screen,(255,255,255),loadRect)
    draw.rect(screen,(0,0,0),loadRect,1)
    
    screen.blit(pencil_1,(251,11))
    screen.blit(eraser_1,(361,11))
    screen.blit(shapes_1,(471,11))
    screen.blit(stamps_1,(581,11))
    screen.blit(undoRedo_1,(691,11))
    screen.blit(music_icon,(850,209))
    screen.blit(save_icon,(851,319))
    screen.blit(setting_icon,(851,101))
    screen.blit(load_icon,(851,428))
    return settingsRect,musicRect,saveRect,loadRect,music_icon  



        

def switchMode(mode,current_colour):       #refreshes the display of tools when a new tool is selected 
            DrawBox=screen.subsurface(canvasRect).copy()
            tools()
            screen.blit(DrawBox,(250,100))
            mode(screen)
            thickness_display(c)
            if music=='stop':
                draw.line(screen,(255,0,0),(855,214),(918,277),5)
                

def materials(box_length,function,colour,thick):                #choice of selection for each tool
            selection=0
            pre_x,pre_y=0,0
            for x in range(250,801-int(box_length),int(box_length)):
                    if mx in range(x,x+int(box_length)) and my in range(520,590):
                        selection=int((x-250)/int(box_length))  #if the mouse is click, this part of the function determines which rect in the bottom did the mouse click on
                        if mx!=pre_x or my!=pre_y:
                            function(screen)    
                            pre_x,pre_y=mx,my
                            draw.rect(screen,colour,(x+int(thick/2),520+int(thick/2),box_length-thick,70-thick),thick)  #highlights the chosen rect everytime a new rect is clicked
            return selection


def thickness_display_setup(screen,thickness,inside_colour,outline_colour,current_colour):  #this function allows the user to see the thickess level he is currently at
    thicknessRect=(815,500,20,-400) #the background of the thickness bar
    thicknessRect2=(820,495,10,-int(390/30*thickness))  #this rectangle will change its height everytime the user adjusts the thickness using the scroller
    draw.rect(screen,inside_colour,thicknessRect)
    draw.rect(screen,outline_colour,thicknessRect,2)
    draw.rect(screen,c,thicknessRect2)
    
def thickness_display(c):   #since the thickness bar is drawn with the colour the user chose, the background for the thickness bar will change to black if the selected colour is white
    if c==(255,255,255):
        thickness_display_setup(screen,thickness,(0,0,0),(255,255,255),c) 
    else:
        thickness_display_setup(screen,thickness,(255,255,255),(0,0,0),c)
    
settingsRect,musicRect,saveRect,loadRect,music_icon=tools()
pencil(screen) #pencil is automatically selected for user at the beginning
c=colours[0]    #colours begin with black
thickness_display(c)


while running:
    SingleClick=False
    LeftButtonPressed=False
    RightButtonPressed=False
    ScrollerPressed=False
    ButtonPressed=False
    pressed=0
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            running = False
        
        if e.type==MOUSEBUTTONUP and e.button==1:
           tick=time.get_ticks()    #gets the time of the first click
           DoubleClick=0    
        if e.type==MOUSEBUTTONDOWN and e.button==1:
            if 250<mx<800 and 100<my<500:
                start_x,start_y=mx,my
            if time.get_ticks()-tick<100:   #if the user clicks again in a short time period, this counts as a doubleclick
                DoubleClick=1
                
                #print("new tick="+str(time.get_ticks()))
                #print("Double clicked")
            else:
                DoubleClick=0
                
        if e.type==MOUSEBUTTONDOWN and e.button==3:
                start_x,start_y=mx,my
        if e.type==MOUSEBUTTONDOWN and e.button==4:
            if thickness<30:    #maximum thickness is 30
                thickness+=1
            if LineSize<18:
                LineSize+=0.4
            thickness_display(c)
            pressed=1   #sets a flag if the roller is rolled
        if e.type==MOUSEBUTTONDOWN and e.button==5:
            if thickness>1:     #minimum thickness is 1
                thickness-=1
            if LineSize>3:
                LineSize-=0.4
            thickness_display(c)
            pressed=1   #sets a flag if the roller is rolled
        if e.type==MOUSEBUTTONDOWN:
            ButtonPressed=True #used for screen saver
            if 250<mx<800 and 100<my<500 and tool!='undo/redo':
                if e.button==1:
                    LeftButtonPressed=True  #if user left clicked
                elif e.button==2:
                    ScrollerPressed=True #if user pressed the scroller
                elif e.button==3:
                    RightButtonPressed=True #if user right clicked            
        if e.type==MOUSEBUTTONUP:
            SingleClick=True

        
        

    if mx2!=mx or my2!=my or ButtonPressed or ScrollerPressed:    #if mouse is moving or pressed
        idle=time.get_ticks()   #the last time when the mouse moved
        mx2,my2=mx,my
        if screen_saver!=0:
            screen.blit(screen_saver,(0,0))
            screen_saver=0
        drawing=True    #if screen saver is not in use, the user is in drawing mode
    elif mx2==mx and my2==my and pressed==0:    #if mouse does not move or is not pressed
        if time.get_ticks()-idle>4000:  #the mouse has not been moving for a certain time, the screen saver will pop up
            if screen_saver==0:
                time.wait(1000)
                screen_saver=screen.copy()
                screen.blit(BackGround,(0,0))
            drawing=False   #if screen saver is in use, the user is not in drawing mode
                

        
    
        
        
    if 251<mx<360 and 10<my<80: #if a feature is selected, the rect will be highlighted and the tool would switch to that feature
        if SingleClick:
            tool='pencil'
            switchMode(pencil,c)    #draws the layout of the pencil mode
            draw.rect(screen,(255,0,0),(251,11,108,68),3)   #outlines the selected rect
            
            
    elif 361<mx<470 and 10<my<80:
        if SingleClick:
            tool='eraser'
            switchMode(eraser,c)    #draws the layout of the eraser mode
            draw.rect(screen,(255,0,0),(360,11,110,68),3)   #outlines the selected rect
            eraser_colour=canvasColour  
            size=4  #the smallest eraser size
            drawBox=screen.subsurface(canvasRect).copy()
        if DoubleClick==1:  #clears the screen if doubleclick the eraser icon
                undo_redo(screen,undo_list)
                redo_list=[]
                draw.rect(screen,canvasColour,canvasRect)
                DoubleClick=0
                
        
        
    elif 471<mx<580 and 10<my<80:
        if SingleClick:
            tool='shape'
            switchMode(shape,c)     #draws the layout of the shape mode
            draw.rect(screen,(255,0,0),(470,11,110,68),3)
            DrawShape=0     #automatially selects the first tool for the user
            pic=screen.copy()

    elif 581<mx<690 and 10<my<80:
        if SingleClick:
            tool='stamps'
            draw.rect(screen,(255,0,0),(581,11,110,68),3)
            switchMode(stamps,c)    #draws the layout of the stamp mode
            draw.rect(screen,(255,0,0),(580,11,110,68),3)
            new_stamp=stamp0    #automatically select the first stamp for user
            drawBox=screen.subsurface(canvasRect).copy()
    elif 691<mx<800 and 10<my<80:
        if SingleClick:
            tool='undo/redo'
            switchMode(undo_redo_setup,c)   #draws the layout of undo redo
            draw.rect(screen,(255,0,0),(691,11,110,68),3)   #highlights the rect
            
    elif SingleClick and settingsRect.collidepoint((mx,my)):
        tool='setting'
        drawBox=screen.subsurface(canvasRect).copy()
        tools() #this function empties the canvas
        draw.rect(screen,(255,0,0),(settingsRect.x+1,settingsRect.y+1,settingsRect.width-2,settingsRect.height-2),3) #highlights the selected rect
        
    elif SingleClick and musicRect.collidepoint((mx,my)):
        if music=='play':
            draw.line(screen,(255,0,0),(855,214),(918,277),5) #draws a line to indicate there is no music playing
            music='stop'
            mixer.music.pause()
        else:
            draw.rect(screen,(255,255,255),musicRect)
            screen.blit(music_icon,(850,209))
            music='play'
            mixer.music.unpause()
    elif SingleClick and saveRect.collidepoint((mx,my)):
            tool='save'
            drawBox=screen.subsurface(canvasRect).copy()
            tools() #this function empties the canvas
            screen.blit(drawBox,(250,100))
            if music=='stop':
                draw.line(screen,(255,0,0),(855,214),(918,277),5)
            draw.rect(screen,(255,0,0),(saveRect.x+1,saveRect.y+1,saveRect.width-2,saveRect.height-2),3)
            typing=True
    elif SingleClick and loadRect.collidepoint((mx,my)):
        tool='load'
        drawBox=screen.subsurface(canvasRect).copy()
        tools() #this function empties the canvas
        screen.blit(drawBox,(canvasRect.x,canvasRect.y)) 
        if music=='stop':
                draw.line(screen,(255,0,0),(855,214),(918,277),5)
        draw.rect(screen,(255,0,0),(loadRect.x+1,loadRect.y+1,loadRect.width-2,loadRect.height-2),3)        
        typing=True
        selected=False  #picture will not be selected if user renters load mode         

    
# pencil mode--------------------------------------------------------------------------------------------------------    

    if tool=='pencil':  
        if 249<=mx<=799 and 521<=my<=589:
            if SingleClick:
                c=colours[materials(550/lenC,pencil,white,1)]   #determines which colour did the user chose
                thickness_display(c)
        
        
        elif 250<mx<800 and 100<my<500: #if the mouse is in the canvas:
            if LeftButtonPressed or RightButtonPressed:
                undo_redo(screen,undo_list)
                redo_list=[]
            if mb[0]==1:
                if mx!=pre_x or mx!=pre_y:    
                    screen.set_clip(canvasRect) #can only draw in canvas
                    draw.circle(screen,c,(pre_x,pre_y),int(thickness/2))  #draws circles at where the user pressed
                    draw.line(screen,c,(pre_x,pre_y),(mx,my),thickness)   #lines are also drawn to cover the spaces that the circles cannot cover
                screen.set_clip(None)
            elif mb[2]==1:
                    if thickness<10:    #the spray paint will not look good at low thickness
                        thickness=10
                        thickness_display(c)
                    screen.set_clip(canvasRect)
                    mx,my=spray(screen,c,thickness,mx,my)
                    screen.set_clip(None)
        
        pre_x,pre_y=mx,my       


# eraser mode--------------------------------------------------------------------------------

    elif tool=='eraser':
        if 249<=mx<=799 and 521<=my<=589:
            if SingleClick:
                size=eraserSize[materials(110,eraser,(255,0,0),4)]    #determines which size of the eraser did the user selects
                drawBox=screen.subsurface(canvasRect).copy()
                                
        if 250<mx<800 and 100<my<500:
            if  LeftButtonPressed:
                screen.blit(drawBox,(250,100))  #must blit once so the undo list will not catch the eraser frame
                undo_redo(screen,undo_list)
                redo_list=[]
            screen.set_clip(canvasRect) 
            if drawing:                        
                screen.blit(drawBox,(250,100))
                draw.circle(screen,eraser_frame,(mx,my),size-1,1)   #draws a frame of the eraser as the mouse moves around in the canvas
            if mb[0]==1:
                screen.blit(drawBox,(250,100))
                draw.circle(screen,eraser_colour,(pre_x,pre_y),size)  #circles and lines of the canvas colour is drawn if the mouse is clicked
                draw.line(screen,eraser_colour,(pre_x,pre_y),(mx,my),size*2) 
                drawBox=screen.subsurface(canvasRect).copy()
            screen.set_clip(None)
            
        else:
            if pre_x!=mx or pre_y!=my:
                screen.blit(drawBox,(250,100))
            
        pre_x,pre_y=mx,my  

         
# shape mode----------------------------------------------------------------

    elif tool=='shape':
        if 249<=mx<=799 and 521<=my<=589:
                if SingleClick:
                    DrawShape=materials(550/6,shape,(255,0,0),4)  #determines which kind of shapes does the user want to draw
                    
        if 250<mx<800 and 100<my<500:   #the undo screen will only append the canvas when a button that will draw something is clicked
            if DrawShape==0 or DrawShape==3 or DrawShape==4:
                if LeftButtonPressed==True:
                    undo_redo(screen,undo_list)
                    redo_list=[]
            elif DrawShape==1 or DrawShape==2:
                if LeftButtonPressed or RightButtonPressed:
                    undo_redo(screen,undo_list)
                    redo_list=[]
            elif DrawShape==5:
                if LeftButtonPressed or RightButtonPressed or ScrollerPressed:
                    undo_redo(screen,undo_list)
                    redo_list=[]

            screen.set_clip(canvasRect)
            if mb[0]==1 and mb[2]==0:
                        if DrawShape==0:
                            screen.blit(pic,(0,0))
                            draw.line(screen,c,(start_x,start_y),(mx,my),thickness) #draws a staight line from the click point to the mouse
                        elif DrawShape==1:
                            screen.blit(pic,(0,0))
                            rect_x,rect_y=mx-start_x,my-start_y
                            draw.rect(screen,c,(start_x,start_y,rect_x,rect_y),thickness)   #draws a rectangle from the click point to the mouse
                        elif DrawShape==2:
                            screen.blit(pic,(0,0))
                            length=mx-start_x
                            height=my-start_y
                            elrect=Rect(start_x,start_y,length,height)  #finds the rect for the ellispe
                            elrect.normalize()
                            if length<0:    #finds the absolute value of the length and height
                                length=0-length
                            if height<0:
                                height=0-height
                            if length>(thickness*2) and height>(thickness*2):   #once the length and height is greater than twice the thickness,a oval will be drawn
                                draw.ellipse(screen,c,elrect,thickness)
                        elif DrawShape==3:
                            screen.blit(pic,(0,0))
                            distance=(hypot((start_x-mx),(start_y-my)))/LineSize    #the distance from click point to mouse
                            if distance!=0:
                                delta_x=(mx-start_x)/distance   #finds the distance between the dash lines
                                delta_y=(my-start_y)/distance
                                x1,y1=start_x,start_y   #get a substitution for start_x, start_y because the value will of it will be used and changed later on 
                                for i in range(int(distance/(LineSize*2))):
                                    draw.line(screen,c,(int(x1),int(y1)),(int(x1+LineSize*delta_x),int(y1+LineSize*delta_y)),thickness) #draw the dashes
                                    x1+=2*LineSize*delta_x
                                    y1+=2*LineSize*delta_y
                        elif DrawShape==4:
                            screen.blit(pic,(0,0))
                            distance=(hypot((start_x-mx),(start_y-my)))/(LineSize*2)
                            if distance!=0:
                                half=int(LineSize/2)
                                delta_x=(mx-start_x)/distance
                                delta_y=(my-start_y)/distance
                                x1,y1=start_x,start_y
                                for i in range (int(distance/(LineSize*2))):
                                    draw.line(screen,c,(int(x1),int(y1)),(int(x1+LineSize*delta_x/2),int(y1+LineSize*delta_y/2)),thickness)
                                    draw.circle(screen,c,(int(x1+LineSize*delta_x*5/4),int(y1+LineSize*delta_y*5/4)),thickness)
                                    x1+=2*LineSize*delta_x
                                    y1+=2*LineSize*delta_y
                        elif DrawShape==5:
                            dis_pre_y=500-pre_y #finds the distance from the mouse to the edge of the canvas
                            dis_my=500-my
                            draw.line(screen,c,(pre_x,pre_y),(mx,my),thickness) #draw lines and circle when mouse is clicked
                            draw.circle(screen,c,(mx,my),int(thickness/2))
                            draw.line(screen,c,(pre_x,100+dis_pre_y),(mx,100+dis_my),thickness) #mirrored lines also drawn(horizontal)
                            draw.circle(screen,c,(mx,100+dis_my),int(thickness/2))
                                    
                       

            elif mb[2]==1 and mb[0]==0:           
                        if DrawShape==1:    #draws a filled rect
                            screen.blit(pic,(0,0))
                            rect_x,rect_y=mx-start_x,my-start_y
                            draw.rect(screen,c,(start_x,start_y,rect_x,rect_y))
                        elif DrawShape==2:  #draws a filled oval
                            screen.blit(pic,(0,0))
                            elrect=Rect(start_x,start_y,mx-start_x,my-start_y)
                            elrect.normalize()
                            draw.ellipse(screen,c,elrect)
                        elif DrawShape==5:
                            dis_pre_x=800-pre_x #finds distance from mouse to edge and draw mirrored lines(vertical)
                            dis_mx=800-mx
                            draw.line(screen,c,(pre_x,pre_y),(mx,my),thickness)
                            draw.circle(screen,c,(mx,my),int(thickness/2))
                            draw.line(screen,c,(250+dis_pre_x,pre_y),(250+dis_mx,my),thickness)
                            draw.circle(screen,c,(250+dis_mx,my),int(thickness/2))

            elif mb[1]==1:
                if DrawShape==5:    #finds distance from mouse to edge and draw mirrored lines(diagonal)
                    dis_pre_x=800-pre_x
                    dis_mx=800-mx
                    dis_pre_y=500-pre_y
                    dis_my=500-my
                    draw.line(screen,c,(pre_x,pre_y),(mx,my),thickness)
                    draw.circle(screen,c,(mx,my),int(thickness/2))
                    draw.line(screen,c,(250+dis_pre_x,100+dis_pre_y),(250+dis_mx,100+dis_my),thickness)
                    draw.circle(screen,c,(250+dis_mx,100+dis_my),int(thickness/2))
            elif mb[0]==0:
                    pic=screen.copy()
            screen.set_clip(None)     
        pre_x,pre_y=mx,my


# stamps--------------------------------------------------

    elif tool=='stamps':
        if 249<=mx<=799 and 521<=my<=589:
            if SingleClick:
                new_stamp=eval('stamp'+str(materials(550/8,stamps,(255,0,0),4)))  #determines which picture does the user want to use
        if 250<mx<800 and 100<my<500:
            
            if LeftButtonPressed:
                undo_redo(screen,undo_list)
                redo_list=[]     
            if mb[0]==1:    #once the user press the mouse in canvas, the picture will be drawn, size will vary as the thickness changes
                screen.set_clip(canvasRect)
                size_x=int(550/8)-2+thickness*2     #width and height of picture
                size_y=68+thickness*2
                new_stamp=transform.scale(new_stamp,(size_x,size_y))
                screen.blit(drawBox,(250,100))
                screen.blit(new_stamp,(mx-int(size_x/2),my-int(size_y/2))) #the middle of the picture will be located at the mouse
                screen.set_clip(None)
            if mb[0]==0:
                drawBox=screen.subsurface(canvasRect).copy()
                


# undo redo----------------------------------------------------

    elif tool=='undo/redo':
        if 249<=mx<=799 and 521<=my<=589:
            if SingleClick:
                UndoRedo=materials(550/2,undo_redo_setup,(255,0,0),3) #determines if the user clicked undo or redo
                if UndoRedo==0:
                    undo(screen,undo_list,redo_list)    #blits the last step
                if UndoRedo==1:
                    redo(screen,undo_list,redo_list)    #reverse undo

# save--------------------------------------------------------

    elif tool=='save':      #if the user enters a invalid destination to save, an error message will pop up, and the user would have to renter 
        try:
            txt = getName(screen,True)                      
            if txt!='':
                image.save(screen.subsurface(canvasRect),txt+'.png')
            tool=''#if user cancels save, tool will exit out of 'load' to prevent an infinite loop
        except:
            txtPic = comicFont.render('...destination not reconized...', True, (0,0,0),(255,0,0))  
            screen.blit(txtPic,(int(250+550/2-txtPic.get_width()/2),int(100+400/2-txtPic.get_height()/2)))                                        
            display.flip()
            time.wait(3000)
            screen.blit(drawBox,(250,100))

            
# setting------------------------------------------------------

    elif tool=='setting':
        canvas_colour_change,canvasColour,eraser_frame,background_picture,music,volume=setting_main(screen,BackGround,background,background_picture,canvasColour,eraser_frame,music,volume)
        BackGround=image.load(background_picture)
        BackGround=transform.scale(BackGround,(1000,700))
        tools() #layout will be drawn after the user exits the setting
        thickness_display(c)
        screen.blit(drawBox,(250,100))
        if canvas_colour_change:
            draw.rect(screen,canvasColour,canvasRect)   #redraws the canvas if the user selected a new background colour
        if music=='stop':
            draw.line(screen,(255,0,0),(855,214),(918,277),5)   #draws a line to indicate music is paused (if paused)
        
        tool=''


# load----------------------------------------------------------------------

    elif tool=='load':
        if typing:
            load_pic_Rect=Rect(250,520,80,80)   #this is where it will show the picture the user loaded
            draw.rect(screen,(255,255,255),load_pic_Rect)
            draw.rect(screen,0,load_pic_Rect,1)        
            try:
                txt=getName(screen,True)    #gets the file name the user will enter
                if txt!='':
                    loadPic=image.load(txt+'.png')
                    loadPic=transform.scale(loadPic,(78,78))
                    screen.blit(loadPic,(251,521))
                    typing=False
                else:
                    tool=''     #if user cancels load, tool will exit out of 'load' to prevent an infinite loop
                    typing=False
                    
            except:     #if the user enters a non-existent picture, an error message will pop up and the user will have to renter
                txtPic = comicFont.render('...The image name entered cannot be found...', True, (0,0,0),(255,0,0))  
                screen.blit(txtPic,(int(250+550/2-txtPic.get_width()/2),int(100+400/2-txtPic.get_height()/2)))  #shows the error message in the middle of the canvas
                display.flip()
                time.wait(3000)
                screen.blit(drawBox,(250,100))
                
        thickness_display(c)    #shows the thickness bar
        if loadPic!=0:
            if load_pic_Rect.collidepoint((mx,my)) and SingleClick: #if the user selects the loaded picture
                draw.rect(screen,(255,0,0),load_pic_Rect,3)
                selected=True
            if canvasRect.collidepoint((mx,my)) and selected:   #the user would then be able to draw the picture on the place desired
                if mb[0]==0:
                    pic=screen.copy()
                elif mb[0]==1:
                    screen.set_clip(canvasRect)
                    size_x=78+2*thickness
                    size_y=78+2*thickness
                    loadPic=transform.scale(loadPic,(size_x,size_y))    #the picture's scale will be different if the thickness level changes
                    screen.blit(pic,(0,0))
                    screen.blit(loadPic,(mx-size_x/2,my-size_y/2))
                    screen.set_clip(None)
    display.flip()
    
font.quit()
del comicFont



                        
quit()
    
    
