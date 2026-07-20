from time import sleep

import pygame
from pygame.locals import Rect
import sys

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("roobic cube")

clearnumber=0
running=0

def gamestart1(x=1,y=1,z=1,):

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

    import random

    # 1. 1〜6の数字を9個ずつ入れた、合計54個のリストを作る
    numbers = [1, 2, 3, 4, 5, 6] * 9

    # 2. リストの中身をランダムにシャッフルする（トランプを切るイメージ）
    random.shuffle(numbers)

    # 3. 54個の変数（今回は辞書のキー）に順番に割り当てる
    # 例として「var_1」から「var_54」までの変数を作ります
    variables = {}
    for i in range(54):
        color_name = f"color_{i+1}"       # 変数の名前（var_1, var_2...）
        variables[color_name] = numbers[i] # シャッフルした数字を割り当て
    
    color1=variables["color_1"]
    color2=variables["color_2"]
    color3=variables["color_3"]
    color4=variables["color_4"]
    color5=variables["color_5"]
    color6=variables["color_6"]
    color7=variables["color_7"]
    color8=variables["color_8"]
    color9=variables["color_9"]

    color10=variables["color_10"]
    color11=variables["color_11"]
    color12=variables["color_12"]
    color13=variables["color_13"]
    color14=variables["color_14"]
    color15=variables["color_15"]
    color16=variables["color_16"]
    color17=variables["color_17"]
    color18=variables["color_18"]

    color19=variables["color_19"]
    color20=variables["color_20"]
    color21=variables["color_21"]
    color22=variables["color_22"]
    color23=variables["color_23"]
    color24=variables["color_24"]
    color25=variables["color_25"]
    color26=variables["color_26"]
    color27=variables["color_27"]

    color28=variables["color_28"]
    color29=variables["color_29"]
    color30=variables["color_30"]
    color31=variables["color_31"]
    color32=variables["color_32"]
    color33=variables["color_33"]
    color34=variables["color_34"]
    color35=variables["color_35"]
    color36=variables["color_36"]

    color37=variables["color_37"]
    color38=variables["color_38"]
    color39=variables["color_39"]
    color40=variables["color_40"]
    color41=variables["color_41"]
    color42=variables["color_42"]
    color43=variables["color_43"]
    color44=variables["color_44"]
    color45=variables["color_45"]

    color46=variables["color_46"]
    color47=variables["color_47"]
    color48=variables["color_48"]
    color49=variables["color_49"]
    color50=variables["color_50"]
    color51=variables["color_51"]
    color52=variables["color_52"]
    color53=variables["color_53"]
    color54=variables["color_54"]

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
        # 画面を塗りつぶす
        screen.fill((255, 255, 255))

        screencolorred=(255,0,0)
        screencolororange=(240,120,0)
        screencoloryellow=(255,255,0)
        screencolorblue=(0,0,255)
        screencolorgreen=(0,255,0)
        screencolorblack=(0,0,0)

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

        if color19==1:
            screencolor19=screencolorred
        elif color19==2:
            screencolor19=screencolororange
        elif color19==3:
            screencolor19=screencoloryellow
        elif color19==4:
            screencolor19=screencolorblue
        elif color19==5:
            screencolor19=screencolorgreen
        elif color19==6:
            screencolor19=screencolorblack
        pygame.draw.rect(screen, screencolor19, [180, 100, 80, 80])
        if color20==1:
            screencolor20=screencolorred
        elif color20==2:
            screencolor20=screencolororange
        elif color20==3:
            screencolor20=screencoloryellow
        elif color20==4:
            screencolor20=screencolorblue
        elif color20==5:
            screencolor20=screencolorgreen
        elif color20==6:
            screencolor20=screencolorblack
        pygame.draw.rect(screen, screencolor20, [280, 100, 80, 80])
        if color21==1:
            screencolor21=screencolorred
        elif color21==2:
            screencolor21=screencolororange
        elif color21==3:
            screencolor21=screencoloryellow
        elif color21==4:
            screencolor21=screencolorblue
        elif color21==5:
            screencolor21=screencolorgreen
        elif color21==6:
            screencolor21=screencolorblack
        pygame.draw.rect(screen, screencolor21, [380, 100, 80, 80])

        if color22==1:
            screencolor22=screencolorred
        elif color22==2:
            screencolor22=screencolororange
        elif color22==3:
            screencolor22=screencoloryellow
        elif color22==4:
            screencolor22=screencolorblue
        elif color22==5:
            screencolor22=screencolorgreen
        elif color22==6:
            screencolor22=screencolorblack
        pygame.draw.rect(screen, screencolor22, [180, 200, 80, 80])
        if color23==1:
            screencolor23=screencolorred
        elif color23==2:
            screencolor23=screencolororange
        elif color23==3:
            screencolor23=screencoloryellow
        elif color23==4:
            screencolor23=screencolorblue
        elif color23==5:
            screencolor23=screencolorgreen
        elif color23==6:
            screencolor23=screencolorblack
        pygame.draw.rect(screen, screencolor23, [280, 200, 80, 80])
        if color24==1:
            screencolor24=screencolorred
        elif color24==2:
            screencolor24=screencolororange
        elif color24==3:
            screencolor24=screencoloryellow
        elif color24==4:
            screencolor24=screencolorblue
        elif color24==5:
            screencolor24=screencolorgreen
        elif color24==6:
            screencolor24=screencolorblack
        pygame.draw.rect(screen, screencolor24, [380, 200, 80, 80])

        if color25==1:
            screencolor25=screencolorred
        elif color25==2:
            screencolor25=screencolororange
        elif color25==3:
            screencolor25=screencoloryellow
        elif color25==4:
            screencolor25=screencolorblue
        elif color25==5:
            screencolor25=screencolorgreen
        elif color25==6:
            screencolor25=screencolorblack
        pygame.draw.rect(screen, screencolor25, [180, 300, 80, 80])
        if color26==1:
            screencolor26=screencolorred
        elif color26==2:
            screencolor26=screencolororange
        elif color26==3:
            screencolor26=screencoloryellow
        elif color26==4:
            screencolor26=screencolorblue
        elif color26==5:
            screencolor26=screencolorgreen
        elif color26==6:
            screencolor26=screencolorblack
        pygame.draw.rect(screen, screencolor26, [280, 300, 80, 80])
        if color27==1:
            screencolor27=screencolorred
        elif color27==2:
            screencolor27=screencolororange
        elif color27==3:
            screencolor27=screencoloryellow
        elif color27==4:
            screencolor27=screencolorblue
        elif color27==5:
            screencolor27=screencolorgreen
        elif color27==6:
            screencolor27=screencolorblack
        pygame.draw.rect(screen, screencolor27, [380, 300, 80, 80])

        sleep(0.01)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # クリックされた「マウスの座標（位置）」を取得
                mouse_pos = event.pos
            
                if is_inside_polygon(mouse_pos, triangle1):
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

        if color1==color2==color3==color4==color5==color6==color7==color8==color9:
            if color11==color12==color13==color14==color15==color16==color17==color18==color10:
                if color21==color22==color23==color24==color25==color26==color27==color19==color20:
                    if color31==color32==color33==color34==color35==color36==color28==color29==color30:
                        if color41==color42==color43==color44==color45==color37==color38==color39==color40:
                            if color51==color52==color53==color54==color46==color47==color48==color49==color50:
                                print("reset")
                                clearnumber+=1
                                running=0
                                break
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if running==0:
        gamestart1()
        running=1