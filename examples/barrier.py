from time import sleep

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block

# axis parameters
AXIS_WIDTH = 40  # x, z: -40 .. 0 .. 40
AXIS_TOP = 127
AXIS_Y_V_ORG = 96  # y of virtual origin
AXIS_BOTTOM = 63  # y: 63 .. 96 .. 127

AXIS_BLOCK_X = block.DIAMOND_BLOCK
AXIS_BLOCK_Y = block.SEA_LANTERN
AXIS_BLOCK_Z = block.GOLD_BLOCK
AXIS_BLOCK_X1 = block.SEA_LANTERN
AXIS_BLOCK_Y1 = block.SEA_LANTERN
AXIS_BLOCK_Z1 = block.SEA_LANTERN
AXIS_BLOCK_TOP = block.GLOWSTONE

def barrier_minecraft_world(mc, width=48):
    mc.postToChat("Barriering your field")
    mc.setBlocks(-width, param.Y_SEA + 1, -width, width, AXIS_TOP-1, -width, block.BARRIER)
    sleep(1)
    mc.setBlocks(-width, AXIS_TOP, -width, width, AXIS_TOP, -width, block.SEA_LANTERN)
    sleep(1)
    mc.setBlocks(width, param.Y_SEA + 1, -width, width, AXIS_TOP-1, width, block.BARRIER)
    sleep(1)
    mc.setBlocks(width, AXIS_TOP, -width, width, AXIS_TOP, width, block.SEA_LANTERN)
    sleep(1)
    mc.setBlocks(width, param.Y_SEA + 1, width, -width, AXIS_TOP-1, width, block.BARRIER)
    sleep(1)
    mc.setBlocks(width, AXIS_TOP, width, -width, AXIS_TOP, width, block.SEA_LANTERN)
    sleep(1)
    mc.setBlocks(-width, param.Y_SEA + 1, width, -width, AXIS_TOP-1, -width, block.BARRIER)
    sleep(1)
    mc.setBlocks(-width, AXIS_TOP, width, -width, AXIS_TOP, -width, block.SEA_LANTERN)
    sleep(1)
    mc.setBlocks(-width+1, AXIS_TOP, -width+1, width-1, AXIS_TOP, width-1, block.BARRIER)
    sleep(1)


if __name__ == "__main__":
    # Connect to minecraft and open a session as player with origin location
    mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
    mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

    mc.postToChat("axis_flat.py")
    # reset_minecraft_world(mc)
    # sleep(20)
    # clear_XYZ_axis(mc, wait=0.05)
    # draw_XYZ_axis(mc, wait=0.02)

    barrier_minecraft_world(mc)
