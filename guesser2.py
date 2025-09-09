import random
import time
var = random.random(1, 10)
print("Pick a number 1-10!")
if num == var:
  print("Brilliant!")
  time.sleep(10)
else:
  print("Wrong! the answer was," + var)
