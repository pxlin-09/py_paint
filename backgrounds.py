#background settup

from random import*

spring=[]   #themes
summer=[]
fall=[]
winter=[]
season_list=[]

for i in range(1,5):    #loads all the backgrounds for each theme
    spring.append('spring'+str(i)+'.jpg')
    summer.append('summer'+str(i)+'.jpg')
    fall.append('autumn'+str(i)+'.jpg')
    winter.append('winter'+str(i)+'.jpg')
    
def background(topic):  #randomly selects a picture from a theme and returns it
    if topic==1:
        season_list=spring
        season='spring'
        image=choice(season_list)
    elif topic==2:
        season_list=summer
        season='summer'
        image=choice(season_list)
    elif topic==3:
        season_list=fall
        season='fall'
        image=choice(season_list)
    else:
        season_list=winter
        season='winter'
        image=choice(season_list)
    return image,season    
    
    
    
        
