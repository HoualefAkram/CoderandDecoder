import random

choice = ""
txt = ''
level = 0
seed = 1
while choice != "1" and choice != "2" and not 1 <= level <= 3:
    choice, txt, seed, level = input("1)Coder\n2)Decoder\nchoose :  "), input("enter your message : "), int(
        input("enter the seed : ")), int(input("enter the level (1-3) : "))


class Levels_coder:
    def __init__(self, t, s):
        self.text = t
        self.seed = s

    def level1(self):
        answer = []
        random.seed(self.seed)
        for i in self.text:
            answer.append(chr(ord(i) + random.randint(0, 3)))
        return answer

    def level2(self):
        answer = Levels_coder.level1(self)
        answer = list(map(lambda x: x + str(random.randint(0, 9)), answer))
        return answer

    def level3(self):
        answer = Levels_coder.level2(self)
        answer = list(map(lambda x: x + chr(random.randint(33, 47)), answer))
        return answer


class Levels_decoder:
    def __init__(self, t, s):
        self.text = t
        self.seed = s

    def level1(self):
        answer = list(self.text)
        random.seed(self.seed)
        answer = list(map(lambda x: chr(ord(x) - random.randint(0, 3)), answer))
        return answer

    def level2(self):
        answer = list(self.text)
        random.seed(self.seed)
        for i in range(1, int(len(answer) / 2) + 1):
            answer.pop(i)
            i *= 2
        answer = Levels_decoder(''.join(answer), self.seed).level1()
        return answer

    def level3(self):
        answer = list(self.text)
        random.seed(self.seed)
        for i in range(2, int(2 * int(len(answer)) / 3) + 1, 2):
            answer.pop(i)
        answer = Levels_decoder(''.join(answer), self.seed).level2()
        return answer


if choice == "1":
    match level:
        case 1:
            print(''.join(Levels_coder(txt, seed).level1()))
        case 2:
            print(''.join(Levels_coder(txt, seed).level2()))
        case 3:
            print(''.join(Levels_coder(txt, seed).level3()))

if choice == "2":
    match level:
        case 1:
            print(''.join(Levels_decoder(txt, seed).level1()))
        case 2:
            print(''.join(Levels_decoder(txt, seed).level2()))
        case 3:
            print(''.join(Levels_decoder(txt, seed).level3()))