import DataProcess as DP
import GenerateList as GL

file_list = ['奇迹的山.txt', '流行的云.txt']
# 生成一阶音高和节奏的矩阵
Info1 = DP.trans_1_order(file_list)

# 生成二阶音高和节奏的矩阵
Info2 = DP.trans_2_order(file_list)

# 生成一阶音高列表
Pitch_List1 = GL.list_generate_1(Info1.pitch, 100)

# 生成一阶节奏列表
Rhythm_List1 = [DP.dict_id_rhythm[i] for i in GL.list_generate_1(Info1.rhythm, 100)]

# 生成二阶音高列表
Pitch_List2 = GL.list_generate_2(Info2.pitch, 100, [])

# 生成二阶节奏列表
Rhythm_List2 = [DP.dict_id_rhythm[i] for i in GL.list_generate_2(Info2.rhythm, 100, [])]
