'''
T.C = O(N^2)
'''

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        board.reverse()
        def cordi(number):
            row=(number-1)//n
            col=(number-1)%n
            if row%2:
                col=n-1-col
            return [row,col]
    
        q=[]
        moves=0
        vis=[[0 for i in range(n)]for j in range(n)]
        q.append(1)
        
        while len(q)>0:
            size=len(q)
            while size>0:
                number=q.pop(0)
                
                for i in range(1,7):
                    if number+i>n*n:
                        break
                    x,y=cordi(number+i)
                    if board[x][y]==n*n or number+i==n*n:
                        return moves+1
                    #if board[x][y]==(n*n): ## agar board ka number or n^2 match kar jaye to return kar do .. yahi same conditon upar (or) operation k sath lagaya hua h 
                    #    return moves+1     ## kyoki ye number sidha game finish kar dega (moves+1 isliye return krna h kyoki uss number ko pick krne k liye b ek step lagega)
                    if vis[x][y]!=0:
                        continue
                    vis[x][y]=1
                    if board[x][y]!=-1:
                        q.append(board[x][y])
                    else:
                        q.append(number+i)
                        
                
                    
                size-=1
            moves+=1
                
        return -1