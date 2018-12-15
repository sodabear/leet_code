class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        int local = 0;
        int count = 0; 

        for (int i = 0; i< nums.length; i++) {
            if (nums[i] != 0) {
                count++;
                
            } else{
                local = Math.max(local, count);
                count = 0;
            }
        }
        local = Math.max(local,count);
        return local;
    }