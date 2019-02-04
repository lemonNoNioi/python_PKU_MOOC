class Student:
    def __init__(self, name, grade):
        self.name, self.grade = name, grade
    # 内置sort函数只引用<比较符来判断前后
    def __lt__(self, other):
        # 成绩比other高的，排在他前面
        return self.grade > other.grade
    # Student的易读字符串表示
    def __str__(self):
        return "(%s,%d)" % (self.name, self.grade)
    # Student的正式字符串表示，让他与易读表示相同
    __repr__ = __str__

# 构造一个列表对象
s = list()
# 添加Student对象到列表中
s.append(Student("Jack", 80))
s.append(Student("Jane", 75))
s.append(Student("Smith", 82))
s.append(Student("Cook", 90))
s.append(Student("Tom", 70))
print("Original:", s)

# 对列表进行排序，注意这是内置sort方法
s.sort()
# 查看结果，已经按照成绩排好序
print("Sorted:", s)
print(s[0]<s[1])