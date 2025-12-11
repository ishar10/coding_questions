class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+ len(nums2)
        flag = 'odd'
        if total%2 ==0:
            flag = 'even'
        if len(nums1)>len(nums2):
            t = nums1
            nums1 = nums2
            nums2 = t
        left = 0
        right = len(nums1)-1
        previous_mid = 'a'
        if nums1 ==[] or nums2 == []:
            final = nums1 +nums2
            if flag =='odd':
                return final[len(final)//2]/1
            else:
                return (final[len(final)//2] + final[(len(final)//2) -1])/2

        while(True):
            mid = (left+right)//2
            print("mid",mid, total//2)
            digits_left = (total//2) - (mid + 1)
            print(digits_left)
            last_from_nums2 = nums2[digits_left-1]
            last_from_nums1 = nums1[mid]
            if mid != previous_mid:
                previous_mid = mid
            else:
                # print(last_from_nums1)
                # print(nums2[digits_left])
                # print(last_from_nums2)
                # print(nums1[mid+1])
                while(digits_left <len(nums2) and last_from_nums1 > nums2[digits_left]):
                    digits_left +=1
                digits_left -=1
                # last_from_nums2 = nums2[digits_left-1]
                if last_from_nums1 > nums2[digits_left]:
                    print("greater")
                    if flag == "odd":
                        if digits_left == len(nums2)-1:
                            return nums2[digits_left]
                        else:
                            return last_from_nums1
                    else:
                   
                        if digits_left -1 >=0:
                            print("hereeee", digits_left)
                            return (min(last_from_nums1,nums2[digits_left-1])  + nums2[digits_left])/2
                        else:
                            return (last_from_nums1  + nums2[digits_left])/2
                        
                        if last_from_nums1
                        



                elif last_from_nums2 > nums1[mid+1]:
                    if flag == "odd":
                        return max(last_from_nums2, nums1[mid+1])
                    else:
                        if digits_left -1 >=0:
                            return (last_from_nums2 + max(nums1[mid+1], nums2[digits_left -1]))/2
                        else:
                            return (last_from_nums2 + nums1[mid+1])/2

            if (mid+1) <len(nums1) and digits_left < len(nums2):
                if last_from_nums1 <= nums2[digits_left] and last_from_nums2<= nums1[mid+1]:
                    if flag =='odd':
                        return min(nums2[digits_left], nums1[mid+1])
                    else:
                        final_left = max(last_from_nums1, last_from_nums2)
                        final_right = min(nums1[mid+1], nums2[digits_left])
                        return (final_left+ final_right)/2
                elif last_from_nums1 > nums2[digits_left]:
                    right = mid

                elif last_from_nums2 > nums1[mid+1]:
                    left = mid

            elif (mid+1) == len(nums1):
                if len(nums2)%2 ==0:
                    mid_value = nums2[len(nums2)//2]
                    if mid_value<= nums1[mid]:
                        return mid_value/1
                    else:
                        return max(nums2[(len(nums2)//2)-1],nums1[mid])/1
                else:
                    mid_value = nums2[len(nums2)//2]
                    print("here")
                    if len(nums2) ==1:
                        return (nums1[mid] + nums2[0])/2
                    if mid_value<= nums1[mid]:
                        return (mid_value + min(nums1[mid] , nums2[(len(nums2)//2)+1]))/2
                    else:
                        return (mid_value + max(nums1[mid] , nums2[(len(nums2)//2)-1]))/2