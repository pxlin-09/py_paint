from pygame import *
from glob import *

''' -------------------------------------------------------------
    getName
    -------------------------------------------------------------
    Because pygame likes to crash you can copy and paste my getName
    function into your program and use it, free of charge.  You
    may want to change the size of the rectange, it's location, the
    font, and the colour so that it matches your program.
    ------------------------------------------------------------- '''
def getName(screen,showFiles):
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(375,300,300,25) # make changes here.

    if showFiles:
        pics = [' '*15+'enter your file name (png files only)',' '*21+'<right click to exit>']  #message to user
        n = len(pics)
        choiceArea = Rect(textArea.x,textArea.y-textArea.height-25,textArea.width,n*textArea.height+25)
        draw.rect(screen,(255,255,220),choiceArea)        # draw the text window and the text.
                # draw the text window and the text.
        for i in range(n):
            txtPic = arialFont.render(pics[i], True, (0,111,0))   #
            screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))

    cursorShow = 0
    myclock = time.Clock()
    typing = True
    while typing:
        mb2=mouse.get_pressed()
        if mb2[2]==1:
            ans=''
            break
        cursorShow += 1
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : # your main loop will stop looping until user hits enter
                    typing = False
                elif e.key < 256:
                    TxtSize=arialFont.render(ans+e.unicode, True, (0,0,0))
                    Size=TxtSize.get_width()
                    if Size<290:
                        ans += e.unicode       # add character to ans
                        
        txtPic = arialFont.render(ans, True, (0,0,0))   

        draw.rect(screen,(110,110,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,1)            
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        if cursorShow // 50 % 2 == 1:
            cx = textArea.x+txtPic.get_width()+3
            cy = textArea.y+3
            draw.rect(screen,(255,0,0),(cx,cy,2,textArea.height-6))
        myclock.tick(100)
        display.flip()
        draw.rect(screen,(0,0,0),choiceArea,3)
        
    screen.blit(back,(0,0))
    return ans
       
