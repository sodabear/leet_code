class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        s = set()
        for x in board:
            
            for y in x:
                #print("this is y",y)
                if y != '.':
                    print(y)
                    if int(y) < 0 or int(y) > 9:
                        print(y)
                        return False
                    elif y not in s:
                        #print("222")
                        s.add(y)
                    else:
                        #print("1111")
                        return False
            s = set()
            
        #print("2")     
        s = set()
        for x in range(9):
            for y in range(9):
                 if board[y][x]  != '.':
                    if int(board[y][x]) >9 or int(board[y][x]) <0:
                        return False 
                    elif board[y][x]  not in s:
                        s.add(board[y][x])
                    else:
                        return False
            s = set()
        #print("3")    
        s = set() 
        for x in [0,3,6]:
            for y in [0,3,6]:
                for i in range(3):
                    for j in range(3):
                        if board[x+i][y+j] != '.':
                            if int(board[x+i][y+j]) > 9 or int(board[x+i][y+j]) < 0:
                                return False 
                            elif board[x+i][y+j] not in s:
                                s.add(board[x+i][y+j])
                            else:
                                return False 
                s = set()            
        return True    
        
            
