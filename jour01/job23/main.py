def draw_triangle(width):
    y = "\ "
    z = "_" * width


    for i in range(1, width):
        c = " " * i
        x = '{}/'.format(" " * 1)

        print(x,c,y)
    for i in range(0, 1):
        print("/",z,"\ ")


draw_triangle(5)
