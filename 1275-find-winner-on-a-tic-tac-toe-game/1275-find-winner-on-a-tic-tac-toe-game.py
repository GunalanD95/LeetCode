class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        N = len(moves)

        rowsum = [0]* 3
        colsum = [0]* 3

        diagn1 = 0
        diang2 = 0

        for i,j in enumerate(moves):
            if i % 2 == 0:
                rowsum[moves[i][0]] += 1
                colsum[moves[i][1]] += 1

                # diaganol check
                if moves[i][0] == moves[i][1]:
                    diagn1 += 1

                if moves[i][0] == 2 - moves[i][1]:
                    diang2 += 1
            else:
                rowsum[moves[i][0]] -= 1
                colsum[moves[i][1]] -= 1
                # diaganol check
                if moves[i][0] == moves[i][1]:
                    diagn1 -= 1

                if moves[i][0] == 2 - moves[i][1]:
                    diang2 -= 1


        if (3 in rowsum ) or (3 in colsum) or \
           (diagn1 == 3) or (diang2 == 3):
               return "A"
            
        elif (-3 in rowsum ) or (-3 in colsum) or \
           (diagn1 == -3) or (diang2 == -3):
               return "B"
            
        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'
    
    