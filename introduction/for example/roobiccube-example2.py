from time import sleep

import random

import pygame
from pygame.locals import Rect
import sys

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("roobic cube")

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

block3=block.DIAMOND_BLOCK
screencolor1=(250,250,250)
block4=block.LAPIS_BLOCK
screencolor2=(200,200,200)
block5=block.EMERALD_BLOCK
screencolor3=(150,150,150)
block1=block.AMETHYST_BLOCK
screencolor4=(100,100,100)
block2=block.COPPER_BLOCK
screencolor5=(50,50,50)
block6=block.NETHERITE_BLOCK
screencolor6=(0,0,0)
block7=block.GOLD_BLOCK

pygame.init()

def gamestart1(mc=mc,x=-10,y=10,z=-10,block1=block1,block2=block2,block3=block3,block4=block4,block5=block5,block6=block6,frameblock=block7,screencolor1=screencolor1,screencolor2=screencolor2,screencolor3=screencolor3,screencolor4=screencolor4,screencolor5=screencolor5,screencolor6=screencolor6):

    mc.setBlocks(x,y,z,x+4,y-4,z+4,frameblock)
    mc.setBlocks(x+1,y-1,z+1,x+3,y-3,z+3,block.BARRIER)
    mc.setBlock(x+2,y-4,z-5,block.DIAMOND_BLOCK)
    mc.postToChat("Let's set roobic cube")

    #up surface
    #left,center,right
    #back   1,2,3
    #center 4,5,6
    #front  7,8,9
    #left surface
    #back,center,front
    #up     10,11,12
    #center 13,14,15
    #down   16,17,18
    #front surface
    #left,center,right
    #up     19,20,21
    #center 22,23,24
    #down   25,26,27
    #right surface
    #front,center,back
    #front  28,29,30
    #center 31,32,33
    #back   34,35,36
    #down surface
    #left,center,right
    #front  37,38,39
    #center 40,41,42
    #back   43,44,45
    #back surface
    #right,center,left
    #up     46,47,48
    #center 49,50,51
    #down   52,53,54

    sleep(0.01) 

    cornerblock1=[block1,block2,block3]
    random.shuffle(cornerblock1)
    cornerblock2=[block1,block3,block4]
    random.shuffle(cornerblock2)
    cornerblock3=[block1,block4,block5]
    random.shuffle(cornerblock3)
    cornerblock4=[block1,block5,block2]
    random.shuffle(cornerblock4)

    cornerblock5=[block6,block4,block3]
    random.shuffle(cornerblock5)
    cornerblock6=[block6,block3,block2]
    random.shuffle(cornerblock6)
    cornerblock7=[block6,block2,block5]
    random.shuffle(cornerblock7)
    cornerblock8=[block6,block5,block4]
    random.shuffle(cornerblock8)

    corners= [cornerblock1, cornerblock2, cornerblock3, cornerblock4, cornerblock5, cornerblock6, cornerblock7, cornerblock8]

    random.shuffle(corners)

    variables = {}
    for i in range(8):
        corner_name = f"corner_{i+1}"
        corner=corners[i]
        variables[corner_name] = [corner[0],corner[1],corner[2]] 
    
    sleep(0.01)

    color12=variables["corner_1"][0]
    color19=variables["corner_1"][1]
    color7=variables["corner_1"][2]
    color9=variables["corner_2"][0]
    color21=variables["corner_2"][1]
    color28=variables["corner_2"][2]
    color34=variables["corner_3"][0]
    color27=variables["corner_3"][1]
    color39=variables["corner_3"][2]
    color37=variables["corner_4"][0]
    color25=variables["corner_4"][1]
    color18=variables["corner_4"][2]

    color30=variables["corner_5"][0]
    color46=variables["corner_5"][1]
    color3=variables["corner_5"][2]
    color1=variables["corner_6"][0]
    color48=variables["corner_6"][1]
    color10=variables["corner_6"][2]
    color16=variables["corner_7"][0]
    color54=variables["corner_7"][1]
    color43=variables["corner_7"][2]
    color45=variables["corner_8"][0]
    color52=variables["corner_8"][1]
    color36=variables["corner_8"][2]

    sleep(0.01) 

    lineblock1=[block1,block2]
    random.shuffle(lineblock1)
    lineblock2=[block1,block3]
    random.shuffle(lineblock2)
    lineblock3=[block1,block4]
    random.shuffle(lineblock3)
    lineblock4=[block1,block5]
    random.shuffle(lineblock4)

    lineblock5=[block2,block3]
    random.shuffle(lineblock5)
    lineblock6=[block3,block4]
    random.shuffle(lineblock6)
    lineblock7=[block4,block5]
    random.shuffle(lineblock7)
    lineblock8=[block5,block2]
    random.shuffle(lineblock8)
    
    lineblock9=[block6,block4]
    random.shuffle(lineblock9)
    lineblock10=[block6,block3]
    random.shuffle(lineblock10)
    lineblock11=[block6,block2]
    random.shuffle(lineblock11)
    lineblock12=[block6,block5]
    random.shuffle(lineblock12)

    lines= [lineblock1, lineblock2, lineblock3, lineblock4, lineblock5, lineblock6, lineblock7, lineblock8, lineblock9, lineblock10, lineblock11, lineblock12]

    random.shuffle(lines)

    variables = {}
    for i in range(12):
        line_name = f"line_{i+1}"
        line=lines[i]
        variables[line_name] = [line[0],line[1]] 

    sleep(0.01)

    color20=variables["line_1"][0]
    color8=variables["line_1"][1]
    color24=variables["line_2"][0]
    color31=variables["line_2"][1]
    color26=variables["line_3"][0]
    color38=variables["line_3"][1]
    color22=variables["line_4"][0]
    color15=variables["line_4"][1]

    color4=variables["line_5"][0]
    color11=variables["line_5"][1]
    color29=variables["line_6"][0]
    color6=variables["line_6"][1]
    color42=variables["line_7"][0]
    color35=variables["line_7"][1]
    color17=variables["line_8"][0]
    color40=variables["line_8"][1]

    color47=variables["line_9"][0]
    color2=variables["line_9"][1]
    color51=variables["line_10"][0]
    color13=variables["line_10"][1]
    color53=variables["line_11"][0]
    color44=variables["line_11"][1]
    color49=variables["line_12"][0]
    color33=variables["line_12"][1]

    sleep(0.01) 
    
    surfacecolors= [block1, block2, block3, block4, block5, block6]

    random.shuffle(surfacecolors)

    variables = {}
    for i in range(6):
        surface_name = f"surface_{i+1}"
        variables[surface_name] = surfacecolors[i]

    color5=variables["surface_1"]
    color14=variables["surface_2"]
    color23=variables["surface_3"]
    color32=variables["surface_4"]
    color41=variables["surface_5"]
    color50=variables["surface_6"]

    sleep(0.01) 

    def is_inside_polygon(mouse_pos, polygon_points):
        if len(polygon_points) < 3: return False
        p = pygame.math.Vector2(mouse_pos)
        signs = []
        for i in range(len(polygon_points)):
            p1 = pygame.math.Vector2(polygon_points[i])
            p2 = pygame.math.Vector2(polygon_points[(i + 1) % len(polygon_points)])
            cross = (p2 - p1).cross(p - p1)
            if cross > 0: signs.append(1)
            elif cross < 0: signs.append(-1)
        return not (1 in signs and -1 in signs)      

    while True:
        screen.fill((255, 255, 255))

        triangle1 = [(180, 80), (220, 10), (260, 80)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle1)
        triangle2 = [(280, 80), (320, 10), (360, 80)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle2)
        triangle3 = [(380, 80), (420, 10), (460, 80)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle3)

        triangle4 = [(160, 100), (90, 140), (160, 180)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle4)
        triangle5 = [(160, 200), (90, 240), (160, 280)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle5)
        triangle6 = [(160, 300), (90, 340), (160, 380)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle6)

        triangle7 = [(180, 400), (220, 470), (260, 400)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle7)
        triangle8 = [(280, 400), (320, 470), (360, 400)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle8)
        triangle9 = [(380, 400), (420, 470), (460, 400)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle9)

        triangle10 = [(480, 100), (550, 140), (480, 180)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle10)
        triangle11 = [(480, 200), (550, 240), (480, 280)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle11)
        triangle12 = [(480, 300), (550, 340), (480, 380)]
        pygame.draw.polygon(screen, (0, 0, 0), triangle12)

        sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
            
                if is_inside_polygon(mouse_pos, triangle1):
                    mc.postToChat("turn up at left column")
                    nc1=color19
                    nc4=color22
                    nc7=color25
                    nc19=color37
                    nc22=color40
                    nc25=color43
                    nc37=color54
                    nc40=color51
                    nc43=color48
                    nc54=color1
                    nc51=color4
                    nc48=color7

                    nc10=color12
                    nc11=color15
                    nc12=color18
                    nc15=color17
                    nc18=color16
                    nc17=color13
                    nc16=color10
                    nc13=color11

                    sleep(0.01)

                    color1=nc1
                    color4=nc4
                    color7=nc7
                    color19=nc19
                    color22=nc22
                    color25=nc25
                    color37=nc37
                    color40=nc40
                    color43=nc43
                    color54=nc54
                    color51=nc51
                    color48=nc48

                    color10=nc10
                    color11=nc11
                    color12=nc12
                    color15=nc15
                    color18=nc18
                    color17=nc17
                    color16=nc16
                    color13=nc13

                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle2):
                    mc.postToChat("turn up at center column")
                    nc2=color20
                    nc5=color23
                    nc8=color26
                    nc20=color38 
                    nc23=color41
                    nc26=color44
                    nc38=color53
                    nc41=color50
                    nc44=color47
                    nc53=color2
                    nc50=color5
                    nc47=color8

                    sleep(0.01)

                    color2=nc2
                    color5=nc5
                    color8=nc8
                    color20=nc20
                    color23=nc23
                    color26=nc26
                    color38=nc38
                    color41=nc41
                    color44=nc44
                    color53=nc53
                    color50=nc50
                    color47=nc47
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle3):
                    mc.postToChat("turn up at right column")
                    nc3=color21
                    nc6=color24
                    nc9=color27
                    nc21=color39
                    nc24=color42
                    nc27=color45
                    nc39=color52
                    nc42=color49
                    nc45=color46
                    nc52=color3
                    nc49=color6
                    nc46=color9

                    nc28=color34
                    nc31=color35
                    nc34=color36
                    nc35=color33
                    nc36=color30
                    nc33=color29
                    nc30=color28
                    nc29=color31

                    sleep(0.01)

                    color3=nc3
                    color6=nc6
                    color9=nc9
                    color21=nc21
                    color24=nc24
                    color27=nc27
                    color39=nc39
                    color42=nc42
                    color45=nc45
                    color52=nc52
                    color49=nc49
                    color46=nc46

                    color28=nc28
                    color31=nc31
                    color34=nc34
                    color35=nc35
                    color36=nc36
                    color33=nc33
                    color30=nc30
                    color29=nc29

                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle4):
                    mc.postToChat("turn left at up column")
                    nc10=color19
                    nc11=color20
                    nc12=color21
                    nc19=color28
                    nc20=color29
                    nc21=color30
                    nc28=color46
                    nc29=color47
                    nc30=color48
                    nc46=color10
                    nc47=color10
                    nc48=color11

                    nc1=color7
                    nc4=color8
                    nc7=color9
                    nc8=color6
                    nc9=color3
                    nc6=color2
                    nc3=color1
                    nc2=color4

                    sleep(0.01)

                    color10=nc10
                    color11=nc11
                    color12=nc12
                    color19=nc19
                    color20=nc20
                    color21=nc21
                    color28=nc28
                    color29=nc29
                    color30=nc30
                    color46=nc46
                    color47=nc47
                    color48=nc48

                    color1=nc1
                    color4=nc4
                    color7=nc7
                    color8=nc8
                    color9=nc9
                    color6=nc6
                    color3=nc3
                    color2=nc2

                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle5):
                    mc.postToChat("turn left at center column")
                    nc13=color22
                    nc14=color23
                    nc15=color24
                    nc22=color31
                    nc23=color32
                    nc24=color33
                    nc31=color49
                    nc32=color50
                    nc33=color51
                    nc49=color13
                    nc50=color14
                    nc51=color15

                    sleep(0.01)

                    color13=nc13
                    color14=nc14
                    color15=nc15
                    color22=nc22
                    color23=nc23
                    color24=nc24
                    color31=nc31
                    color32=nc32
                    color33=nc33
                    color49=nc49
                    color50=nc50
                    color51=nc51
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle6):
                    mc.postToChat("turn left at down column")
                    nc16=color25
                    nc17=color26
                    nc18=color27
                    nc25=color34
                    nc26=color35
                    nc27=color36
                    nc34=color52
                    nc35=color53
                    nc36=color54
                    nc52=color16
                    nc53=color17
                    nc54=color18

                    nc37=color39
                    nc38=color42
                    nc39=color45
                    nc42=color44
                    nc45=color43
                    nc44=color40
                    nc43=color37
                    nc40=color38

                    sleep(0.01)

                    color16=nc16
                    color17=nc17
                    color18=nc18
                    color25=nc25
                    color26=nc26
                    color27=nc27
                    color34=nc34
                    color35=nc35
                    color36=nc36
                    color52=nc52
                    color53=nc53
                    color54=nc54

                    color37=nc37
                    color38=nc38
                    color39=nc39
                    color42=nc42
                    color45=nc45
                    color44=nc44
                    color43=nc43
                    color40=nc40
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle7):
                    mc.postToChat("turn down at left column")
                    nc1=color54
                    nc4=color51
                    nc7=color48
                    nc19=color1
                    nc22=color4
                    nc25=color7
                    nc37=color19
                    nc40=color22
                    nc43=color25
                    nc54=color37
                    nc51=color40
                    nc48=color43

                    nc10=color16
                    nc11=color13
                    nc12=color17
                    nc15=color11
                    nc18=color12
                    nc17=color15
                    nc16=color18
                    nc13=color17
            
                    sleep(0.01)
                    color1=nc1
                    color4=nc4
                    color7=nc7
                    color19=nc19
                    color22=nc22
                    color25=nc25
                    color37=nc37
                    color40=nc40
                    color43=nc43
                    color54=nc54
                    color51=nc51
                    color48=nc48

                    color10=nc10
                    color11=nc11
                    color12=nc12
                    color15=nc15
                    color18=nc18
                    color17=nc17
                    color16=nc16
                    color13=nc13
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle8):
                    mc.postToChat("turn down at center column")
                    nc2=color53
                    nc5=color50
                    nc8=color47
                    nc20=color2 
                    nc23=color5
                    nc26=color8
                    nc38=color20
                    nc41=color23
                    nc44=color26
                    nc53=color38
                    nc50=color41
                    nc47=color44

                    sleep(0.01)

                    color2=nc2
                    color5=nc5
                    color8=nc8
                    color20=nc20
                    color23=nc23
                    color26=nc26
                    color38=nc38
                    color41=nc41
                    color44=nc44
                    color53=nc53
                    color50=nc50
                    color47=nc47 
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle9):
                    mc.postToChat("turn down at right column")
                    nc3=color52
                    nc6=color49
                    nc9=color46
                    nc21=color3
                    nc24=color6
                    nc27=color9
                    nc39=color21
                    nc42=color24
                    nc45=color27
                    nc52=color39
                    nc49=color42
                    nc46=color45

                    nc28=color30
                    nc31=color29
                    nc34=color28
                    nc35=color31
                    nc36=color34
                    nc33=color35
                    nc30=color36
                    nc29=color33

                    sleep(0.01)

                    color3=nc3
                    color6=nc6
                    color9=nc9
                    color21=nc21
                    color24=nc24
                    color27=nc27
                    color39=nc39
                    color42=nc42
                    color45=nc45
                    color52=nc52
                    color49=nc49
                    color46=nc46

                    color28=nc28
                    color31=nc31
                    color34=nc34
                    color35=nc35
                    color36=nc36
                    color33=nc33
                    color30=nc30
                    color29=nc29

                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle10):
                    mc.postToChat("turn right at up column")
                    nc10=color46
                    nc11=color47
                    nc12=color48
                    nc19=color10
                    nc20=color11
                    nc21=color12
                    nc28=color19
                    nc29=color20
                    nc30=color21
                    nc46=color28
                    nc47=color29
                    nc48=color30

                    nc1=color3
                    nc4=color2
                    nc7=color1
                    nc8=color4
                    nc9=color7
                    nc6=color8
                    nc3=color9
                    nc2=color6

                    sleep(0.01)

                    color10=nc10
                    color11=nc11
                    color12=nc12
                    color19=nc19
                    color20=nc20
                    color21=nc21
                    color28=nc28
                    color29=nc29
                    color30=nc30
                    color46=nc46
                    color47=nc47
                    color48=nc48

                    color1=nc1
                    color4=nc4
                    color7=nc7
                    color8=nc8
                    color9=nc9
                    color6=nc6
                    color3=nc3
                    color2=nc2

                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle11):
                    mc.postToChat("turn right at center column")
                    nc13=color49
                    nc14=color50
                    nc15=color51
                    nc22=color13
                    nc23=color14
                    nc24=color15
                    nc31=color22
                    nc32=color23
                    nc33=color24
                    nc49=color31
                    nc50=color32
                    nc51=color33

                    sleep(0.01)

                    color13=nc13                    
                    color14=nc14
                    color15=nc15
                    color22=nc22
                    color23=nc23
                    color24=nc24
                    color31=nc31
                    color32=nc32
                    color33=nc33
                    color49=nc49
                    color50=nc50
                    color51=nc51
                    
                    sleep(0.01)
                elif is_inside_polygon(mouse_pos, triangle12):
                    mc.postToChat("turn right at down column")
                    nc16=color52
                    nc17=color53
                    nc18=color54
                    nc25=color16
                    nc26=color17
                    nc27=color18
                    nc34=color25
                    nc35=color26
                    nc36=color27
                    nc52=color34
                    nc53=color35
                    nc54=color36

                    nc37=color43
                    nc38=color40
                    nc39=color37
                    nc42=color38
                    nc45=color39
                    nc44=color42
                    nc43=color45
                    nc40=color44

                    sleep(0.01)

                    color16=nc16
                    color17=nc17
                    color18=nc18
                    color25=nc25
                    color26=nc26
                    color27=nc27
                    color34=nc34
                    color35=nc35
                    color36=nc36
                    color52=nc52
                    color53=nc53
                    color54=nc54

                    color37=nc37
                    color38=nc38
                    color39=nc39
                    color42=nc42
                    color45=nc45
                    color44=nc44
                    color43=nc43
                    color40=nc40
                    
                    sleep(0.01)

        mc.setBlock(x+3,y,z+3,color1)
        mc.setBlock(x+2,y,z+3,color2)
        mc.setBlock(x+1,y,z+3,color3)
        mc.setBlock(x+3,y,z+2,color4)
        mc.setBlock(x+2,y,z+2,color5)
        mc.setBlock(x+1,y,z+2,color6)
        mc.setBlock(x+3,y,z+1,color7)
        mc.setBlock(x+2,y,z+1,color8)
        mc.setBlock(x+1,y,z+1,color9)

        sleep(0.01)  

        mc.setBlock(x+4,y-1,z+3,color10)
        mc.setBlock(x+4,y-1,z+2,color11)
        mc.setBlock(x+4,y-1,z+1,color12)
        mc.setBlock(x+4,y-2,z+3,color13)
        mc.setBlock(x+4,y-2,z+2,color14)
        mc.setBlock(x+4,y-2,z+1,color15)
        mc.setBlock(x+4,y-3,z+3,color16)
        mc.setBlock(x+4,y-3,z+2,color17)
        mc.setBlock(x+4,y-3,z+1,color18)

        sleep(0.01)    

        if color19==block1:
            screencolor19=screencolor1
        elif color19==block2:
            screencolor19=screencolor2
        elif color19==block3:
            screencolor19=screencolor3
        elif color19==block4:
            screencolor19=screencolor4
        elif color19==block5:
            screencolor19=screencolor5
        elif color19==block6:
            screencolor19=screencolor6
        mc.setBlock(x+3,y-1,z,color19)
        pygame.draw.rect(screen, screencolor19, [180, 100, 80, 80])

        if color20==block1:
            screencolor20=screencolor1
        elif color20==block2:
            screencolor20=screencolor2
        elif color20==block3:
            screencolor20=screencolor3
        elif color20==block4:
            screencolor20=screencolor4
        elif color20==block5:
            screencolor20=screencolor5
        elif color20==block6:
            screencolor20=screencolor6
        mc.setBlock(x+2,y-1,z,color20)
        pygame.draw.rect(screen, screencolor20, [280, 100, 80, 80])

        if color21==block1:
            screencolor21=screencolor1
        elif color21==block2:
            screencolor21=screencolor2
        elif color21==block3:
            screencolor21=screencolor3
        elif color21==block4:
            screencolor21=screencolor4
        elif color21==block5:
            screencolor21=screencolor5
        elif color21==block6:
            screencolor21=screencolor6
        mc.setBlock(x+1,y-1,z,color21)
        pygame.draw.rect(screen, screencolor21, [380, 100, 80, 80])

        if color22==block1:
            screencolor22=screencolor1
        elif color22==block2:
            screencolor22=screencolor2
        elif color22==block3:
            screencolor22=screencolor3
        elif color22==block4:
            screencolor22=screencolor4
        elif color22==block5:
            screencolor22=screencolor5
        elif color22==block6:
            screencolor22=screencolor6
        mc.setBlock(x+3,y-2,z,color22)
        pygame.draw.rect(screen, screencolor22, [180, 200, 80, 80])

        screencolor23=0
        if color23==block1:
            screencolor23=screencolor1
        elif color23==block2:
            screencolor23=screencolor2
        elif color23==block3:
            screencolor23=screencolor3
        elif color23==block4:
            screencolor23=screencolor4
        elif color23==block5:
            screencolor23=screencolor5
        elif color23==block6:
            screencolor23=screencolor6
        mc.setBlock(x+2,y-2,z,color23)
        pygame.draw.rect(screen, screencolor23, [280, 200, 80, 80])

        if color24==block1:
            screencolor24=screencolor1
        elif color24==block2:
            screencolor24=screencolor2
        elif color24==block3:
            screencolor24=screencolor3
        elif color24==block4:
            screencolor24=screencolor4
        elif color24==block5:
            screencolor24=screencolor5
        elif color24==block6:
            screencolor24=screencolor6
        mc.setBlock(x+1,y-2,z,color24)
        pygame.draw.rect(screen, screencolor24, [380, 200, 80, 80])

        if color25==block1:
            screencolor25=screencolor1
        elif color25==block2:
            screencolor25=screencolor2
        elif color25==block3:
            screencolor25=screencolor3
        elif color25==block4:
            screencolor25=screencolor4
        elif color25==block5:
            screencolor25=screencolor5
        elif color25==block6:
            screencolor25=screencolor6
        mc.setBlock(x+3,y-3,z,color25)
        pygame.draw.rect(screen, screencolor25, [180, 300, 80, 80])

        if color26==block1:
            screencolor26=screencolor1
        elif color26==block2:
            screencolor26=screencolor2
        elif color26==block3:
            screencolor26=screencolor3
        elif color26==block4:
            screencolor26=screencolor4
        elif color26==block5:
            screencolor26=screencolor5
        elif color26==block6:
            screencolor26=screencolor6
        mc.setBlock(x+2,y-3,z,color26)
        pygame.draw.rect(screen, screencolor26, [280, 300, 80, 80])

        if color27==block1:
            screencolor27=screencolor1
        elif color27==block2:
            screencolor27=screencolor2
        elif color27==block3:
            screencolor27=screencolor3
        elif color27==block4:
            screencolor27=screencolor4
        elif color27==block5:
            screencolor27=screencolor5
        elif color27==block6:
            screencolor27=screencolor6
        mc.setBlock(x+1,y-3,z,color27)
        pygame.draw.rect(screen, screencolor27, [380, 300, 80, 80])

        sleep(0.01)

        mc.setBlock(x,y-1,z+1,color28)
        mc.setBlock(x,y-1,z+2,color29)
        mc.setBlock(x,y-1,z+3,color30)
        mc.setBlock(x,y-2,z+1,color31)
        mc.setBlock(x,y-2,z+2,color32)
        mc.setBlock(x,y-2,z+3,color33)
        mc.setBlock(x,y-3,z+1,color34)
        mc.setBlock(x,y-3,z+2,color35)
        mc.setBlock(x,y-3,z+3,color36)

        sleep(0.01)

        mc.setBlock(x+3,y-4,z+1,color37)
        mc.setBlock(x+2,y-4,z+1,color38)
        mc.setBlock(x+1,y-4,z+1,color39)
        mc.setBlock(x+3,y-4,z+2,color40)
        mc.setBlock(x+2,y-4,z+2,color41)
        mc.setBlock(x+1,y-4,z+2,color42)
        mc.setBlock(x+3,y-4,z+3,color43)
        mc.setBlock(x+2,y-4,z+3,color44)
        mc.setBlock(x+1,y-4,z+3,color45)

        sleep(0.01)

        mc.setBlock(x+1,y-1,z+4,color46)
        mc.setBlock(x+2,y-1,z+4,color47)
        mc.setBlock(x+3,y-1,z+4,color48)
        mc.setBlock(x+1,y-2,z+4,color49)
        mc.setBlock(x+2,y-2,z+4,color50)
        mc.setBlock(x+3,y-2,z+4,color51)
        mc.setBlock(x+1,y-3,z+4,color52)
        mc.setBlock(x+2,y-3,z+4,color53)
        mc.setBlock(x+3,y-3,z+4,color54)

        sleep(0.01)

        if color1==color2==color3==color4==color5==color6==color7==color8==color9:
            if color11==color12==color13==color14==color15==color16==color17==color18==color10:
                if color21==color22==color23==color24==color25==color26==color27==color19==color20:
                    if color31==color32==color33==color34==color35==color36==color28==color29==color30:
                        if color41==color42==color43==color44==color45==color37==color38==color39==color40:
                            if color51==color52==color53==color54==color46==color47==color48==color49==color50:
                                mc.setBlocks(x,y,z,x+4,y-4,z+4,block.GOLD_BLOCK)
                                mc.setBlocks(x+1,y-1,z+1,x+3,y-3,z+3,block.BARRIER)
                                mc.setBlocks(x,y-1,z+1,x+4,y-3,z+3,block.DIAMOND_BLOCK)
                                mc.setBlocks(x+1,y,z+1,x+3,y-4,z+3,block.DIAMOND_BLOCK)
                                mc.setBlocks(x+1,y-1,z,x+4,y-3,z+4,block.DIAMOND_BLOCK)
                                print("clear")
                                mc.postToChat("congratuation")
                                mc.postToChat("you won")
                                mc.postToChat("you cleared this cube")
                                break
        pygame.display.update()


gamestart1(mc=mc,x=-10,y=param.Y_SEA + 10,z=-10,block1=block1,block2=block2,block3=block3,block4=block4,block5=block5,block6=block6,frameblock=block7,screencolor1=screencolor1,screencolor2=screencolor2,screencolor3=screencolor3,screencolor4=screencolor4,screencolor5=screencolor5,screencolor6=screencolor6)
