def greater(a,b):
  if a>b:
    return 'a is greater'
  elif b>a:
    return 'b is greater'
  else:
    return 'both are equal'
x=int(input())
y=int(input())
c=greater(x,y)
print(c)

def sum1(a,b):
  return a+b
  