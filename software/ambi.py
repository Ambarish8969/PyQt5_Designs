# import os
# path="D:\PyQt5_Designs\project20.py"
# # path1=path.split("\ ")
# # print(path1)
# # print(path1[-1])
# spli=os.path.split(path)
# print(spli)
# print(spli[-1])
# taile=os.path.basename(spli[1])
# print(taile)
from pathlib import Path
path=Path("D:\PyQt5_Designs\Try100.py")
print(path.name)