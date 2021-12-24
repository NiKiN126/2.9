#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def clear_str(stri):
    res = ""
    for s in stri:
        if s in "()[]{}<>":
            res = res + s
    return res


# Проверка

def check_par(stri):
    if len(stri) == 0:
        return True
    else:
        f = stri[0]
        l = stri[-1]
        kf = "([{<".find(f)
        if kf == -1:
            return False
        if l == ")]}>"[kf]:
            return check_par(stri[1:len(stri) - 1])
        else:
            return False


def task(stri):
    return clear_str(clear_str(stri))

if __name__ == '__main__':

    print(check_par("( [ ) ]"))