# version code
from enum import Enum

version_code = '当前版本号：V0.3'

# app name
app_name = 'WIRING'

# update log
update_log = '''日期：2019年6月26日 
版本：V0.1

1.完成详细设计中的所有功能。
2.删除了避障操作。'''

if_block = '''IF condition THEN
'code
ELSE
'code
END IF\n'''

move_block = '''MOVES ROBOT  #{%s,%s,%s,0,0,0} ABS=%s\n'''

# 速度调节
speed_block = 'SYS.VORD=%s\n'

# 基础坐标系
xyz_base_block = 'CALL SETBASENUM(%s)\n'
# 工具坐标系
xyz_tool_block = 'CALL SETTOOLNUM(%s)\n'

# 输入
din_block = 'D_IN[%s] = %s\n'
# 输出
dout_block = 'D_OUT[%s] = %s\n'

# 延时
delay_block = "DELAY ROBOT %s\n"

# 参数
val_block = 'DIM %s AS LONG  = %d\n'
