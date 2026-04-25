from time import sleep

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
import a3changecube as chan

def putcube(x=1,y=1,z=1):
    ubsl=chan.cubsl
    ubss=chan.cubss
    ubsr=chan.cubsr
    ussl=chan.cussl
    usss=chan.cusss
    ussr=chan.cussr
    ufsl=chan.cufsl
    ufss=chan.cufss
    ufsr=chan.cufsr

    lusb=chan.clusb
    luss=chan.cluss
    lusf=chan.clusf,
    fusl=chan.cfusl
    fuss=chan.cfuss
    fusr=chan.cfusr
    rusf=chan.crusf
    russ=chan.cruss
    rusb=chan.crusb
    lssb=chan.clssb
    lsss=chan.clsss
    lssf=chan.clssf
    fssl=chan.cfssl
    fsss=chan.cfsss
    fssr=chan.cfssr
    rssf=chan.crssf
    rsss=chan.crsss
    rssb=chan.crssb
    ldsb=chan.cldsb
    ldss=chan.cldss
    ldsf=chan.cldsf
    fdsl=chan.cfdsl
    fdss=chan.cfdss
    fdsr=chan.cfdsr
    rdsf=chan.crdsf
    rdss=chan.crdss
    rdsb=chan.crdsb

    dbsl=chan.cdbsl
    dbss=chan.cdbss
    dbsr=chan.cdbsr
    dssl=chan.cdssl
    dsss=chan.cdsss
    dssr=chan.cdssr
    dfsl=chan.cdfsl
    dfss=chan.cdfss
    dfsr=chan.cdfsr

    busl=chan.cbusl
    buss=chan.cbuss
    busr=chan.cbusr
    bssl=chan.cbssl
    bsss=chan.cbsss
    bssr=chan.cbssr
    bdsl=chan.cbdsl
    bdss=chan.cbdss
    bdsr=chan.cbdsr

    while location< 55:
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

        def putcube(x=1,y=1,z=1):
    
            # Connect to minecraft and open a session as player with origin location
            mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
            mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)
        
            if surface == 1:
                sx=x+point+1
                sy=y
                sz=z+row+1
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)
            if surface == 2:
                sx=x
                sy=y-row-1
                sz=z+point+1
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)
            if surface == 3:
                sx=x+point+1
                sy=y-row-1
                sz=z+4
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)
            if surface == 4:
                sx=x+4
                sy=y-row-1
                sz=z-point+3
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)
            if surface == 5:
                sx=x+point+1
                sy=y-4
                sz=z-row+4
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)
            if surface == 6:
                sx=x+point+1
                sy=y+row-3
                sz=z
                if brocktipe == 1:
                   brocktipeid = block.WHITE_WOOL
                if brocktipe == 2:
                   brocktipeid = block.BLUE_WOOL
                if brocktipe == 3:
                   brocktipeid = block.RED_WOOL
                if brocktipe == 4:
                   brocktipeid = block.YELLOW_WOOL
                if brocktipe == 5:
                   brocktipeid = block.ORANGE_WOOL
                if brocktipe == 6:
                   brocktipeid = block.GREEN_WOOL
                mc.setblock(mc=mc,x=sx,y=sy,z=sz,blocktipeid=brocktipeid)
            sleep(0.01)

        smx=x
        smy=y
        smz=z
        
        putcube(x=smx,y=smy,z=smz)

        sleep(0.01)

        location +=1

