import turtle  # 导入海龟制图模块
import random  # 导入随机模块

colors = ['blue', 'green', 'red', 'pink', 'brown', 'yellow', 'orange']
t = turtle.Turtle()  # 生成一个海龟，名字叫“t”
t.pensize(2)


# 随机颜色的用法：在需要用到颜色的地方写：
# random.choice(colors)

# 在下面开始写你的代码，以上的代码勿动
# =============

# 一个边长是n的正方形
def rectangle(n):
    for i in range(4):
        t.forward(n)
        t.right(90)


for i in range(10):
    t.penup()
    t.backward(i * 10)
    t.left(90)
    t.backward(i * 10)
    t.pendown()

    t.color(random.choice(colors))
    rectangle(i * 20)

    t.penup()
    t.forward(i * 10)
    t.right(90)
    t.forward(i * 10)
    t.pendown()

# =============
# 你的代码结束，以下的代码勿动

t.hideturtle()  # 隐藏海龟
turtle.done()  # 海龟作图完成，等待欣赏
