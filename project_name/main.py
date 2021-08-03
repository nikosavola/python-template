def hello_world(x='') -> str:
    hello = "Hello world, " + x
    print(hello)
    return hello


if __name__ == '__main__':
    hello_world('Niko')
