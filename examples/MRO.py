# class First(object):
#     def __init__(self):
#         super(First, self).__init__()
#         print("first")

# class Second(object):
#     def __init__(self):
#         super(Second, self).__init__()
#         print("second")

# class Third(First, Second):
#     def __init__(self):
#         super(Third, self).__init__()
#         print("thats it")

# x = Third()

class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")

class Second(First):
    def __init__(self):
        super(Second, self).__init__()
        print("second")

class Third(First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")

class Forth(Second, Third):
    def __init__(self):
        super(Forth, self).__init__()
        print("that's it")

x = Forth()