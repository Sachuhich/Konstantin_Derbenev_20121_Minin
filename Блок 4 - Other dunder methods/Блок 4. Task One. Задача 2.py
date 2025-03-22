import random
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars=psw_chars
        self.min_length=min_length
        self.max_length=max_length

    def __call__(self):
        length = random.randint(self.min_length, self.max_length)
        d=[''.join(random.choice(self.psw_chars)) for i in range(length)]
        return ''.join(d)

rnd=RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for i in range(3)]
print(lst_pass)