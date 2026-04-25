from time import sleep

def setrandamcube():
        white = 0
        blue = 0
        red =0
        yellow=0
        orange=0
        green=0
        i=1
        for i in range(54):
            import random

            #1から6までの乱数を生成
            dice = random.randint(1, 6)
            if dice==1:
                white +=1
                if white > 9 :
                    blue+=1
                    if blue >9:
                        red +=1
                        if red >9:
                            yellow+=1
                            if yellow>9:
                                orange+=1
                                if orange >9:
                                    green +=1
                                    color=6
                                else:
                                    color=5
                            else:
                                color=4
                        else:
                            color=3
                    else:
                        color=2
                else:
                    color=1
            
            sleep(0.01)

            if dice==2:
                blue+=1
                if blue >9:
                    red +=1
                    if red >9:
                        yellow+=1
                        if yellow>9:
                            orange+=1
                            if orange >9:
                                green+=1
                                if green>9:
                                    white +=1
                                    color=1
                                else:
                                    color=6
                            else:
                                color=5
                        else:
                            color=4
                    else:
                        color=3
                else:
                    color=2
            
            sleep(0.01)

            if dice==3:
                red +=1
                if red >9:
                    yellow+=1
                    if yellow>9:
                        orange+=1
                        if orange >9:
                            green +=1
                            if green>9:
                                white +=1
                                if white>9:
                                    blue+=1
                                    color=2
                                else:
                                    color=1
                            else:
                                color=6
                        else:
                            color=5
                    else:
                        color=4
                else:
                    color=3

            sleep(0.01)

            if dice==4:
                yellow+=1
                if yellow>9:
                    orange+=1
                    if orange >9:
                        green +=1
                        if green>9:
                            white +=1
                            if white>9:
                                blue+=1
                                if blue>9:
                                    red+=1
                                    color=3
                                else:
                                    color=2
                            else:
                                color=1
                        else:
                            color=6
                    else:
                        color=5
                else:
                    color=4
            
            sleep(0.01)

            if dice==5:
                orange+=1
                if orange >9:
                    green +=1
                    if green>9:
                        white +=1
                        if white>9:
                            blue+=1
                            if blue>9:
                                red+=1
                                if red >9:
                                    yellow+=1
                                    color=4
                                else:
                                    color=3
                            else:
                                color=2
                        else:
                            color=1
                    else:
                        color=6
                else:
                    color=5

            sleep(0.01)

            if dice==6:
                green+=1
                if green >9:
                    white +=1
                    if white>9:
                        blue +=1
                        if blue>9:
                            red+=1
                            if red>9:
                                yellow+=1
                                if yellow >9:
                                    orange+=1
                                    color=5
                                else:
                                    color=4
                            else:
                                color=3
                        else:
                            color=2
                    else:
                        color=1
                else:
                    color=6

            sleep(0.01)

            if i==1:
                cubsl = color
            if i==2:
                cubss=color
            if i==3:
                cubsr=color
            if i==4:
                cussl=color
            if i==5:
                cusss=color
            if i==6:
                cussr=color
            if i==7:
                cufsl=color
            if i==8:
                cufss=color
            if i==9:
                cufsr=color
            
            sleep(0.01)

            if i==10:
                clusb=color
            if i==11:
                cluss=color
            if i==12:
                clusf=color
            if i==13:
                clssb=color
            if i==14:
                clsss=color
            if i==15:
                clssf=color
            if i==16:
                cldsb=color
            if i==17:
                cldss=color
            if i==18:
                cldsf=color
            
            sleep(0.01)

            if i==19:
                cfusl=color
            if i==20:
                cfuss=color
            if i==21:
                cfusr=color
            if i==22:
                cfssl=color
            if i==23:
                cfsss=color
            if i==24:
                cfssr=color
            if i==25:
                cfdsl=color
            if i==26:
                cfdss=color
            if i==27:
                cfdsr=color

            sleep(0.01)

            if i==28:
                crusf=color
            if i==29:
                cruss=color
            if i==30:
                crusb=color
            if i==31:
                crssf=color
            if i==32:
                crsss=color
            if i==33:
                crssb=color
            if i==34:
                crdsf=color
            if i==35:
                crdss=color
            if i==36:
                crdsb=color

            sleep(0.01)

            if i==37:
                cdbsl=color
            if i==38:
                cdbss=color
            if i==39:
                cdbsr=color
            if i==40:
                cdssl=color
            if i==41:
                cdsss=color
            if i==42:
                cdssr=color
            if i==43:
                cdfsl=color
            if i==44:
                cdfss=color
            if i==45:
                cdfsr=color
            
            sleep(0.01)

            if i==46:
                cbusl=color
            if i==47:
                cbuss=color
            if i==48:
                cbusr=color
            if i==49:
                cbssl=color
            if i==50:
                cbsss=color
            if i==51:
                cbssr=color
            if i==52:
                cbdsl=color
            if i==53:
                cbdss=color
            if i==54:
                cbdsr=color

            sleep(0.01)

            i+=1

        sleep(0.01)