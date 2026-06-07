from time import sleep


from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

def setrandamcube(x=1,y=1,z=1):
    white = 0
    blue = 0
    red =0
    yellow=0
    orange=0
    green=0
    i=0

    # Connect to minecraft and open a session as player with origin location
    mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
    mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

    for i in range(55):
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

    ubsl=cubsl
    ubss=cubss
    ubsr=cubsr
    ussl=cussl
    usss=cusss
    ussr=cussr
    ufsl=cufsl
    ufss=cufss
    ufsr=cufsr

    lusb=clusb
    luss=cluss
    lusf=clusf
    fusl=cfusl
    fuss=cfuss
    fusr=cfusr
    rusf=crusf
    russ=cruss
    rusb=crusb
    lssb=clssb
    lsss=clsss
    lssf=clssf
    fssl=cfssl
    fsss=cfsss
    fssr=cfssr
    rssf=crssf
    rsss=crsss
    rssb=crssb
    ldsb=cldsb
    ldss=cldss
    ldsf=cldsf
    fdsl=cfdsl
    fdss=cfdss
    fdsr=cfdsr
    rdsf=crdsf
    rdss=crdss
    rdsb=crdsb

    dbsl=cdbsl
    dbss=cdbss
    dbsr=cdbsr
    dssl=cdssl
    dsss=cdsss
    dssr=cdssr
    dfsl=cdfsl
    dfss=cdfss
    dfsr=cdfsr

    busl=cbusl
    buss=cbuss
    busr=cbusr
    bssl=cbssl
    bsss=cbsss
    bssr=cbssr
    bdsl=cbdsl
    bdss=cbdss
    bdsr=cbdsr

    sleep(0.01)

    def firstputcube(x=1,y=1,z=1):
    
        location = 0

        while location<55:

            discriminations = location - 1
            sleep(0.01)
            if  discriminations // 9 == 0:
                surface = 1
                discriminationr=discriminations
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=ubsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=ubss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=ubsr
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=ussl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=usss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=ussr
                if discriminationr // 3 == 2 :
                    row = 2
                    discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=ufsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=ufss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=ufsr
            sleep(0.01)
            if  discriminations // 9 == 1:
                surface = 2
                discriminationr=discriminations-9
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=lusb
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=luss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=lusf
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=lssb
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=lsss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=lssf
                if discriminationr // 3 == 2 :
                    row = 2
                    discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=ldsb
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=ldss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=ldsf
            sleep(0.01)
            if  discriminations // 9 == 2:
                surface = 3
                discriminationr=discriminations-18
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=fusl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=fuss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=fusr
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=fssl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=fsss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=fssr
                if discriminationr // 3 == 2 :
                    row = 2
                    discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=fdsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=fdss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=fdsr
            sleep(0.01)
            if  discriminations // 9 == 3:
                surface = 4
                discriminationr=discriminations-27
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=rusf
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=russ
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=rusb
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=rssf
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=rsss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=rssb
                    if discriminationr // 3 == 2 :
                        row = 2
                        discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=rdsf
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=rdss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=rdsb
            sleep(0.01)
            if  discriminations // 9 == 4:
                surface = 5
                discriminationr=discriminations-36
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=dbsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=dbss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=dbsr
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=dssl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=dsss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=dssr
                if discriminationr // 3 == 2 :
                    row = 2
                    discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=dfsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=dfss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=dfsr
            sleep(0.01)
            if  discriminations // 9 == 5:
                surface = 6
                discriminationr=discriminations-45
                if discriminationr // 3 == 0 :
                    row = 0
                    discriminationp=discriminationr
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=busl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=buss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=busr
                if discriminationr // 3 == 1 :
                    row = 1
                    discriminationp =discriminationr - 3
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=bssl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=bsss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=bssr
                if discriminationr // 3 == 2 :
                    row = 2
                    discriminationp =discriminationr - 6
                    if discriminationp % 3 == 0 :
                        point = 0
                        brocktipe=bdsl
                    if discriminationp % 3 == 1 :
                        point = 1
                        brocktipe=bdss
                    if discriminationp % 3 == 2 :
                        point = 2
                        brocktipe=bdsr
            sleep(0.01)
        
            if surface == 1:
                sx=x+point+1
                sy=y
                sz=z+row+1
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
            if surface == 2:
                sx=x
                sy=y-row-1
                sz=z+point+1
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
            if surface == 3:
                sx=x+point+1
                sy=y-row-1
                sz=z+4
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
            if surface == 4:
                sx=x+4
                sy=y-row-1
                sz=z-point+3
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
            if surface == 5:
                sx=x+point+1
                sy=y-4
                sz=z-row+4
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
            if surface == 6:
                sx=x+point+1
                sy=y+row-3
                sz=z
                if brocktipe == 1:
                   mc.setBlock(mc,sx,sy,sz,block.WHITE_WOOL)
                if brocktipe == 2:
                   mc.setBlock(mc,sx,sy,sz,block.BLUE_WOOL)
                if brocktipe == 3:
                  mc.setBlock(mc,sx,sy,sz,block.RED_WOOL)
                if brocktipe == 4:
                   mc.setBlock(mc,sx,sy,sz,block.YELLOW_WOOL)
                if brocktipe == 5:
                   mc.setBlock(mc,sx,sy,sz,block.ORANGE_WOOL)
                if brocktipe == 6:
                   mc.setBlock(mc,sx,sy,sz,block.GREEN_WOOL)
            sleep(0.01)
        smx=x
        smy=y
        smz=z

        firstputcube(smx,smy,smz)

        location+=1
