#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3
# -*- coding: utf-8 -*-

# 文件操作
# fil = open("./test_file.txt", "r", encoding="utf-8")
# print(fil.read())
# fil.close()

# with open("./test_file.txt") as fil:
#   while True:
#     line = fil.readline()
#     print(line)
#     if not line:
#       break

# fil = open("./test_file.txt").readlines()
# for line in fil:
#   print(line)

# 复制
# import shutil
# shutil.copy("./test_file.txt", "./test_file_copy.txt")

# 写入
# import io
# io.open("./test_file_copy.txt", "w",encoding="utf-8").write("666\n111".decode("utf-8"))
# io.open("./test_file_copy.txt", "a",encoding="utf-8").write("\nsadasd\n111".decode("utf-8"))

# 正则匹配
import re
line = "Cats are smarter than dogs"
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
print(searchObj.group(1))
print(searchObj.group(2))