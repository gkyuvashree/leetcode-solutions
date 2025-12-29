class Solution {
    public int findShortestSubArray(int[] nums) {
        int n = nums.length;
        int[] count = new int[50001];
        int[] first = new int[50001];

        int degree = 0, ans = n;

        for (int i = 0; i < n; i++) {
            if (count[nums[i]] == 0) first[nums[i]] = i;
            count[nums[i]]++;

            if (count[nums[i]] > degree) {
                degree = count[nums[i]];
                ans = i - first[nums[i]] + 1;
            } else if (count[nums[i]] == degree) {
                ans = Math.min(ans, i - first[nums[i]] + 1);
            }
        }

        return ans;
    }
}
