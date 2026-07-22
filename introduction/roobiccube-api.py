import roobiccubefinal as api
from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

block1=block.RED_WOOL
screencolor1=(255,0,0)
block2=block.ORANGE_WOOL
screencolor2=(240,120,0)
block3=block.YELLOW_WOOL
screencolor3=(255,255,0)
block4=block.BLUE_WOOL
screencolor4=(0,0,255)
block5=block.GREEN_WOOL
screencolor5=(0,255,0)
block6=block.BLACK_WOOL
screencolor6=(0,0,0)
block7=block.WHITE_CONCRETE

api.gamestart1(mc=mc,x=-10,y=param.Y_SEA + 10,z=-10,block1=block1,block2=block2,block3=block3,block4=block4,block5=block5,block6=block6,frameblock=block7,screencolor1=screencolor1,screencolor2=screencolor2,screencolor3=screencolor3,screencolor4=screencolor4,screencolor5=screencolor5,screencolor6=screencolor6)
