def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        
        for i in range(len(nums)):
            # if elemwent is already in the dictionary & distance between indices is <= k
            if nums[i] in index_map and i - index_map[nums[i]] <= k:
                return True
            
            # update dictionary with current index of element
            index_map[nums[i]] = i
        #otherwise false        
        return False
