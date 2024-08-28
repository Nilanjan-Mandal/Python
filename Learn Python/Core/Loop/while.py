coin = 0
while coin <= 5:
    print("You Have {0} Coin".format(coin))
    coin = coin + 1
print("Good Bye!")

# Using Break Statement
while True:
    name = input("Please write your name: ")
    if name == 'Nilanjan':
        break
print("Hey {}".format(name))

# Using Break & Contineous Statement
while True:
    name1 = input("Please write your name: ")
    if name != 'Nilanjan':
        continue
    pwd = input("Please enter the password")
    if pwd == 'admin':
        break
print("Hey {} welcome to the vlog".format(name1))