"""
# Display two messages
print('''Welcome to python''')
print("Python is fun")
"""
"""
import turtle

turtle.showturtle()
turtle.write("Welcome to TGU!")
turtle.forward(100)
turtle.right(90)
turtle.color("blue")
turtle.forward(50)
turtle.right(90)
turtle.color("green")
turtle.forward(80)
turtle.right(45)
turtle.forward(80)
turtle.done()
"""
"""
import turtle

turtle.goto(0, 50)
turtle.penup()
turtle.goto(50, -50)
turtle.pendown()
turtle.color("red")
turtle.circle(50)

turtle.done()
"""
""" r = eval(input("请输入半径："))
area = r * r * 3.14159
print("面积为",area)
"""
""" x, y, z = eval(input("请输入3个数以逗号分隔:"))
print(x, y, z) """
""" a = int(3*3)
print(a) """

""" purchaseAmount = eval(input("Enter purchase amount:"))
tax = purchaseAmount * 0.06
print("Sales tax is", int(tax * 100) / 100.0)
"""

""" import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSecond = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHour = totalHours % 24

print("Current time is", currentHour,":", currentMinute, ":", currentSecond, "GMT")
"""

""" import math

print(round(math.degrees(math.pi))) """

""" import turtle

turtle.write("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")
turtle.done() """

print("Welcome","to",sep="you")
