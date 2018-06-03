import turtle  # 导入海龟制图模块
import random  # 导入随机模块

colors = ['blue', 'green', 'red', 'pink', 'brown', 'yellow', 'orange']
t = turtle.Turtle()  # 生成一个海龟，名字叫“t”
t.pensize(2)


# 开始写你的代码
# =============

def triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)


def rectangle():
    for i in range(4):
        t.forward(20)
        t.right(90)


t.left(90)
for i in range(10):
    t.color(random.choice(colors))
    rectangle()
    t.penup()
    t.forward(30)
    t.pendown()

# =============
# 代码结束

t.hideturtle()  # 隐藏海):龟
turtle.done()  # 海龟作图完成，等待欣赏
