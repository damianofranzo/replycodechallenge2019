import heatmap as hm
import queue
import candidate

def djikstra(customers,motw):
    heatmaps=[]
    for custom in customers:
        heatmap=hm.Heatmap(custom,motw,customers)
        heatmaps.append(heatmap)

        explore(heatmap)
    #for i in range (len(heatmap.map)):
     #   for el in heatmap.map[i]:
      #      print (el.prize_up_to,)
       # print()
    return heatmaps



def explore(heatmap):

    customer_coordinates=[(c.row,c.col) for c in heatmap.customers]
    to_visit=queue.Queue()
    row=heatmap.customer.row
    col=heatmap.customer.col
    cand=candidate.Candidate(False,None,None,row,col,heatmap.motw[row][col].cost,heatmap.customer.reward)
    to_visit.put(cand)
    heatmap.map[row][col]=cand

    while not to_visit.empty():
        cand=to_visit.get()

        for i in range (4):
            if i == 0 :
                new_row=cand.row - 1
                new_col=cand.col
                if new_row < 0 :
                    continue

            if i == 1:
                new_row = cand.row + 1
                new_col = cand.col
                if new_row >= len(heatmap.motw) :
                    continue
            if i == 2:
                new_row = cand.row
                new_col = cand.col - 1
                if new_col < 0 :
                    continue

            if i == 3:
                new_row = cand.row
                new_col = cand.col + 1
                if new_col >= len(heatmap.motw[0]):
                    continue

            if heatmap.map[new_row][new_col] == None:
                if not heatmap.motw[new_row][new_col].walkable:
                    cand_sverg = candidate.Candidate(True, cand.row, cand.col, new_row, new_col,heatmap.motw[new_row][new_col].cost, -float('inf'))
                    heatmap.map[new_row][new_col] = cand_sverg
                    continue

                cand_sverg=candidate.Candidate(False,cand.row,cand.col,new_row,new_col,heatmap.motw[new_row][new_col].cost,cand.prize_up_to-cand.cost)
                heatmap.map[new_row][new_col]= cand_sverg
                to_visit.put(cand_sverg)
            elif heatmap.map[new_row][new_col].out:
                continue
            else:
                our_prize_up_to=cand.prize_up_to-cand.cost
                if our_prize_up_to > heatmap.map[new_row][new_col].prize_up_to:
                    heatmap.map[new_row][new_col].prize_up_to=our_prize_up_to
                    heatmap.map[new_row][new_col].row_dad=cand.row
                    heatmap.map[new_row][new_col].col_dad=cand.col


    for (row,col) in customer_coordinates:
        heatmap.map[row][col].prize_up_to= -float('inf')
    for i in range(len(heatmap.map)):
        for j in range(len(heatmap.map[0])):
            if heatmap.map[i][j] is None:
                heatmap.map[i][j]=candidate.Candidate(True, i, j, -1, -1,heatmap.motw[i][j].cost, -float('inf'))



