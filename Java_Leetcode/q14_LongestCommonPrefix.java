
// still has problems which are not solved.
public class q14_LongestCommonPrefix {
    public static String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";

        String longest_preflix = strs[0];
        int min_size = strs[0].length();

        for (int i = 0; i < strs.length-1; i++){
            min_size = Math.min(min_size, strs[i+1].length());
            for (int j = 0; j < min_size; j++){
                if (strs[i].charAt(j) == strs[i+1].charAt(j)){
                    longest_preflix = longest_preflix.substring(0, j);                    
                }
            }
        }

     
        return longest_preflix;

    }

    // public String longestCommonPrefix(String[] strs) {
    //     if (strs == null || strs.length == 0) return "";
    //     for (int i = 0; i < strs[0].length() ; i++){
    //         char c = strs[0].charAt(i);
    //         for (int j = 1; j < strs.length; j ++) {
    //             if (i == strs[j].length() || strs[j].charAt(i) != c)
    //                 return strs[0].substring(0, i);             
    //         }
    //     }
    //     return strs[0];
    // }

    public static void main(String[] args) {
        String s[] = {"flower","flow","flight"};
        System.out.println(s);
        System.out.println(longestCommonPrefix(s));
    }
 }