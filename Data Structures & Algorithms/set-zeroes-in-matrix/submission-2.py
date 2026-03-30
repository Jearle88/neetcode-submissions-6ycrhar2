class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    
        cols=len(matrix[0])
        rows=len(matrix)
       # def set_cols_x(matrix,col):
        # need to find a way to set row and col to 0 if 0
        # after we do that, we can itrarte mark
        """
        itrarte through by rows, check if ther is a zero via min
        if zero, find the column, mark the column with x's to end
        then when itrartting by rows, check if min0
        """
        
        for i in range(rows):
            has_x=False
            for j in range(cols):
                if 0 in matrix[i] and not has_x:
                    if matrix[i][j]==0:
                        matrix[i][j]="x"
                        tmp_col=j
                        for row in range(rows):
                            #print("truth/0set curr",matrix[row][tmp_col])
                            if matrix[row][tmp_col]==0:
                                continue 
                            if row<=i:
                                matrix[row][tmp_col]=0
                            else:
                                matrix[row][tmp_col]="x"
                        print("curr matrix", matrix)
                   
                    else:    
                        print("i, j set to 0",[i,j])
                        matrix[i][j]=0
                
                if matrix[i][j]=="x":
                    #print("curr change ", [i,j])
                    matrix[i][j]=0
                    has_x=True
                        

        return 