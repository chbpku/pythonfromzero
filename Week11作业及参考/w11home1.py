import turtle  # 导入海龟制图模块
import random  # 导入随机模块

colors = ['blue', 'green', 'red', 'pink', 'brown', 'yellow', 'orange']
t = turtle.Turtle()  # 生成一个海龟，名字叫“t”
t.pensize(2)


# 随机颜色的用法：在需要用到颜色的地方写：
# random.choice(colors)

# 在下面开始写你的代码，以上的代码勿动
# =============

# 一个边长是m,n的长方形
def rectangle(m, n):
    for i in range(2):
        t.forward(m)
        t.right(90)
        t.forward(n)
        t.right(90)


def circle(n):
    for i in range(36):
        t.forward(n)
        t.right(10)


def triangle(n):
    for i in range(3):
        t.forward(n)
        t.right(120)


t.penup()
t.goto(100, 200)
t.pendown()
circle(20)

t.penup()
t.goto(60, 140)
t.pendown()
t.right(60)
triangle(50)

t.penup()
t.goto(150, 140)
t.pendown()
triangle(50)

t.penup()
t.goto(50, 50)
t.pendown()
t.left(60)
rectangle(100, 30)

# =============
# 你的代码结束，以下的代码勿动

t.hideturtle()  # 隐藏海龟
turtle.done()  # 海龟作图完成，等待欣赏
