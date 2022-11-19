# -*- coding: utf-8 -*-

"""
求最大子数组和
int MaxSubSum(int arr[],int len)  
{  
    int i;  
    int MaxSum = 0;  
    int ThisSum= 0;  
    for(i=0;i<len;i++)  
    {  
        ThisSum+= arr[i];  
        if(ThisSum > MaxSum)  
            MaxSum = ThisSum;  
        /*如果累加和出现小于0的情况，  
           则和最大的子序列肯定不可能包含前面的元素，  
           这时将累加和置0，从下个元素重新开始累加  */
        else if(ThisSum< 0)  
            ThisSum= 0;  
    }  
    return MaxSum;  
}
"""

def max_sub_sum(arr):
    i = max_sum = this_sum = 0
    while i < len(arr):
        this_sum += arr[i]
        if this_sum > max_sum:
            max_sum = this_sum
        else:
            if this_sum < 0:
                this_sum = 0
        i += 1
    return max_sum

print max_sub_sum([1, 2, -3, -1, 1])



def reverse(x):
    if x>=0:
        res = int(str(x)[::-1])
    else:
        res = int('-' + str(x)[:0:-1])
    print res

reverse(-1230)