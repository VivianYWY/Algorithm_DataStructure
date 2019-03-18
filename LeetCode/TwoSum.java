""" Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // use Hashtable 
        Map<Integer, Integer> map = new HashMap<>();
        int complement = 0;
        int i = 0;
        for (; i < nums.length; i++){
            complement = target - nums[i];
            if (map.containsKey(complement)){
                break;  
            }
            map.put(nums[i], i);
        }
        return new int[] {map.get(complement), i};
    }
}
