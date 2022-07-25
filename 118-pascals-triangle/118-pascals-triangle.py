class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mylist = [[1]]
        for row in range(numRows)[1:]:
            list1 = []
            for i in range(row+1):
                if i == 0:
                    list1.append(1)
                elif i == row:
                    list1.append(1)
                else:
                    list1.append(mylist[row-1][i-1] + mylist[row-1][i])
            mylist.append(list1)
        return mylist