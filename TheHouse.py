# TheHouse.py
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.postToChat("Home Sweet, Home")

#Walls
mc.setBlocks(x, y, z+3, x+13, y+4, z+20, block.WOOD.id)
mc.setBlocks(x+1, y, z+4, x+12, y+4, z+19, block.AIR.id)

#Ground and Siling
mc.setBlocks(x-1, y-1, z+2, x+14, y-1, z+21, block.STONE_BRICK.id)
mc.setBlocks(x-1, y+5, z+2, x+14, y+5, z+21, block.STONE_BRICK.id)

#Entrance
mc.setBlock(x+2, y, z+3, block.DOOR_WOOD.id, 0)
mc.setBlock(x+2, y+1, z+3, block.DOOR_WOOD.id, 8)

#Windows
mc.setBlocks(x+11, y+1, z+3, x+4, y+3, z+3, block.GLASS_PANE.id)
mc.setBlocks(x+10, y+1, z+20, x+3, y+3, z+20, block.GLASS_PANE.id)
mc.setBlocks(x, y+1, z+5, x, y+3, z+7, block.GLASS_PANE.id)
mc.setBlocks(x+13, y+1, z+5, x+13, y+3, z+7, block.GLASS_PANE.id)

#There for no Reason
mc.setBlocks(x+7, y+3, z+12, x+7, y+3, z+12, block.LAVA.id)