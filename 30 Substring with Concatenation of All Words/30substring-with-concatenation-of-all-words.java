import java.util.*;
class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s.length() == 0 || words.length == 0) {
            return result;
        }
        int wordLength = words[0].length();
        int wordCount = words.length;
        int totalLength = wordLength * wordCount;
        Map<String, Integer> wordMap = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            String w = words[i];
            if (wordMap.containsKey(w)) {
                wordMap.put(w, wordMap.get(w) + 1);
            } else {
                wordMap.put(w, 1);
            }
        }
        for (int start = 0; start < wordLength; start++) {
            int left = start;
            int count = 0;
            Map<String, Integer> windowMap = new HashMap<>();
            for (int right = start; right + wordLength <= s.length(); right += wordLength) {
                String word = s.substring(right, right + wordLength);
                if (wordMap.containsKey(word)) {
                    if (windowMap.containsKey(word)) {
                        windowMap.put(word, windowMap.get(word) + 1);
                    } else {
                        windowMap.put(word, 1);
                    }
                    count++;
                    while (windowMap.get(word) > wordMap.get(word)) {
                        String leftWord = s.substring(left, left + wordLength);
                        windowMap.put(leftWord, windowMap.get(leftWord) - 1);
                        left += wordLength;
                        count--;
                    }
                    if (count == wordCount) {
                        result.add(left);
                    }
                } 
                else {
                    windowMap.clear();
                    count = 0;
                    left = right + wordLength;
                }
            }
        }
        return result;
    }
}
