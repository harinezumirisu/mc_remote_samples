from time import sleep

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
import a1randamcube as ram
import a2firstsetcube as set

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

def gamestart1(mc=mc,x=1,y=1,z=1,): 
    # color = 1~6
    #1=white 2=blue 3=red 4=yellow 5=orange 6=green
    # u=up d=down l=left r=right f=front b=back 

    #Location
    #1,2,3
    #4,5,6
    #7,8,9

    #10,11,12, 19,20,21, 28,29,30
    #13,14,15, 22,23,24, 31,32,33
    #16,17,18, 25,26,27, 34,35,36

    #37,38,39
    #40,41,42
    #43,44,45

    #46,47,48
    #49,50,51
    #52,53,54

    smx=x
    smy=y
    smz=z

    mc.setBlocks(x,y,z,x+4,y-4,z+4,block.WHITE_CONCRETE)
    mc.setBlocks(x+1,y-1,z+1,x+3,y-3,z+3,block.BARRIER)

    ram.setrandamcube(x=smx,y=smy,z=smz)

def gamestart2(mc=mc,x=1,y=1,z=1,): 
    # color = 1~6
    #1=white 2=blue 3=red 4=yellow 5=orange 6=green
    # u=up d=down l=left r=right f=front b=back 

    #Location
    #1,2,3
    #4,5,6
    #7,8,9

    #10,11,12, 19,20,21, 28,29,30
    #13,14,15, 22,23,24, 31,32,33
    #16,17,18, 25,26,27, 34,35,36

    #37,38,39
    #40,41,42
    #43,44,45

    #46,47,48
    #49,50,51
    #52,53,54

    smx=x
    smy=y
    smz=z

    mc.setBlocks(x,y,z,x+4,y-4,z+4,block.WHITE_CONCRETE)
    mc.setBlocks(x+1,y-1,z+1,x+3,y-3,z+3,block.BARRIER)

    set.putcube(x=smx,y=smy,z=smz)
    
gamestart2(mc=mc,x=10,y=75,z=10,)

   

    