class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """    
    def backtrack(params):
    if base_case_condition:
        save_result
        return

    for choice in choices:
        if violates_constraints:
            continue

        make_choice
        backtrack(updated_params)
        undo_choice  # Backtracking Step

        """
        res=[]
        n=len(nums)
        sol=[]
    # choices-all numers in nums
    # constraints- must be len of nums, no dup numbers
    #base case- pick number
    #backtrack step- pop last  numberadded, go back

        def backtracking(path):
            if len(path)==n:
                res.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtracking(path)
                path.pop()
            # we do not select
        backtracking([])

        return res
        