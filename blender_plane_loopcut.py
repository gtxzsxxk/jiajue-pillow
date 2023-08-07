bpy.ops.mesh.primitive_plane_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.05, 0.34, 1))
bpy.context.object.scale[0] = 0.05
bpy.context.object.scale[1] = 0.34

bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":3, 
"smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, 
"edge_index":1, "mesh_select_mode_init":(True, False, False)}, 
TRANSFORM_OT_edge_slide={"value":0, "single_side":False, 
"use_even":False, "flipped":False, "use_clamp":True, "mirror":True, 
"snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, 
"snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, 
"use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0),
 "correct_uv":True, "release_confirm":True, "use_accurate":False})
 
 bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":3, 
"smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, 
"edge_index":2, "mesh_select_mode_init":(True, False, False)}, 
TRANSFORM_OT_edge_slide={"value":0, "single_side":False, 
"use_even":False, "flipped":False, "use_clamp":True, "mirror":True, 
"snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, 
"snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, 
"use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0),
 "correct_uv":True, "release_confirm":True, "use_accurate":False})
