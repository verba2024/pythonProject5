import turtle
turtle.shape('turtle')
nums = [(0, 100, -25, 75), (50, 0), (50, 100, 50, 50, 25, 50, 25, 100), (100, 0),
        (100, 100, 75, 75), (150, 0), (150, 100, 125, 70), (200, 0),
        (200, 100, 250, 100, 250, 0, 200, 0), (300, 0), 
        (300, 100, 350, 100, 350, 0, 300, 0)]

for j in range(len(nums)):
    if j % 2 != 0:
        turtle.penup()
        for i in range(0, len(nums[j]) - 1, 2):
            turtle.goto(nums[j][i], nums[j][i + 1])
        turtle.down()
    else:
        for i in range(0, len(nums[j]) - 1, 2):
            turtle.goto(nums[j][i], nums[j][i + 1])