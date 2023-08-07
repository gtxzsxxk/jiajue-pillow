import bpy
import time
import os

target_name = "SPRING2001"
target_object = None
plane_name = "B_PLANE"
plane_created = False
blend_language = 'zh-cn'
plane_object = None
division = 10
step = 0.5  # unit: cm
initial_height = 0  # z-axis, unit: cm
output_path = "D:\\code\\pillow-srt\\dataset_test"

def set_obj(which,dist):
    for i in which.data.vertices:
        i.co.z=dist

def move_obj(which,dist):
    for i in which.data.vertices:
        i.co.z+=dist
        
def save_txt(div_cnt):
    fp=open(os.path.join(output_path,"splice_%s+%.2f.txt"%(target_name,div_cnt*step)),"w+")
    for i in plane_object.data.vertices:
        fp.write("%.8f %.8f\r\n"%(i.co.x,i.co.y))
    fp.close()
for cnt in range(0, division):
    for i in bpy.data.objects:
        if i.name == plane_name:
            plane_created = True
            plane_object = i
        if i.name == target_name:
            target_object = i

    if plane_created == False:
        bpy.ops.mesh.primitive_plane_add()
        obj = None
        for i in bpy.data.objects:
            if blend_language == 'zh-cn':
                if i.name.__contains__("平面"):
                    obj = i
            else:
                if i.name.__contains__("Plane"):
                    obj = i
        obj.name = plane_name
        plane_object = obj
        
    set_obj(plane_object,initial_height/100)
    move_obj(plane_object,-step*cnt/100)
    plane_object.modifiers.new("MODIFIER","BOOLEAN")
    plane_object.modifiers[0].object = target_object
    plane_object.modifiers[0].operation = "INTERSECT"
    plane_object.modifiers[0].solver = "FAST"
    bpy.ops.object.modifier_apply(modifier="MODIFIER")
    save_txt(cnt)
    bpy.data.objects.remove(plane_object)
    
        
    
    
