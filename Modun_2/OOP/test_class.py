import turtle
def main():
    drawer = turtle.Turtle()

    # size_str = input('input size: \n')
    # assert size_str.isnumeric(), 'input so co ma ditcu m'

    # size_i   = int(size_str)

    for i in range(4):
        drawer.forward(100)
        drawer.left(90)

main()