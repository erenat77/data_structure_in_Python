from linear_data_str import Deque

#A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam.
#I would like to construct an algorithm to input a string of characters and check whether it is a palindrome


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

#---------------------------------------------
#-----------TEST------------------------------
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

