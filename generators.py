def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b
        if b>170:
            return 100

f = fibonacci()

counter = 0
print(next(f))
print(f.send(4))

for x in f:
    print(x, " ", end="")

def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        message = yield objects[count]
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1
x = infinite_looper("A string with some words")
print(dir(x))
print(range)
print(next(x))
print(x.send(10))
print(x.send(9))



expertises = ["Novice", "Beginner", "Intermediate", "Proficient", "Experienced", "Advanced"]
expertises_iterator = iter(expertises)
print(next(expertises_iterator))
print(next(expertises_iterator))
