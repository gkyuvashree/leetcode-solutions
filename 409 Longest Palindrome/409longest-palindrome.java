class Solution {
    public int longestPalindrome(String s) {
        int[] freq = new int[128];
        int length = 0;

        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i);
            freq[c]++;
            if ((freq[c] & 1) == 0) length += 2;
        }

        return length < s.length() ? length + 1 : length;
    }
}
