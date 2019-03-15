class Candidate():
    def __init__(self,out,row_dad,col_dad,row,col,cost,prize_up_to):
        self.out=out;
        self.row_dad=row_dad
        self.col_dad=col_dad
        self.row=row
        self.col=col
        self.cost = cost
        self.prize_up_to=prize_up_to
