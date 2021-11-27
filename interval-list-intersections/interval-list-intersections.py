class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ia = 0
        ib = 0
        answer = []
        
        while ia < len(firstList) and ib < len(secondList):
            fast = max(firstList[ia][0], secondList[ib][0])
            late = min(firstList[ia][1], secondList[ib][1])
            
            if fast <= late:
                answer.append([fast, late])
                
            if firstList[ia][1] < secondList[ib][1]:
                ia += 1
            else:
                ib += 1
        
        return answer