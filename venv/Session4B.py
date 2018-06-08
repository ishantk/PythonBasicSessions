import sys

def main():
    print("This is Awesome")

    for n in sys.argv:
        print(n)

    print(type(sys.argv))


if __name__ == "__main__":
    main()
