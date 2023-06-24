# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 

 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""




class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        p1_h = 0
        p1_t = len(nums1) - 1
        p2_h = 0
        p2_t = len(nums2) - 1

        n_l = len(nums1) + len(nums2)
        if n_l % 2 == 0:
            #偶数个(剩中间两个数)
            nloop = n_l // 2 - 1
        else:
            #奇数个(剩中间一个数)
            nloop = n_l // 2
        for _ in range(nloop):
            if p1_t >= p1_h and p2_t >= p2_h:
                # 两个不为空
                min1 = nums1[p1_h]
                min2 = nums2[p2_h]
                max1 = nums1[p1_t]
                max2 = nums2[p2_t]

                if min1 <= min2:
                    p1_h += 1
                else:
                    p2_h += 1
                
                if max1 >= max2:
                    p1_t -= 1
                else:
                    p2_t -= 1
            # 其中一个列表空了，则直接为剩下的子列表中位数
            elif p1_t < p1_h and p2_t >= p2_h:
                nsl = p2_t - p2_h + 1
                mid = (p2_h + p2_t) // 2
                if nsl % 2 == 0:
                    #子列表剩偶数个元素
                    return (nums2[mid] + nums2[mid+1]) / 2.0
                else:
                    return nums2[mid]  
            elif p1_t >= p1_h and p2_t < p1_h:
                nsl = p1_t - p1_h + 1
                mid = (p1_t + p1_h) // 2
                if nsl % 2 == 0:
                    return (nums1[mid] + nums1[mid+1]) / 2.0
                else:
                    return nums1[mid]
        
        if n_l % 2 == 0:
            # 偶数个
            if p1_t >= p1_h and p2_t >= p2_h:
                #相等(偶数个)
                return (nums1[p1_h] + nums2[p2_h]) / 2.0     
            if p1_t >= p1_h and p2_t < p2_h:
                return (nums1[p1_t] + nums1[p1_h]) / 2.0
    
            if p1_t < p1_h and  p2_t >= p2_h:
                return (nums2[p2_h] + nums2[p2_t]) / 2.0
        else:
            if p1_t >= p1_h and p2_t < p2_h:
                return nums1[(p1_t + p1_h)//2]
    
            if p1_t < p1_h and  p2_t >= p2_h:
                return nums2[(p2_h + p2_t)//2]            
nums1 = [1,2,3]
nums2 = [4,5,6,7]
s = Solution()

r = s.findMedianSortedArrays(nums1, nums2)



