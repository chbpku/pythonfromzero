import turtle  # 导入海龟制图模块
import random  # 导入随机模块

colors = ['blue', 'green', 'red', 'pink', 'brown', 'yellow', 'orange']
t = turtle.Turtle()  # 生成一个海龟，名字叫“t”
t.pensize(2)


# 随机颜色的用法：在需要用到颜色的地方写：
# random.choice(colors)

# 在下面开始写你的代码，以上的代码勿动
# =============

# 一个边长是n的三角形
def triangle(n):
    for i in range(3):
        t.forward(n)
        t.right(120)


# 一个边长是m,n的长方形
def rectangle(m, n):
    for i in range(2):
        t.forward(m)
        t.right(90)
        t.forward(n)
        t.right(90)


t.left(90)
rectangle(50, 20)
t.forward(50)
t.right(90)
t.forward(10)
t.left(90)

t.forward(80)
t.right(150)
triangle(100)
t.left(150)

t.forward(20)
t.right(150)
triangle(80)
t.left(150)

t.forward(20)
t.right(150)
triangle(60)
t.left(150)

t.forward(20)
t.right(150)
triangle(40)
t.left(150)
# =============
# 你的代码结束，以下的代码勿动

t.hideturtle()  # 隐藏海龟
turtle.done()  # 海龟作图完成，等待欣赏
