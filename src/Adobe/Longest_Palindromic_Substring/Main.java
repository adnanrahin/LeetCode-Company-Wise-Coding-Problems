package Adobe.Longest_Palindromic_Substring;

public class Main {

    public static void main(String args[]) {

    }

    public static String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";

        int start = 0;
        int end = 0;
        for (int i = 0; i < s.length(); i++) {
            int maxLen = Math.max(palindromeLen(s, i, i), palindromeLen(s, i, i + 1));
            if (maxLen > end - start) {
                start = i - (maxLen - 1) / 2;
                end = i + (maxLen) / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    public static int palindromeLen(String s, int i, int j) {
        while (i >= 0 && j < s.length() && s.charAt(i) == s.charAt(j)) {
            i--;
            j++;
        }
        return j - 1 - i;
    }

}
