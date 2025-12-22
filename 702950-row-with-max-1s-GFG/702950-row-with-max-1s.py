class Solution:
    def rowWithMax1s(self, arr):
        rows = len(arr)
        cols = len(arr[0])
        
        max_row_index = -1
        col = cols - 1  # Start at the top-right corner
        
        # Iterate through rows
        for r in range(rows):
            # Move left as long as we encounter 1s
            # We only check arr[r][col] because we only care if this row
            # has MORE 1s than the previous best.
            while col >= 0 and arr[r][col] == 1:
                max_row_index = r
                col -= 1
            
            # OPTIMIZATION: If we've reached the far left (index -1),
            # this row (or a previous one) is all 1s. 
            # We can't beat "all 1s", so stop searching.
            if col < 0:
                break
                
        return max_row_index