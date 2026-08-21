public class Solution {
    public int HammingWeight(uint n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (1 << i)) > 0) {
                result++;
            }
        }
        return result;
    }
}
