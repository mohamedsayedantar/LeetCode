class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mylist = [1]
        for row in range(rowIndex+1)[1:]:
            list1 = []
            for i in range(row+1):
                if i == 0:
                    list1.append(1)
                elif i == row:
                    list1.append(1)
                else:
                    list1.append(mylist[i-1] + mylist[i])
            mylist = list1
        return mylist