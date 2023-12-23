#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fun1(a):
    x = a * 3

    def fun2(b):
        nonlocal x
        return b + x

    return fun2


if __name__ == "__main__":
    test_fun = fun1(4)
    test_fun(7)
    print(test_fun)



