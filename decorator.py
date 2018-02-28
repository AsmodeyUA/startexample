
def decorator1(f):
    def g(*args, **kwargs):
        print("Here")
        print(args)
        print(kwargs)
        return f(*args, **kwargs)
    return g

@decorator1
def w_test(a,drrr):
    print("HHHH")
    return a


def main():
    print(w_test(7,drrr={"sxs":5}))
    return 0


if __name__ == "__main__":
    main()