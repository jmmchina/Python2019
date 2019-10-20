# def devi_num(num1, num2):
#     result = num1 * num2
#     return result

# print(devi_num(2, 8))

# def def_class():
#     num = int(input('请输入成绩： \n'))
#     if num >100:
#         print('请输入正确数值')
#         result = 'error'
#     elif 90 <= num <= 100:
#         result = 'A'
#     elif 80 <= num < 90:
#         result = 'B'
#     elif 70 <= num < 80:
#         result = 'C'
#     elif 60 <= num < 70:
#         result = 'D'
#     else:
#         result = 'F'
#     return result

# print(def_class())

# def count_coins(sum_num):
#     coin_lists = [1, 0.5, 0.1]
#     print(str(sum_num) + '元换算需要： \n')
#     for coin_list in coin_lists:
#         coin_num = sum_num // coin_list
#         if  coin_num > 0:
#             print(str(int(coin_num)) + ' 个 ' + str(float(coin_list)) + '面值的硬币')
#             sum_num = sum_num % coin_list

# count_coins(float(input('请输入想换算的金额：')))

# name_list = []
# while True:
#     name = input('请输入姓名： \n')
#     if name == 'q':
#         break
#     elif ',' in name:
#         name_list.append(name)
#     else:
#         print('请按正确格式输入')

# name_list.sort()
# for name in name_list:
#     print(name)

# f_temp = float(input('请输入华氏温度： \n'))
# c_temp = (f_temp - 32) / 1.8
# print(c_temp)

# r = float(input('请输入半径： '))
# zoucang = 2 * 3.14 *r
# size = 3.14 * r**2
# print('半径 ', r, ' 的周长是 ', zoucang, '面积是 ', size)

# year = int(input('请输入年份： '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('这是闰年')
# else:
#     print('这不是闰年')

# value = float(input('请输入长度： '))
# unit = input('请输入单位（inch \ cm)： ')
# if unit == 'inch':
#     print(value, ' 英寸等于 ', value * 2.54, '厘米')
# elif unit == 'cm':
#     print(value, ' 厘米等于 ', value / 2.54, '英寸')
# else:
#     print('请输入正确的单位')

trig_lines = []
for i in range(1,4):
    trig_lines.append(float(input('请输入第'+str(i)+'条边的长度： ')))

long_line = trig_lines.pop(max(trig_lines))
if long_line <= trig_lines[0] + trig_lines[1]:
    print('请输入正确的边长')
else:
    print(long_line + trig_lines[0] + trig_lines[1])