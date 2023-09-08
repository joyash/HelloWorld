lst = ["kimmo", "janne", "mohammed", "luna"]
lst.append("hora")
"""for x in lst:
    print(x)"""
for xid, x in enumerate(lst):
    if(x != lst[-1]):
      print(f"{x} is having coffee with {lst[xid+1]}")