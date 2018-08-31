from random import randint


class RandomGenerator:

    def __init__(self):
        self.numCode = '''0123456789'''
        self.letterCode = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'''
        self.mixCode = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ123456789!@#%&()*"{}'''

    def nextNum(self, length):
        res = ''
        for i in range(length):
            index = randint(0, len(self.numCode) - 1)
            res += self.numCode[index]
        return res

    def nextLetter(self, length):
        res = ''
        for i in range(length):
            index = randint(0, len(self.letterCode) - 1)
            res += self.letterCode[index]
        return res

    def nextPwd(self, minLen=6, maxLen=16):
        randomLength = randint(minLen, maxLen)
        res = ''
        for i in range(randomLength):
            index = randint(0, len(self.mixCode) - 1)
            res += self.mixCode[index]
        return res


if __name__ == '__main__':
    generator = RandomGenerator()
    for i in range(100):
        print(generator.nextPwd())

    import os
    os.system('pause')
