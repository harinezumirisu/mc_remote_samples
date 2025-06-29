# Parameters for Minecraft Java Edition

from mc_remote.vec3 import Vec3
import mc_remote.block_id as block
import mc_remote.entity_id as entity
import mc_remote.particle_id as particle


PLAYER_NAME = "harinezumi131"  # set your player name in Minecraft
PLAYER_ORIGIN = Vec3(-100, 0, -300)  # PO.x, PO.y, PO.z
print(f"param_mc_remote loaded for {PLAYER_NAME} at {PLAYER_ORIGIN.x}, {PLAYER_ORIGIN.y}, {PLAYER_ORIGIN.z}")

# minecraft remote connection to the host at address:port
# ADRS_MCR = "localhost"  # Minecraft server running on your pc
ADRS_MCR = "sb.mc-remote.com"  # mc-remote sandbox server
PORT_MCR = 25575  # socket server port

# vertical levels in Minecraft 1.20+
Y_TOP = 320  # the top where blocks can be set
Y_CLOUD_BOTTOM = 199  # the bottom of clouds
Y_SEA = 62  # the sea level
Y_BOTTOM = 0  # the bottom where blocks can be set
Y_BOTTOM_STEVE = -64  # the bottom where Steve can go down
