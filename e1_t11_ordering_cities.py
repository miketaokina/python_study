'''
Task 11: Ordering Cities

In task 6 you ordered three integers in descending order. In this task we want you to ask for three cities instead 
(that is, three strings) and that you sort them alphabetically. Again, you are not allowed to use lists or similar 
to solve the task. See below for an example execution:

Enter the name of the first city:  Växjö
Enter the name of the second city:  Nybro
Enter the name of the third city:  Kalmar
The cities in alphabetical order are: Kalmar, Nybro, Växjö
'''

# Code Starts:

city1 = input("Enter the name of the first city: ")
city2 = input("Enter the name of the second city: ")
city3 = input("Enter the name of the third city: ")

if city1 <= city2 and city2 <= city3:
    print(f"The cities in alphabetical order are: {city1}, {city2}, {city3}")
elif city1 <= city3 and city3 <= city2:
    print(f"The cities in alphabetical order are: {city1}, {city3}, {city2}")
elif city2 <= city1 and city1 <= city3:
    print(f"The cities in alphabetical order are: {city2}, {city1}, {city3}")
elif city2 <= city3 and city3 <= city1:
    print(f"The cities in alphabetical order are: {city2}, {city3}, {city1}")
elif city3 <= city1 and city1 <= city2:
    print(f"The cities in alphabetical order are: {city3}, {city1}, {city2}")
else:
    print(f"The cities in alphabetical order are: {city3}, {city2}, {city1}")
    
# Second solution: 

city1 = input("Enter the name of the first city: ")
city2 = input("Enter the name of the second city: ")
city3 = input("Enter the name of the third city: ")

# 不使用列表，通过两两比较和交换位置来进行排序
# 1. 确保 city1 小于等于 city2
if city1 > city2:
    city1, city2 = city2, city1

# 2. 确保 city2 小于等于 city3（经过这步，最大的城市一定被排到了最后，即 city3）
if city2 > city3:
    city2, city3 = city3, city2

# 3. 再次比较 city1 和 city2，确保前两个也按顺序排列
if city1 > city2:
    city1, city2 = city2, city1

# 输出结果
print(f"The cities in alphabetical order are: {city1}, {city2}, {city3}")

# Third solution:

city1 = input("Enter the name of the first city: ")
city2 = input("Enter the name of the second city: ")
city3 = input("Enter the name of the third city: ")

# 运用 and 组合条件，直接定位到需要调整位置的 5 种特定状态
if city1 <= city3 and city3 <= city2:
    # 顺序是 1-3-2
    city2, city3 = city3, city2
elif city2 <= city1 and city1 <= city3:
    # 顺序是 2-1-3
    city1, city2 = city2, city1
elif city2 <= city3 and city3 <= city1:
    # 顺序是 2-3-1
    city1, city2, city3 = city2, city3, city1
elif city3 <= city1 and city1 <= city2:
    # 顺序是 3-1-2
    city1, city2, city3 = city3, city1, city2
elif city3 <= city2 and city2 <= city1:
    # 顺序是 3-2-1
    city1, city3 = city3, city1

# 为什么不需要 else 和 pass？
# 如果顺序一开始就是完美的 1-2-3（即 city1 <= city2 and city2 <= city3），
# 上面所有的判断都会是 False。程序会自动跳过所有分支，直接来到最后的 print，
# 从而优雅地省去了 else 和 pass。

print(f"The cities in alphabetical order are: {city1}, {city2}, {city3}")