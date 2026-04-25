from time import sleep

from mc_remote.minecraft import Minecraft
import param_mc_remote as param
from param_mc_remote import PLAYER_ORIGIN as PO
from param_mc_remote import block
import a2firstsetcube as set

# Connect to minecraft and open a session as player with origin location
mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
mc.setPlayer(param.PLAYER_NAME, PO.x, PO.y, PO.z)

def gamestart(mc=mc,x=1,y=1,z=1,): 
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


   set.firstsetcube
   
   nubsl=set.ubsl
   nubss=set.ubss
   nubsr=set.ubsr
   nussl=set.ussl
   nusss=set.usss
   nussr=set.ussr
   nufsl=set.ufsl
   nufss=set.ufss
   nufsr=set.ufsr

   nlusb=set.lusb
   nluss=set.luss
   nlusf=set.lusf,
   nfusl=set.fusl
   nfuss=set.fuss
   nfusr=set.fusr
   nrusf=set.rusf
   nruss=set.russ
   nrusb=set.rusb
   nlssb=set.lssb
   nlsss=set.lsss
   nlssf=set.lssf
   nfssl=set.fssl
   nfsss=set.fsss
   nfssr=set.fssr
   nrssf=set.rssf
   nrsss=set.rsss
   nrssb=set.rssb
   nldsb=set.ldsb
   nldss=set.ldss
   nldsf=set.ldsf
   nfdsl=set.fdsl
   nfdss=set.fdss
   nfdsr=set.fdsr
   nrdsf=set.rdsf
   nrdss=set.rdss
   nrdsb=set.rdsb

   ndbsl=set.dbsl
   ndbss=set.dbss
   ndbsr=set.dbsr
   ndssl=set.dssl
   ndsss=set.dsss
   ndssr=set.dssr
   ndfsl=set.dfsl
   ndfss=set.dfss
   ndfsr=set.dfsr

   nbusl=set.busl
   nbuss=set.buss
   nbusr=set.busr
   nbssl=set.bssl
   nbsss=set.bsss
   nbssr=set.bssr
   nbdsl=set.bdsl
   nbdss=set.bdss
   nbdsr=set.bdsr

    