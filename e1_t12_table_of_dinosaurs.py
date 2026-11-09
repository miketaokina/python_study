'''
Task 12: Table of Dinosaurs

Millions of years ago, dinosaurs roamed the Earth! In this exercise, you will create a justified table like the one below, where there is space for the name, length and weight of five dinosaurs. Notice that length is centred and the weight is right justified. Use f-strings to format the table, that is -- use the string formatting discussed in chapters 4.8.6 and 4.8.7 and do not just add spaces or escape sequences.

| Dinosaur             | Length (m) |  Weight (tons) |
---------------------------------------------------
| Tyrannosaurus Rex    |    12.0    |          9.000 |
| Velociraptor         |    1.8     |          0.015 |
| Triceratops          |    9.0     |          6.800 |
| Stegosaurus          |    9.0     |          5.500 |
| Brachiosaurus        |    30.0    |         56.000 |
'''

# Code Starts:

# Need to be figured out!!!

# Second solution: 

# 将恐龙的数据存储在一个列表中，每个元素是一个元组 (名字, 长度, 重量)
dinosaurs = [
    ("Tyrannosaurus Rex", 12.0, 9.000),
    ("Velociraptor", 1.8, 0.015),
    ("Triceratops", 9.0, 6.800),
    ("Stegosaurus", 9.0, 5.500),
    ("Brachiosaurus", 30.0, 56.000)
]

# 1. 打印表头，使用 f-string 定义列宽和对齐方式
# <20 表示左对齐占20字符，^10 表示居中占10字符，>14 表示右对齐占14字符
header = f"| {'Dinosaur':<20} | {'Length (m)':^10} | {'Weight (tons)':>14} |"
print(header)

# 2. 打印分隔线，长度与表头保持一致
print("-" * len(header))

# 3. 遍历数据并打印每一行
for name, length, weight in dinosaurs:
    # .1f 限制长度保留1位小数，.3f 限制重量保留3位小数，并分别对齐
    print(f"| {name:<20} | {length:^10.1f} | {weight:>14.3f} |")