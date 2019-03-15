class Heatmap():
    def __init__(self,customer,motw,customers):
        self.customer=customer
        self.motw=motw
        self.customers=customers
        self.map=[[None for i in range(len(motw[0]))] for j in range(len(motw))]

