class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> ban = new HashSet<>();
        for (String b : banned) ban.add(b.toLowerCase());

        paragraph = paragraph.toLowerCase().replaceAll("[^a-z]", " ");
        String[] words = paragraph.split("\\s+");

        Map<String, Integer> map = new HashMap<>();
        String ans = "";
        int max = 0;

        for (String w : words) {
            if (w.length() == 0 || ban.contains(w)) continue;
            map.put(w, map.getOrDefault(w, 0) + 1);
            if (map.get(w) > max) {
                max = map.get(w);
                ans = w;
            }
        }
        return ans;
    }
}