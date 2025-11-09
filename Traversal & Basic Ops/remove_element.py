def removeElement(nums: List[int], val: int) -> int:
      w = 0
      for i in range(len(nums)):
          if nums[i] == val:
              pass
          else:
              nums[i], nums[w] = nums[w], nums[i]
              w += 1
      return w
