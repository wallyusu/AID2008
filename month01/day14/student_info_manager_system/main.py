# 主模块不会自动生成PYC文件
# 所以主模块代码应该最少

# 入口
from usl import StudentView

view = StudentView()
view.main()