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
        while high > 0:
            ny = inclination
            nx = 1 // inclination
            mc.setBlocks(x, y, z, x, y - inclination, z + size, blockTypeId)
            x += Changex
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizez -= 1
        size = sizez * Changez
        while high > 0:
            ny = inclination
            nx = 1 // inclination
            mc.setBlocks(x, y, z, x + (nx * Changex), y, z + size, blockTypeId)
            x += (Changex * nx)
            high -= 1
            y += 1

    if inclination == 1:
        high = steps
        sizez -= 1
        size = sizez * Changez
        def setStep(mc=mc, x=0, z=0, y=param.Y_SEA + 1, Changex=1, size=3, high=3,  blockTypeId=block.IRON_BLOCK):
            while high > 0:
                mc.setBlocks(x, y, z, x, y - 1, z + size, blockTypeId)
                x += Changex
                high -= 1
                y += 1
        setStep(x, z, y, Changex, size, high,  blockTypeId)
    
    sleep(0.01)

def setStepZ(mc=mc, x=0, z=0, y=param.Y_SEA + 1, sizex=3, steps=3, inclination=1, Changex=-1, Changez=1, blockTypeId=block.IRON_BLOCK):
    # inclination = 1/n or n
    # Changez = 1 or -1
    if inclination > 1:
        high = steps * inclination
        sizex -= 1
        size = sizex * Changex
        while high > 0:
            ny = inclination
            nz = 1 // inclination
            mc.setBlocks(x, y, z, x + size, y - inclination, z, blockTypeId)
            z += Changez
            high -= ny
            y += ny

    if inclination < 1:
        high = steps
        sizex -= 1
        size = sizex * Changex
        while high > 0:
            ny = inclination
            nz = 1 // inclination
            mc.setBlocks(x, y, z + size, x, y, z + (nz * Changex), blockTypeId)
            z += (Changez * nz)
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

setStepX(mc=mc, x=25, z=-25, y=param.Y_SEA + 5, sizez=5, steps=5, inclination= 0.5, Changex=1, Changez=1, blockTypeId=block.IRON_BLOCK)

setStepX(mc=mc, x=25, z=25, y=param.Y_SEA + 5, sizez=5, steps=5, inclination= 1, Changex=1, Changez=1, blockTypeId=block.IRON_BLOCK)

setStepX(mc=mc, x=-25, z=-25, y=param.Y_SEA + 2, sizez=5, steps=6, inclination= 2, Changex=1, Changez=1, blockTypeId=block.IRON_BLOCK)

