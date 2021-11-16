# generate a password with length "passlen" with no duplicate characters 
#change "passlen" if you need more or less characters in your password 
import random

s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p = "".join(random.sample(s,passlen))
print (p)
