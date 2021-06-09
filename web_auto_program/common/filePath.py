import os

'''专门用来获取路径的值'''

path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 获取根目录

print(path + '/report/result.html')