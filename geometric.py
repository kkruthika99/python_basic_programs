def geometric(vals):
if len(vals)==0 or len(vals)==1:
return True
d=vals[1]/vals[0]
for i in range(0,len(vals)-1):
if (vals[i+1]/vals[i])!=d:
return False
return True
inp =list(input("Enter series to check").split(" "))
for i in range(0,len(inp)):
inp[i]=int(inp[i])
print(geometric(inp))
