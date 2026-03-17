def reverse_lookup(data,target):
   results=[]
   for k,v in data.items():
       if v==target:
           results.append(k)
   return results
my_dict={"sai":2,"chinni":'A3','jagan':'J1'}
print(reverse_lookup(my_dict,'J1'))
