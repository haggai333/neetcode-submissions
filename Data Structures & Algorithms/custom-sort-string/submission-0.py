from functools import cmp_to_key
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def comp(x,y):
            if x in orders and y  in orders:
                return orders[x]-orders[y]
            else:
                if x in orders:
                    return -1
                else:
                    return 1
        orders={}
        for i in range(len(order)):
            if order[i] not in orders:
                orders[order[i]]=i
        temp=[]
        for i in s:
            temp.append(i)
        temp.sort(key=cmp_to_key(comp))
        return "".join(temp)