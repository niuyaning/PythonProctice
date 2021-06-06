def a():
    local = 1
    print(local)

if __name__ == "__main__":
    a()

global_b = 123

def b():
    print(global_b)

if __name__ == "__main__":
    b();


def out():
    global_a = 1
    def sa():
        print(global_a)
        return global_a
    return sa()

out()