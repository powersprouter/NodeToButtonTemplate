#Instructions: 

#Geometry Node Script goes here. Be sure to name your Geometry Node Tree

#       'Node Name' Nodegroup  for the callable name of the modifier
#  		node_name will be variable



import bpy
from bpy.types import Context, Operator




#  * * * * * * * * * * * * * * * * * * * * * * * * 
#  * * * * * * * * * * * * * * * * * * * * * * * * 
#  * * * * * * * * * * * * * * * * * * * * * * * * 






#initialize ducky node group
def ducky_node_group():
	ducky= bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Ducky")

	#initialize ducky nodes
	#node spin
	spin = ducky.nodes.new("NodeFrame")
	spin.label = "Z Spin"

	#node Frame
	frame = ducky.nodes.new("NodeFrame")
	frame.label = "Z Wind Up"

	#node Frame.001
	frame_001 = ducky.nodes.new("NodeFrame")
	frame_001.label = "y spin"

	#node Switch
	switch = ducky.nodes.new("GeometryNodeSwitch")
	switch.input_type = 'VECTOR'
	#Switch_001
	switch.inputs[1].default_value = False
	#False
	switch.inputs[2].default_value = 0.0
	#True
	switch.inputs[3].default_value = 0.0
	#False_001
	switch.inputs[4].default_value = 0
	#True_001
	switch.inputs[5].default_value = 0
	#False_002
	switch.inputs[6].default_value = False
	#True_002
	switch.inputs[7].default_value = True
	#False_004
	switch.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
	#True_004
	switch.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
	#False_005
	switch.inputs[12].default_value = ""
	#True_005
	switch.inputs[13].default_value = ""

	#node Compare
	compare = ducky.nodes.new("FunctionNodeCompare")
	compare.data_type = 'FLOAT'
	compare.operation = 'GREATER_THAN'
	compare.mode = 'ELEMENT'
	#A_INT
	compare.inputs[2].default_value = 0
	#B_INT
	compare.inputs[3].default_value = 0
	#A_VEC3
	compare.inputs[4].default_value = (0.0, 0.0, 0.0)
	#B_VEC3
	compare.inputs[5].default_value = (0.0, 0.0, 0.0)
	#A_COL
	compare.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
	#B_COL
	compare.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
	#A_STR
	compare.inputs[8].default_value = ""
	#B_STR
	compare.inputs[9].default_value = ""
	#C
	compare.inputs[10].default_value = 0.8999999761581421
	#Angle
	compare.inputs[11].default_value = 0.08726649731397629
	#Epsilon
	compare.inputs[12].default_value = 0.0010000000474974513

	#node Reroute.013
	reroute_013 = ducky.nodes.new("NodeReroute")
	#node Reroute.014
	reroute_014 = ducky.nodes.new("NodeReroute")
	#node Reroute.016
	reroute_016 = ducky.nodes.new("NodeReroute")
	#node Reroute.017
	reroute_017 = ducky.nodes.new("NodeReroute")
	#node Reroute.018
	reroute_018 = ducky.nodes.new("NodeReroute")
	#node Reroute.012
	reroute_012 = ducky.nodes.new("NodeReroute")
	#node Float Curve.002
	float_curve_002 = ducky.nodes.new("ShaderNodeFloatCurve")
	#mapping settings
	float_curve_002.mapping.extend = 'EXTRAPOLATED'
	float_curve_002.mapping.tone = 'STANDARD'
	float_curve_002.mapping.black_level = (0.0, 0.0, 0.0)
	float_curve_002.mapping.white_level = (1.0, 1.0, 1.0)
	float_curve_002.mapping.clip_min_x = 0.0
	float_curve_002.mapping.clip_min_y = 0.0
	float_curve_002.mapping.clip_max_x = 1.0
	float_curve_002.mapping.clip_max_y = 1.0
	float_curve_002.mapping.use_clip = True
	#curve 0
	float_curve_002_curve_0 = float_curve_002.mapping.curves[0]
	float_curve_002_curve_0_point_0 = float_curve_002_curve_0.points[0]
	float_curve_002_curve_0_point_0.location = (0.0, 0.0)
	float_curve_002_curve_0_point_0.handle_type = 'AUTO_CLAMPED'
	float_curve_002_curve_0_point_1 = float_curve_002_curve_0.points[1]
	float_curve_002_curve_0_point_1.location = (0.22146117687225342, 0.6577381491661072)
	float_curve_002_curve_0_point_1.handle_type = 'AUTO'
	float_curve_002_curve_0_point_2 = float_curve_002_curve_0.points.new(0.6027394533157349, 0.9702380299568176)
	float_curve_002_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
	float_curve_002_curve_0_point_3 = float_curve_002_curve_0.points.new(0.8447485566139221, 1.0)
	float_curve_002_curve_0_point_3.handle_type = 'AUTO_CLAMPED'
	float_curve_002_curve_0_point_4 = float_curve_002_curve_0.points.new(0.894977331161499, 0.9851190447807312)
	float_curve_002_curve_0_point_4.handle_type = 'AUTO'
	float_curve_002_curve_0_point_5 = float_curve_002_curve_0.points.new(1.0, 0.9791666865348816)
	float_curve_002_curve_0_point_5.handle_type = 'AUTO_CLAMPED'
	#update curve after changes
	float_curve_002.mapping.update()
	#Factor
	float_curve_002.inputs[0].default_value = 1.0

	#node Math.006
	math_006 = ducky.nodes.new("ShaderNodeMath")
	math_006.operation = 'DIVIDE'
	math_006.use_clamp = True
	#Value_002
	math_006.inputs[2].default_value = 0.5

	#node Math.004
	math_004 = ducky.nodes.new("ShaderNodeMath")
	math_004.operation = 'RADIANS'
	#Value_001
	math_004.inputs[1].default_value = 0.5
	#Value_002
	math_004.inputs[2].default_value = 0.5

	#node Switch.001
	switch_001 = ducky.nodes.new("GeometryNodeSwitch")
	switch_001.input_type = 'FLOAT'
	#Switch_001
	switch_001.inputs[1].default_value = False
	#False
	switch_001.inputs[2].default_value = 0.0
	#False_001
	switch_001.inputs[4].default_value = 0
	#True_001
	switch_001.inputs[5].default_value = 0
	#False_002
	switch_001.inputs[6].default_value = False
	#True_002
	switch_001.inputs[7].default_value = True
	#False_003
	switch_001.inputs[8].default_value = (0.0, 0.0, 0.0)
	#True_003
	switch_001.inputs[9].default_value = (0.0, 0.0, 0.0)
	#False_004
	switch_001.inputs[10].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
	#True_004
	switch_001.inputs[11].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
	#False_005
	switch_001.inputs[12].default_value = ""
	#True_005
	switch_001.inputs[13].default_value = ""

	#node Compare.002
	compare_002 = ducky.nodes.new("FunctionNodeCompare")
	compare_002.data_type = 'FLOAT'
	compare_002.operation = 'LESS_EQUAL'
	compare_002.mode = 'ELEMENT'
	#A_INT
	compare_002.inputs[2].default_value = 0
	#B_INT
	compare_002.inputs[3].default_value = 0
	#A_VEC3
	compare_002.inputs[4].default_value = (0.0, 0.0, 0.0)
	#B_VEC3
	compare_002.inputs[5].default_value = (0.0, 0.0, 0.0)
	#A_COL
	compare_002.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
	#B_COL
	compare_002.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
	#A_STR
	compare_002.inputs[8].default_value = ""
	#B_STR
	compare_002.inputs[9].default_value = ""
	#C
	compare_002.inputs[10].default_value = 0.8999999761581421
	#Angle
	compare_002.inputs[11].default_value = 0.08726649731397629
	#Epsilon
	compare_002.inputs[12].default_value = 0.0010000000474974513

	#node Combine XYZ.001
	combine_xyz_001 = ducky.nodes.new("ShaderNodeCombineXYZ")
	#X
	combine_xyz_001.inputs[0].default_value = 0.0

	#node Reroute.020
	reroute_020 = ducky.nodes.new("NodeReroute")
	#node Reroute.019
	reroute_019 = ducky.nodes.new("NodeReroute")
	#node Reroute.023
	reroute_023 = ducky.nodes.new("NodeReroute")
	#node Reroute.024
	reroute_024 = ducky.nodes.new("NodeReroute")
	#node Reroute.021
	reroute_021 = ducky.nodes.new("NodeReroute")
	#node Reroute.022
	reroute_022 = ducky.nodes.new("NodeReroute")
	#node Reroute.015
	reroute_015 = ducky.nodes.new("NodeReroute")
	#node Reroute.027
	reroute_027 = ducky.nodes.new("NodeReroute")
	#node Reroute.025
	reroute_025 = ducky.nodes.new("NodeReroute")
	#node Reroute.028
	reroute_028 = ducky.nodes.new("NodeReroute")
	#node Reroute.029
	reroute_029 = ducky.nodes.new("NodeReroute")
	#node Reroute.030
	reroute_030 = ducky.nodes.new("NodeReroute")
	#node Reroute.031
	reroute_031 = ducky.nodes.new("NodeReroute")
	#node Reroute.026
	reroute_026 = ducky.nodes.new("NodeReroute")
	#node Transform Geometry
	transform_geometry = ducky.nodes.new("GeometryNodeTransform")
	#Translation
	transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
	#Scale
	transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

	#node Math.003
	math_003 = ducky.nodes.new("ShaderNodeMath")
	math_003.operation = 'MULTIPLY'
	#Value_002
	math_003.inputs[2].default_value = 0.5

	#node Combine XYZ
	combine_xyz = ducky.nodes.new("ShaderNodeCombineXYZ")
	#X
	combine_xyz.inputs[0].default_value = 0.0
	#Y
	combine_xyz.inputs[1].default_value = 0.0

	#node Math.002
	math_002 = ducky.nodes.new("ShaderNodeMath")
	math_002.operation = 'RADIANS'
	#Value_001
	math_002.inputs[1].default_value = 0.5
	#Value_002
	math_002.inputs[2].default_value = 0.5

	#node Reroute.002
	reroute_002 = ducky.nodes.new("NodeReroute")
	#node Map Range
	map_range = ducky.nodes.new("ShaderNodeMapRange")
	map_range.data_type = 'FLOAT'
	map_range.interpolation_type = 'LINEAR'
	map_range.clamp = True
	#To Min
	map_range.inputs[3].default_value = 0.0
	#Steps
	map_range.inputs[5].default_value = 4.0
	#Vector
	map_range.inputs[6].default_value = (0.0, 0.0, 0.0)
	#From_Min_FLOAT3
	map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
	#From_Max_FLOAT3
	map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
	#To_Min_FLOAT3
	map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
	#To_Max_FLOAT3
	map_range.inputs[10].default_value = (1.0, 1.0, 1.0)
	#Steps_FLOAT3
	map_range.inputs[11].default_value = (4.0, 4.0, 4.0)

	#node Float Curve.001
	float_curve_001 = ducky.nodes.new("ShaderNodeFloatCurve")
	#mapping settings
	float_curve_001.mapping.extend = 'EXTRAPOLATED'
	float_curve_001.mapping.tone = 'STANDARD'
	float_curve_001.mapping.black_level = (0.0, 0.0, 0.0)
	float_curve_001.mapping.white_level = (1.0, 1.0, 1.0)
	float_curve_001.mapping.clip_min_x = 0.0
	float_curve_001.mapping.clip_min_y = 0.0
	float_curve_001.mapping.clip_max_x = 1.0
	float_curve_001.mapping.clip_max_y = 1.0
	float_curve_001.mapping.use_clip = True
	#curve 0
	float_curve_001_curve_0 = float_curve_001.mapping.curves[0]
	float_curve_001_curve_0_point_0 = float_curve_001_curve_0.points[0]
	float_curve_001_curve_0_point_0.location = (1.1641532182693481e-09, 0.0)
	float_curve_001_curve_0_point_0.handle_type = 'AUTO_CLAMPED'
	float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
	float_curve_001_curve_0_point_1.location = (0.04109583795070648, 0.03869002312421799)
	float_curve_001_curve_0_point_1.handle_type = 'AUTO'
	float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(0.2625569701194763, 0.7767852544784546)
	float_curve_001_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
	float_curve_001_curve_0_point_3 = float_curve_001_curve_0.points.new(0.49086833000183105, 0.9494045376777649)
	float_curve_001_curve_0_point_3.handle_type = 'AUTO'
	float_curve_001_curve_0_point_4 = float_curve_001_curve_0.points.new(1.0, 1.0)
	float_curve_001_curve_0_point_4.handle_type = 'AUTO'
	#update curve after changes
	float_curve_001.mapping.update()
	#Factor
	float_curve_001.inputs[0].default_value = 1.0

	#node Math.001
	math_001 = ducky.nodes.new("ShaderNodeMath")
	math_001.operation = 'DIVIDE'
	math_001.use_clamp = True
	#Value_002
	math_001.inputs[2].default_value = 0.5

	#node Reroute.009
	reroute_009 = ducky.nodes.new("NodeReroute")
	#node Reroute.004
	reroute_004 = ducky.nodes.new("NodeReroute")
	#node Reroute.005
	reroute_005 = ducky.nodes.new("NodeReroute")
	#node Reroute.010
	reroute_010 = ducky.nodes.new("NodeReroute")
	#node Reroute.006
	reroute_006 = ducky.nodes.new("NodeReroute")
	#node Reroute.007
	reroute_007 = ducky.nodes.new("NodeReroute")
	#node Reroute.003
	reroute_003 = ducky.nodes.new("NodeReroute")
	#node Reroute.001
	reroute_001 = ducky.nodes.new("NodeReroute")
	#node Reroute
	reroute = ducky.nodes.new("NodeReroute")
	#node Reroute.011
	reroute_011 = ducky.nodes.new("NodeReroute")
	#node Reroute.008
	reroute_008 = ducky.nodes.new("NodeReroute")
	#node Scene Time
	scene_time = ducky.nodes.new("GeometryNodeInputSceneTime")

	#node Map Range.001
	map_range_001 = ducky.nodes.new("ShaderNodeMapRange")
	map_range_001.data_type = 'FLOAT'
	map_range_001.interpolation_type = 'LINEAR'
	map_range_001.clamp = True
	#To Min
	map_range_001.inputs[3].default_value = 0.0
	#Steps
	map_range_001.inputs[5].default_value = 4.0
	#Vector
	map_range_001.inputs[6].default_value = (0.0, 0.0, 0.0)
	#From_Min_FLOAT3
	map_range_001.inputs[7].default_value = (0.0, 0.0, 0.0)
	#From_Max_FLOAT3
	map_range_001.inputs[8].default_value = (1.0, 1.0, 1.0)
	#To_Min_FLOAT3
	map_range_001.inputs[9].default_value = (0.0, 0.0, 0.0)
	#To_Max_FLOAT3
	map_range_001.inputs[10].default_value = (1.0, 1.0, 1.0)
	#Steps_FLOAT3
	map_range_001.inputs[11].default_value = (4.0, 4.0, 4.0)

	#node Math.005
	math_005 = ducky.nodes.new("ShaderNodeMath")
	math_005.operation = 'MULTIPLY'
	#Value_002
	math_005.inputs[2].default_value = 0.5

	#node Reroute.036
	reroute_036 = ducky.nodes.new("NodeReroute")
	#node Reroute.037
	reroute_037 = ducky.nodes.new("NodeReroute")
	#node Reroute.034
	reroute_034 = ducky.nodes.new("NodeReroute")
	#node Reroute.038
	reroute_038 = ducky.nodes.new("NodeReroute")
	#node Reroute.039
	reroute_039 = ducky.nodes.new("NodeReroute")
	#node Reroute.035
	reroute_035 = ducky.nodes.new("NodeReroute")
	#node Math.008
	math_008 = ducky.nodes.new("ShaderNodeMath")
	math_008.operation = 'DIVIDE'
	math_008.use_clamp = True
	#Value_002
	math_008.inputs[2].default_value = 0.5

	#node Math
	math = ducky.nodes.new("ShaderNodeMath")
	math.operation = 'SUBTRACT'
	#Value_002
	math.inputs[2].default_value = 0.5

	#node Float Curve.004
	float_curve_004 = ducky.nodes.new("ShaderNodeFloatCurve")
	#mapping settings
	float_curve_004.mapping.extend = 'EXTRAPOLATED'
	float_curve_004.mapping.tone = 'STANDARD'
	float_curve_004.mapping.black_level = (0.0, 0.0, 0.0)
	float_curve_004.mapping.white_level = (1.0, 1.0, 1.0)
	float_curve_004.mapping.clip_min_x = 0.0
	float_curve_004.mapping.clip_min_y = 0.0
	float_curve_004.mapping.clip_max_x = 1.0
	float_curve_004.mapping.clip_max_y = 1.0
	float_curve_004.mapping.use_clip = True
	#curve 0
	float_curve_004_curve_0 = float_curve_004.mapping.curves[0]
	float_curve_004_curve_0_point_0 = float_curve_004_curve_0.points[0]
	float_curve_004_curve_0_point_0.location = (0.0, 0.0)
	float_curve_004_curve_0_point_0.handle_type = 'AUTO_CLAMPED'
	float_curve_004_curve_0_point_1 = float_curve_004_curve_0.points[1]
	float_curve_004_curve_0_point_1.location = (0.22146117687225342, 0.6577381491661072)
	float_curve_004_curve_0_point_1.handle_type = 'AUTO'
	float_curve_004_curve_0_point_2 = float_curve_004_curve_0.points.new(0.6027394533157349, 0.9702380299568176)
	float_curve_004_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
	float_curve_004_curve_0_point_3 = float_curve_004_curve_0.points.new(1.0, 1.0)
	float_curve_004_curve_0_point_3.handle_type = 'AUTO_CLAMPED'
	#update curve after changes
	float_curve_004.mapping.update()
	#Factor
	float_curve_004.inputs[0].default_value = 1.0

	#node Math.009
	math_009 = ducky.nodes.new("ShaderNodeMath")
	math_009.operation = 'RADIANS'
	#Value_001
	math_009.inputs[1].default_value = 0.5
	#Value_002
	math_009.inputs[2].default_value = 0.5

	#node Reroute.033
	reroute_033 = ducky.nodes.new("NodeReroute")
	#node Reroute.032
	reroute_032 = ducky.nodes.new("NodeReroute")
	#node Math.007
	math_007 = ducky.nodes.new("ShaderNodeMath")
	math_007.operation = 'MULTIPLY'
	#Value_002
	math_007.inputs[2].default_value = 0.5

	#node Compare.001
	compare_001 = ducky.nodes.new("FunctionNodeCompare")
	compare_001.data_type = 'FLOAT'
	compare_001.operation = 'GREATER_THAN'
	compare_001.mode = 'ELEMENT'
	#A_INT
	compare_001.inputs[2].default_value = 0
	#B_INT
	compare_001.inputs[3].default_value = 0
	#A_VEC3
	compare_001.inputs[4].default_value = (0.0, 0.0, 0.0)
	#B_VEC3
	compare_001.inputs[5].default_value = (0.0, 0.0, 0.0)
	#A_COL
	compare_001.inputs[6].default_value = (0.0, 0.0, 0.0, 0.0)
	#B_COL
	compare_001.inputs[7].default_value = (0.0, 0.0, 0.0, 0.0)
	#A_STR
	compare_001.inputs[8].default_value = ""
	#B_STR
	compare_001.inputs[9].default_value = ""
	#C
	compare_001.inputs[10].default_value = 0.8999999761581421
	#Angle
	compare_001.inputs[11].default_value = 0.08726649731397629
	#Epsilon
	compare_001.inputs[12].default_value = 0.0010000000474974513

	#node Reroute.040
	reroute_040 = ducky.nodes.new("NodeReroute")
	#node Reroute.041
	reroute_041 = ducky.nodes.new("NodeReroute")
	#node Math.010
	math_010 = ducky.nodes.new("ShaderNodeMath")
	math_010.operation = 'SUBTRACT'
	#Value_002
	math_010.inputs[2].default_value = 0.5

	#node Map Range.002
	map_range_002 = ducky.nodes.new("ShaderNodeMapRange")
	map_range_002.data_type = 'FLOAT'
	map_range_002.interpolation_type = 'LINEAR'
	map_range_002.clamp = True
	#To Min
	map_range_002.inputs[3].default_value = 0.0
	#Steps
	map_range_002.inputs[5].default_value = 4.0
	#Vector
	map_range_002.inputs[6].default_value = (0.0, 0.0, 0.0)
	#From_Min_FLOAT3
	map_range_002.inputs[7].default_value = (0.0, 0.0, 0.0)
	#From_Max_FLOAT3
	map_range_002.inputs[8].default_value = (1.0, 1.0, 1.0)
	#To_Min_FLOAT3
	map_range_002.inputs[9].default_value = (0.0, 0.0, 0.0)
	#To_Max_FLOAT3
	map_range_002.inputs[10].default_value = (1.0, 1.0, 1.0)
	#Steps_FLOAT3
	map_range_002.inputs[11].default_value = (4.0, 4.0, 4.0)

	#ducky inputs
	#input Geometry
	ducky.inputs.new('NodeSocketGeometry', "Geometry")
	ducky.inputs[0].attribute_domain = 'POINT'

	#input End KeyFrame ZWindup
	ducky.inputs.new('NodeSocketFloat', "End KeyFrame ZWindup")
	ducky.inputs[1].default_value = 13.0
	ducky.inputs[1].min_value = -10000.0
	ducky.inputs[1].max_value = 10000.0
	ducky.inputs[1].attribute_domain = 'POINT'

	#input Start KeyFrame ZWindup
	ducky.inputs.new('NodeSocketFloat', "Start KeyFrame ZWindup")
	ducky.inputs[2].default_value = 1.0
	ducky.inputs[2].min_value = -10000.0
	ducky.inputs[2].max_value = 10000.0
	ducky.inputs[2].attribute_domain = 'POINT'

	#input ZWindup Degrees
	ducky.inputs.new('NodeSocketFloat', "ZWindup Degrees")
	ducky.inputs[3].default_value = -33.900001525878906
	ducky.inputs[3].min_value = -10000.0
	ducky.inputs[3].max_value = 10000.0
	ducky.inputs[3].attribute_domain = 'POINT'

	#input Start Keyframe ZSpin
	ducky.inputs.new('NodeSocketFloat', "Start Keyframe ZSpin")
	ducky.inputs[4].default_value = 13.0
	ducky.inputs[4].min_value = -10000.0
	ducky.inputs[4].max_value = 10000.0
	ducky.inputs[4].attribute_domain = 'POINT'

	#input End Keyframe ZSpin
	ducky.inputs.new('NodeSocketFloat', "End Keyframe ZSpin")
	ducky.inputs[5].default_value = 148.0
	ducky.inputs[5].min_value = -10000.0
	ducky.inputs[5].max_value = 10000.0
	ducky.inputs[5].attribute_domain = 'POINT'

	#input ZSpin Degrees
	ducky.inputs.new('NodeSocketFloat', "ZSpin Degrees")
	ducky.inputs[6].default_value = 1841.739990234375
	ducky.inputs[6].min_value = -10000.0
	ducky.inputs[6].max_value = 10000.0
	ducky.inputs[6].attribute_domain = 'POINT'

	#input Start KF YSpin
	ducky.inputs.new('NodeSocketFloat', "Start KF YSpin")
	ducky.inputs[7].default_value = 75.0
	ducky.inputs[7].min_value = -10000.0
	ducky.inputs[7].max_value = 10000.0
	ducky.inputs[7].attribute_domain = 'POINT'

	#input End KF YSpin
	ducky.inputs.new('NodeSocketFloat', "End KF YSpin")
	ducky.inputs[8].default_value = 128.0
	ducky.inputs[8].min_value = -10000.0
	ducky.inputs[8].max_value = 10000.0
	ducky.inputs[8].attribute_domain = 'POINT'

	#input YSpin degrees
	ducky.inputs.new('NodeSocketFloat', "YSpin degrees")
	ducky.inputs[9].default_value = 720.0
	ducky.inputs[9].min_value = -10000.0
	ducky.inputs[9].max_value = 10000.0
	ducky.inputs[9].attribute_domain = 'POINT'


	#node Group Input
	group_input = ducky.nodes.new("NodeGroupInput")

	#ducky outputs
	#output Geometry
	ducky.outputs.new('NodeSocketGeometry', "Geometry")
	ducky.outputs[0].attribute_domain = 'POINT'


	#node Group Output
	group_output = ducky.nodes.new("NodeGroupOutput")

	#Set parents
	float_curve_002.parent = spin
	math_006.parent = spin
	math_004.parent = spin
	switch_001.parent = spin
	compare_002.parent = spin
	combine_xyz_001.parent = spin
	reroute_020.parent = spin
	reroute_019.parent = spin
	reroute_023.parent = spin
	reroute_024.parent = spin
	reroute_021.parent = spin
	reroute_022.parent = spin
	reroute_015.parent = spin
	reroute_027.parent = spin
	reroute_025.parent = spin
	reroute_028.parent = spin
	reroute_029.parent = spin
	reroute_030.parent = spin
	reroute_031.parent = spin
	reroute_026.parent = spin
	math_003.parent = frame
	combine_xyz.parent = frame
	math_002.parent = frame
	reroute_002.parent = frame
	map_range.parent = frame
	float_curve_001.parent = frame
	math_001.parent = frame
	reroute_009.parent = frame
	reroute_004.parent = frame
	reroute_005.parent = frame
	reroute_010.parent = frame
	reroute_006.parent = frame
	reroute_007.parent = frame
	reroute_003.parent = frame
	reroute_001.parent = frame
	reroute.parent = frame
	map_range_001.parent = spin
	math_005.parent = spin
	reroute_036.parent = spin
	reroute_037.parent = spin
	reroute_034.parent = spin
	reroute_038.parent = spin
	reroute_039.parent = spin
	reroute_035.parent = spin
	math_008.parent = frame_001
	math.parent = frame_001
	float_curve_004.parent = frame_001
	math_009.parent = frame_001
	reroute_033.parent = frame_001
	reroute_032.parent = frame_001
	math_007.parent = frame_001
	compare_001.parent = spin
	reroute_040.parent = frame_001
	math_010.parent = frame_001
	map_range_002.parent = frame_001

	#Set locations
	spin.location = (271.30908203125, 1007.3134765625)
	frame.location = (-387.758056640625, 1132.09912109375)
	frame_001.location = (397.7972412109375, 691.6746826171875)
	switch.location = (1707.396240234375, 1332.43408203125)
	compare.location = (609.9258422851562, 1536.8426513671875)
	reroute_013.location = (1598.43408203125, 208.48590087890625)
	reroute_014.location = (1818.0255126953125, 204.2693328857422)
	reroute_016.location = (969.518798828125, 1501.1170654296875)
	reroute_017.location = (976.702392578125, 1311.649169921875)
	reroute_018.location = (1584.2403564453125, 1309.82421875)
	reroute_012.location = (1588.4990234375, 1123.7801513671875)
	float_curve_002.location = (-493.6226806640625, -1427.8951416015625)
	math_006.location = (-814.1204833984375, -1428.7987060546875)
	math_004.location = (627.2147827148438, -1008.5499267578125)
	switch_001.location = (779.7398071289062, -1656.037353515625)
	compare_002.location = (559.8403930664062, -1757.656494140625)
	combine_xyz_001.location = (1110.48095703125, -1024.9644775390625)
	reroute_020.location = (992.8851318359375, -1693.07275390625)
	reroute_019.location = (983.5068359375, -935.8101196289062)
	reroute_023.location = (830.259765625, -1041.683349609375)
	reroute_024.location = (828.7396240234375, -1129.760498046875)
	reroute_021.location = (1075.6319580078125, -1108.968994140625)
	reroute_022.location = (1074.7646484375, -938.0849609375)
	reroute_015.location = (1320.3455810546875, -1060.3701171875)
	reroute_027.location = (267.59600830078125, -1057.21533203125)
	reroute_025.location = (200.74774169921875, -1367.435302734375)
	reroute_028.location = (271.17999267578125, -1149.9779052734375)
	reroute_029.location = (831.130859375, -2157.15576171875)
	reroute_030.location = (745.616943359375, -1804.8621826171875)
	reroute_031.location = (759.4197998046875, -2026.96044921875)
	reroute_026.location = (197.75909423828125, -1056.7608642578125)
	transform_geometry.location = (2094.88232421875, 1740.8822021484375)
	math_003.location = (-36.65228271484375, -370.43743896484375)
	combine_xyz.location = (1003.6609497070312, -32.34564971923828)
	math_002.location = (499.67291259765625, -90.00458526611328)
	reroute_002.location = (-389.53485107421875, -473.3421630859375)
	map_range.location = (171.20303344726562, -102.35668182373047)
	float_curve_001.location = (-376.44085693359375, -521.3928833007812)
	math_001.location = (-651.1799926757812, -505.60186767578125)
	reroute_009.location = (-37.296173095703125, -19.58050537109375)
	reroute_004.location = (-662.5194702148438, -24.38970947265625)
	reroute_005.location = (-866.5023803710938, 56.4356689453125)
	reroute_010.location = (-661.5935668945312, 62.6280517578125)
	reroute_006.location = (-410.8328857421875, -108.41925048828125)
	reroute_007.location = (-42.09423828125, -300.09088134765625)
	reroute_003.location = (-396.82861328125, -245.1790771484375)
	reroute_001.location = (-766.0231323242188, -649.6807250976562)
	reroute.location = (-772.9343872070312, -260.86474609375)
	reroute_011.location = (-1020.2620849609375, 1681.732421875)
	reroute_008.location = (-348.05352783203125, 1375.32275390625)
	scene_time.location = (-1873.4100341796875, 1495.6497802734375)
	map_range_001.location = (299.0428466796875, -1004.2757568359375)
	math_005.location = (13.263664245605469, -1329.5716552734375)
	reroute_036.location = (-943.2544555664062, -1562.29052734375)
	reroute_037.location = (-943.4371337890625, -1089.7747802734375)
	reroute_034.location = (-1188.012939453125, -1123.9951171875)
	reroute_038.location = (-80.15106201171875, -1221.984130859375)
	reroute_039.location = (-58.1995849609375, -1442.89208984375)
	reroute_035.location = (-1186.787109375, -1561.108642578125)
	math_008.location = (-683.4851684570312, -2615.70751953125)
	math.location = (-875.1083984375, -2617.16455078125)
	float_curve_004.location = (-467.9092102050781, -2701.30517578125)
	math_009.location = (933.1383056640625, -2244.064208984375)
	reroute_033.location = (594.0797119140625, -2339.11376953125)
	reroute_032.location = (552.8158569335938, -2339.989013671875)
	math_007.location = (312.0243835449219, -2548.200439453125)
	compare_001.location = (340.0603942871094, -1761.2020263671875)
	reroute_040.location = (-1328.01318359375, -2174.482666015625)
	reroute_041.location = (-1137.76904296875, -1698.7205810546875)
	math_010.location = (-922.5781860351562, -2863.0703125)
	map_range_002.location = (655.3948974609375, -2288.213134765625)
	group_input.location = (-2684.58154296875, -178.66514587402344)
	group_output.location = (3208.5966796875, -41.13558578491211)

	#Set dimensions
	spin.width, spin.height = 2579.3583984375, 1301.595703125
	frame.width, frame.height = 2077.260498046875, 991.9771728515625
	frame_001.width, frame_001.height = 2468.2158203125, 933.942138671875
	switch.width, switch.height = 140.0, 100.0
	compare.width, compare.height = 140.0, 100.0
	reroute_013.width, reroute_013.height = 16.0, 100.0
	reroute_014.width, reroute_014.height = 16.0, 100.0
	reroute_016.width, reroute_016.height = 16.0, 100.0
	reroute_017.width, reroute_017.height = 16.0, 100.0
	reroute_018.width, reroute_018.height = 16.0, 100.0
	reroute_012.width, reroute_012.height = 16.0, 100.0
	float_curve_002.width, float_curve_002.height = 240.0, 100.0
	math_006.width, math_006.height = 140.0, 100.0
	math_004.width, math_004.height = 140.0, 100.0
	switch_001.width, switch_001.height = 140.0, 100.0
	compare_002.width, compare_002.height = 140.0, 100.0
	combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
	reroute_020.width, reroute_020.height = 16.0, 100.0
	reroute_019.width, reroute_019.height = 16.0, 100.0
	reroute_023.width, reroute_023.height = 16.0, 100.0
	reroute_024.width, reroute_024.height = 16.0, 100.0
	reroute_021.width, reroute_021.height = 16.0, 100.0
	reroute_022.width, reroute_022.height = 16.0, 100.0
	reroute_015.width, reroute_015.height = 16.0, 100.0
	reroute_027.width, reroute_027.height = 16.0, 100.0
	reroute_025.width, reroute_025.height = 16.0, 100.0
	reroute_028.width, reroute_028.height = 16.0, 100.0
	reroute_029.width, reroute_029.height = 16.0, 100.0
	reroute_030.width, reroute_030.height = 16.0, 100.0
	reroute_031.width, reroute_031.height = 16.0, 100.0
	reroute_026.width, reroute_026.height = 16.0, 100.0
	transform_geometry.width, transform_geometry.height = 140.0, 100.0
	math_003.width, math_003.height = 140.0, 100.0
	combine_xyz.width, combine_xyz.height = 140.0, 100.0
	math_002.width, math_002.height = 140.0, 100.0
	reroute_002.width, reroute_002.height = 16.0, 100.0
	map_range.width, map_range.height = 176.39990234375, 100.0
	float_curve_001.width, float_curve_001.height = 240.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	reroute_009.width, reroute_009.height = 16.0, 100.0
	reroute_004.width, reroute_004.height = 16.0, 100.0
	reroute_005.width, reroute_005.height = 16.0, 100.0
	reroute_010.width, reroute_010.height = 16.0, 100.0
	reroute_006.width, reroute_006.height = 16.0, 100.0
	reroute_007.width, reroute_007.height = 16.0, 100.0
	reroute_003.width, reroute_003.height = 16.0, 100.0
	reroute_001.width, reroute_001.height = 16.0, 100.0
	reroute.width, reroute.height = 16.0, 100.0
	reroute_011.width, reroute_011.height = 16.0, 100.0
	reroute_008.width, reroute_008.height = 16.0, 100.0
	scene_time.width, scene_time.height = 140.0, 100.0
	map_range_001.width, map_range_001.height = 176.39990234375, 100.0
	math_005.width, math_005.height = 140.0, 100.0
	reroute_036.width, reroute_036.height = 16.0, 100.0
	reroute_037.width, reroute_037.height = 16.0, 100.0
	reroute_034.width, reroute_034.height = 16.0, 100.0
	reroute_038.width, reroute_038.height = 16.0, 100.0
	reroute_039.width, reroute_039.height = 16.0, 100.0
	reroute_035.width, reroute_035.height = 16.0, 100.0
	math_008.width, math_008.height = 140.0, 100.0
	math.width, math.height = 140.0, 100.0
	float_curve_004.width, float_curve_004.height = 700.0, 100.0
	math_009.width, math_009.height = 140.0, 100.0
	reroute_033.width, reroute_033.height = 16.0, 100.0
	reroute_032.width, reroute_032.height = 16.0, 100.0
	math_007.width, math_007.height = 140.0, 100.0
	compare_001.width, compare_001.height = 140.0, 100.0
	reroute_040.width, reroute_040.height = 16.0, 100.0
	reroute_041.width, reroute_041.height = 16.0, 100.0
	math_010.width, math_010.height = 140.0, 100.0
	map_range_002.width, map_range_002.height = 176.39990234375, 100.0
	group_input.width, group_input.height = 140.0, 100.0
	group_output.width, group_output.height = 140.0, 100.0

	#initialize ducky links
	#math_006.Value -> float_curve_002.Value
	ducky.links.new(math_006.outputs[0], float_curve_002.inputs[1])
	#reroute_021.Output -> combine_xyz_001.Y
	ducky.links.new(reroute_021.outputs[0], combine_xyz_001.inputs[1])
	#scene_time.Frame -> compare_001.A
	ducky.links.new(scene_time.outputs[1], compare_001.inputs[0])
	#scene_time.Frame -> math.Value
	ducky.links.new(scene_time.outputs[1], math.inputs[0])
	#float_curve_004.Value -> math_007.Value
	ducky.links.new(float_curve_004.outputs[0], math_007.inputs[1])
	#map_range_002.Result -> math_009.Value
	ducky.links.new(map_range_002.outputs[0], math_009.inputs[0])
	#compare_001.Result -> compare_002.A
	ducky.links.new(compare_001.outputs[0], compare_002.inputs[0])
	#reroute_018.Output -> switch.Switch
	ducky.links.new(reroute_018.outputs[0], switch.inputs[0])
	#reroute_012.Output -> switch.True
	ducky.links.new(reroute_012.outputs[0], switch.inputs[9])
	#reroute_033.Output -> map_range_002.Value
	ducky.links.new(reroute_033.outputs[0], map_range_002.inputs[0])
	#combine_xyz.Vector -> switch.False
	ducky.links.new(combine_xyz.outputs[0], switch.inputs[8])
	#scene_time.Frame -> math_006.Value
	ducky.links.new(scene_time.outputs[1], math_006.inputs[0])
	#float_curve_002.Value -> math_005.Value
	ducky.links.new(float_curve_002.outputs[0], math_005.inputs[1])
	#reroute_007.Output -> map_range.From Max
	ducky.links.new(reroute_007.outputs[0], map_range.inputs[2])
	#math_002.Value -> combine_xyz.Z
	ducky.links.new(math_002.outputs[0], combine_xyz.inputs[2])
	#math_003.Value -> map_range.Value
	ducky.links.new(math_003.outputs[0], map_range.inputs[0])
	#reroute_024.Output -> combine_xyz_001.Z
	ducky.links.new(reroute_024.outputs[0], combine_xyz_001.inputs[2])
	#scene_time.Frame -> math_001.Value
	ducky.links.new(scene_time.outputs[1], math_001.inputs[0])
	#reroute_030.Output -> switch_001.True
	ducky.links.new(reroute_030.outputs[0], switch_001.inputs[3])
	#math_008.Value -> float_curve_004.Value
	ducky.links.new(math_008.outputs[0], float_curve_004.inputs[1])
	#math.Value -> math_008.Value
	ducky.links.new(math.outputs[0], math_008.inputs[0])
	#reroute_028.Output -> map_range_001.Value
	ducky.links.new(reroute_028.outputs[0], map_range_001.inputs[0])
	#compare_002.Result -> switch_001.Switch
	ducky.links.new(compare_002.outputs[0], switch_001.inputs[0])
	#float_curve_001.Value -> math_003.Value
	ducky.links.new(float_curve_001.outputs[0], math_003.inputs[1])
	#scene_time.Frame -> compare.A
	ducky.links.new(scene_time.outputs[1], compare.inputs[0])
	#math_010.Value -> math_008.Value
	ducky.links.new(math_010.outputs[0], math_008.inputs[1])
	#switch.Output -> transform_geometry.Rotation
	ducky.links.new(switch.outputs[3], transform_geometry.inputs[2])
	#map_range.Result -> math_002.Value
	ducky.links.new(map_range.outputs[0], math_002.inputs[0])
	#map_range_001.Result -> math_004.Value
	ducky.links.new(map_range_001.outputs[0], math_004.inputs[0])
	#reroute_011.Output -> transform_geometry.Geometry
	ducky.links.new(reroute_011.outputs[0], transform_geometry.inputs[0])
	#transform_geometry.Geometry -> group_output.Geometry
	ducky.links.new(transform_geometry.outputs[0], group_output.inputs[0])
	#reroute_002.Output -> math_003.Value
	ducky.links.new(reroute_002.outputs[0], math_003.inputs[0])
	#reroute_001.Output -> math_001.Value
	ducky.links.new(reroute_001.outputs[0], math_001.inputs[1])
	#reroute.Output -> reroute_001.Input
	ducky.links.new(reroute.outputs[0], reroute_001.inputs[0])
	#reroute_003.Output -> reroute_002.Input
	ducky.links.new(reroute_003.outputs[0], reroute_002.inputs[0])
	#reroute.Output -> reroute_003.Input
	ducky.links.new(reroute.outputs[0], reroute_003.inputs[0])
	#reroute_008.Output -> compare.B
	ducky.links.new(reroute_008.outputs[0], compare.inputs[1])
	#reroute_009.Output -> reroute_008.Input
	ducky.links.new(reroute_009.outputs[0], reroute_008.inputs[0])
	#group_input.Start KeyFrame ZWindup -> map_range.From Min
	ducky.links.new(group_input.outputs[2], map_range.inputs[1])
	#math_001.Value -> float_curve_001.Value
	ducky.links.new(math_001.outputs[0], float_curve_001.inputs[1])
	#group_input.ZWindup Degrees -> map_range.To Max
	ducky.links.new(group_input.outputs[3], map_range.inputs[4])
	#reroute.Output -> reroute_004.Input
	ducky.links.new(reroute.outputs[0], reroute_004.inputs[0])
	#group_input.Geometry -> reroute_005.Input
	ducky.links.new(group_input.outputs[0], reroute_005.inputs[0])
	#reroute.Output -> reroute_006.Input
	ducky.links.new(reroute.outputs[0], reroute_006.inputs[0])
	#reroute_006.Output -> reroute_007.Input
	ducky.links.new(reroute_006.outputs[0], reroute_007.inputs[0])
	#reroute_004.Output -> reroute_009.Input
	ducky.links.new(reroute_004.outputs[0], reroute_009.inputs[0])
	#reroute_005.Output -> reroute_010.Input
	ducky.links.new(reroute_005.outputs[0], reroute_010.inputs[0])
	#reroute_010.Output -> reroute_011.Input
	ducky.links.new(reroute_010.outputs[0], reroute_011.inputs[0])
	#reroute_013.Output -> reroute_012.Input
	ducky.links.new(reroute_013.outputs[0], reroute_012.inputs[0])
	#reroute_014.Output -> reroute_013.Input
	ducky.links.new(reroute_014.outputs[0], reroute_013.inputs[0])
	#reroute_015.Output -> reroute_014.Input
	ducky.links.new(reroute_015.outputs[0], reroute_014.inputs[0])
	#combine_xyz_001.Vector -> reroute_015.Input
	ducky.links.new(combine_xyz_001.outputs[0], reroute_015.inputs[0])
	#compare.Result -> reroute_016.Input
	ducky.links.new(compare.outputs[0], reroute_016.inputs[0])
	#reroute_016.Output -> reroute_017.Input
	ducky.links.new(reroute_016.outputs[0], reroute_017.inputs[0])
	#reroute_017.Output -> reroute_018.Input
	ducky.links.new(reroute_017.outputs[0], reroute_018.inputs[0])
	#reroute_020.Output -> reroute_019.Input
	ducky.links.new(reroute_020.outputs[0], reroute_019.inputs[0])
	#switch_001.Output -> reroute_020.Input
	ducky.links.new(switch_001.outputs[0], reroute_020.inputs[0])
	#reroute_022.Output -> reroute_021.Input
	ducky.links.new(reroute_022.outputs[0], reroute_021.inputs[0])
	#reroute_019.Output -> reroute_022.Input
	ducky.links.new(reroute_019.outputs[0], reroute_022.inputs[0])
	#math_004.Value -> reroute_023.Input
	ducky.links.new(math_004.outputs[0], reroute_023.inputs[0])
	#reroute_023.Output -> reroute_024.Input
	ducky.links.new(reroute_023.outputs[0], reroute_024.inputs[0])
	#math_005.Value -> reroute_025.Input
	ducky.links.new(math_005.outputs[0], reroute_025.inputs[0])
	#reroute_025.Output -> reroute_026.Input
	ducky.links.new(reroute_025.outputs[0], reroute_026.inputs[0])
	#reroute_026.Output -> reroute_027.Input
	ducky.links.new(reroute_026.outputs[0], reroute_027.inputs[0])
	#reroute_027.Output -> reroute_028.Input
	ducky.links.new(reroute_027.outputs[0], reroute_028.inputs[0])
	#math_009.Value -> reroute_029.Input
	ducky.links.new(math_009.outputs[0], reroute_029.inputs[0])
	#reroute_031.Output -> reroute_030.Input
	ducky.links.new(reroute_031.outputs[0], reroute_030.inputs[0])
	#reroute_029.Output -> reroute_031.Input
	ducky.links.new(reroute_029.outputs[0], reroute_031.inputs[0])
	#math_007.Value -> reroute_032.Input
	ducky.links.new(math_007.outputs[0], reroute_032.inputs[0])
	#reroute_032.Output -> reroute_033.Input
	ducky.links.new(reroute_032.outputs[0], reroute_033.inputs[0])
	#group_input.End KeyFrame ZWindup -> reroute.Input
	ducky.links.new(group_input.outputs[1], reroute.inputs[0])
	#group_input.Start Keyframe ZSpin -> map_range_001.From Min
	ducky.links.new(group_input.outputs[4], map_range_001.inputs[1])
	#reroute_037.Output -> map_range_001.From Max
	ducky.links.new(reroute_037.outputs[0], map_range_001.inputs[2])
	#group_input.End Keyframe ZSpin -> reroute_034.Input
	ducky.links.new(group_input.outputs[5], reroute_034.inputs[0])
	#reroute_039.Output -> math_005.Value
	ducky.links.new(reroute_039.outputs[0], math_005.inputs[0])
	#reroute_036.Output -> math_006.Value
	ducky.links.new(reroute_036.outputs[0], math_006.inputs[1])
	#reroute_034.Output -> reroute_035.Input
	ducky.links.new(reroute_034.outputs[0], reroute_035.inputs[0])
	#reroute_035.Output -> reroute_036.Input
	ducky.links.new(reroute_035.outputs[0], reroute_036.inputs[0])
	#reroute_034.Output -> reroute_037.Input
	ducky.links.new(reroute_034.outputs[0], reroute_037.inputs[0])
	#reroute_034.Output -> reroute_038.Input
	ducky.links.new(reroute_034.outputs[0], reroute_038.inputs[0])
	#reroute_038.Output -> reroute_039.Input
	ducky.links.new(reroute_038.outputs[0], reroute_039.inputs[0])
	#group_input.ZSpin Degrees -> map_range_001.To Max
	ducky.links.new(group_input.outputs[6], map_range_001.inputs[4])
	#reroute_040.Output -> compare_001.B
	ducky.links.new(reroute_040.outputs[0], compare_001.inputs[1])
	#group_input.Start KF YSpin -> reroute_040.Input
	ducky.links.new(group_input.outputs[7], reroute_040.inputs[0])
	#reroute_040.Output -> map_range_002.From Min
	ducky.links.new(reroute_040.outputs[0], map_range_002.inputs[1])
	#reroute_040.Output -> math.Value
	ducky.links.new(reroute_040.outputs[0], math.inputs[1])
	#reroute_040.Output -> math_010.Value
	ducky.links.new(reroute_040.outputs[0], math_010.inputs[1])
	#reroute_041.Output -> map_range_002.From Max
	ducky.links.new(reroute_041.outputs[0], map_range_002.inputs[2])
	#group_input.End KF YSpin -> reroute_041.Input
	ducky.links.new(group_input.outputs[8], reroute_041.inputs[0])
	#reroute_041.Output -> compare_002.B
	ducky.links.new(reroute_041.outputs[0], compare_002.inputs[1])
	#reroute_041.Output -> math_007.Value
	ducky.links.new(reroute_041.outputs[0], math_007.inputs[0])
	#reroute_041.Output -> math_010.Value
	ducky.links.new(reroute_041.outputs[0], math_010.inputs[0])
	#group_input.YSpin degrees -> map_range_002.To Max
	ducky.links.new(group_input.outputs[9], map_range_002.inputs[4])
	return ducky



