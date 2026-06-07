from time import sleep

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

def setStepX(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizez=3, steps=3, inclination=1, Changex=-1, Changez=1, blockTypeId=block.IRON_BLOCK):
    # inclination = 1/n or n
    # ChangeX = 1 or -1
    if inclination > 1:
        high = steps * inclination
        sizez -= 1
        size = sizez * Changez
        ny = inclination
        while high > 0:            
            mc.setBlocks(x, y, z, x, y - inclination, z + size, blockTypeId)
            x += Changex
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizez -= 1
        size = sizez * Changez
        nx = 1 / inclination * Changex
        while high > 0:
            mc.setBlocks(x, y, z, x + nx, y, z + size, blockTypeId)
            x += nx
            high -= 1
            y += 1

    if inclination == 1:
        high = steps
        sizez -= 1
        size = sizez * Changez
        while high > 0:
            mc.setBlocks(x, y, z, x, y - 1, z + size, blockTypeId)
            x += Changex
            high -= 1
            y += 1
    
    sleep(0.01)

def setStepZ(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex=3, steps=3, inclination=1, Changex=-1, Changez=1, blockTypeId=block.IRON_BLOCK):
    # inclination = 1/n or n
    # Changez = 1 or -1
    if inclination > 1:
        high = steps * inclination
        sizex -= 1
        size = sizex * Changex
        ny = inclination
        while high > 0:
            mc.setBlocks(x, y, z, x + size, y - inclination, z, blockTypeId)
            z += Changez
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizex -= 1
        size = sizex * Changex
        nz = 1 / inclination * Changex
        while high > 0:
            mc.setBlocks(x, y, z + size, x, y, z + nz, blockTypeId)
            z += nz
            high -= 1
            y += 1

    if inclination == 1:
        high = steps
        sizex -= 1
        size = sizex * Changex
        def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, Changez=1, size=3, high=3,  blockTypeId=block.IRON_BLOCK):
            while high > 0:
                mc.setBlocks(x, y, z, x + size, y - 1, z, blockTypeId)
                z += Changez
                high -= 1
                y += 1
        setStep(x, z, y, Changez, size, high,  blockTypeId)
    
    sleep(0.01)

mc.postToChat("Drawing x-step")

setStepX(mc=mc, x=25, z=-25, y=param.Y_SEA + 5, sizez=5, steps=5, inclination= 1 / 3, Changex=1, Changez=1, blockTypeId=block.IRON_BLOCK)
