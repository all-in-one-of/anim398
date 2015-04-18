import math
light = hou.node('/obj/pointlight1')
box = hou.node('/obj/box_object1')
boxTuple = box.parmTuple('t')
lightTuple = light.parmTuple('t')

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[2] - p1[2])**2)

lightx = lightTuple[0].eval()-boxTuple[0].eval()
lightz = lightTuple[2].eval()-boxTuple[2].eval()
lightTuple[0].set(lightx*math.cos(math.radians(90))-lightz*math.sin(math.radians(90))+boxTuple[0].eval())
lightTuple[2].set(lightx*math.sin(math.radians(90))+lightz*math.cos(math.radians(90))+boxTuple[2].eval())

