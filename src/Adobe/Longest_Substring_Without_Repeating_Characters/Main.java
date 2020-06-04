package Adobe.Longest_Substring_Without_Repeating_Characters;

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String args[]) {

        System.out.println(lengthOfLongestSubstring("abcabcdabab"));
        System.out.println(lengthOfLongestSubstring(" "));

    }

    public static int lengthOfLongestSubstring(String s) {

        int maxLen = 0;
        int localLen = 0;

        Map<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {

            if (map.containsKey(s.charAt(i))) {
                localLen = Math.max(localLen, map.get(s.charAt(i)));
            }
            maxLen = Math.max(maxLen, i + 1 - localLen);
            map.put(s.charAt(i), i + 1);

        }
        return maxLen;
    }

}
