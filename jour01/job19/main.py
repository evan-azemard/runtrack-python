def draw_rectangle(width, height):
    x = '-' * width
    y = ' ' * width

    print('|{}|'.format(x))


    for i in range(2, height):
        print('|{}|'.format(y))
        print('|{}|'.format(x))

draw_rectangle(10, 3)