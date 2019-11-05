l = [1,2,5,4,8,9,87,9,9,6,4,5]

# recursive solution
def rev(l):
  if len(l)<=1 : return l
  else: return [l[-1]] + rev(l[:-1])
  
rev(l)

#easy solution
print(l[::-1])
