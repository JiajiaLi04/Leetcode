public class q5_LongestPalindromicSubstring {
    // 1. reverse string S to S' and find the longest substring that
    public static String longestPalindrome(String s) {
        //String new_s = s;
        StringBuilder new_s = new StringBuilder(s); 
        for (int i = 0; i < s.length(); i++){
            new_s.setCharAt((s.length()-i-1),s.charAt(i));
        }
        String reversed_s = new_s.toString();

        for (int i =0; i<s.length(); i++){
            //int j = i;
            //String sub_s = s.substring(i,j);

        }

        return reversed_s;
    }
    public static void main(String[] args) {
        String s = new String("abcdbueab");
        StringBuilder new_s = new StringBuilder(s);
        String reversed_s = new_s.toString();
        System.out.println(reversed_s);
        System.out.println(s);
        System.out.println(longestPalindrome(s));
    }
 }