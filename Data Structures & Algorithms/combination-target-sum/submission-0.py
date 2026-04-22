class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

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
        sol=[]
        def backtrack(path,index):
            if sum(path)==target:
                res.append(path[:])
                return
            for i in range(index,len(nums)):
                if (sum(path)+nums[i]) >target:
                      continue
                path.append(nums[i])
                backtrack(path,i)
                path.pop()
        backtrack([],0)
        return res





        
