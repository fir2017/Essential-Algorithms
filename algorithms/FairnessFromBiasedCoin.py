import random

def BiasedCoin():
    number = random.randint(1,4)
    if number ==3:
        return "tails"
    else:
        return "heads"

def fairCoin(BiasedCoin):
      coin1, coin2 = BiasedCoin(), BiasedCoin()
      if coin1 == "heads" and coin2 == "tails":
          return "heads"
      elif coin1 == "tails" and coin2 == "heads":
          return "tails"
      else:
          return fairCoin(BiasedCoin)

# test
# list_ = []
# for i in range(10):
#     i = fairCoin(BiasedCoin)
#     list_.append(i)
#
#
# print fairCoin(BiasedCoin)
# print list_
