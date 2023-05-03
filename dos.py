import requests
import random
import string

print("はじめマッスルうほうほ^^♪")
while True:
    
    num = random.randint(0, 10000)
    def res(num):
        for i in range(num):
            q = ""
            r = string.ascii_letters + string.digits
            q = q + r
        return q
    a = res(num)
    requests.post("ウェブのURL", a)
