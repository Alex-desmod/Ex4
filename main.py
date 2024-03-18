import tools
def main():

    class MyError(Exception):
        pass

    def oops():
        raise MyError('Fuck you!')

    tools.safe(oops)


if __name__ == '__main__':
    main()


