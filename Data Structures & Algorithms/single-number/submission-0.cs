public class Solution {
    public int SingleNumber(int[] nums) {
        int mask = 0;
        foreach (int num in nums) {
            mask ^= num;
        }
        return mask;
    }
}
