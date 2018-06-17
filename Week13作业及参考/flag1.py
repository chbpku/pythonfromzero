import turtle  # 导入海龟制图模块
import random  # 导入随机模块

colors = ['blue', 'green', 'red', 'pink', 'brown', 'yellow', 'orange']
t = turtle.Turtle()  # 生成一个海龟，名字叫“t”
t.pensize(2)


# 随机颜色的用法：在需要用到颜色的地方写：
# random.choice(colors)

# 在下面开始写你的代码，以上的代码勿动
# =============

# 一个边长是n的三角形，填充颜色c
def triangle(n, c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(3):
        t.forward(n)
        t.right(120)
    t.end_fill()


# 一个边长是m,n的长方形，填充颜色c
def rectangle(m, n, c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(m)
        t.right(90)
        t.forward(n)
        t.right(90)
    t.end_fill()


t.left(90)
rectangle(300, 10, 'gray')
t.forward(50)
t.right(90)
t.forward(10)
t.left(90)

triangle(80, 'blue')
t.forward(80)

triangle(60, 'red')
t.forward(60)·

triangle(50, 'green')
t.forward(50)

triangle(40, 'brown')

# =============
# 你的代码结束，以下的代码勿动

t.hideturtle()  # 隐藏海龟
turtle.done()  # 海龟作图完成，等待欣赏
