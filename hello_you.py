#!/usr/bin/env python3

def get_user_name():
    user_name = input("What is your name?\n")
    return user_name

def main():
    """ Hello, (name)! """
    name = get_user_name()
    print("Hello, "+ name +"!")

if __name__ == '__main__':
    main()
