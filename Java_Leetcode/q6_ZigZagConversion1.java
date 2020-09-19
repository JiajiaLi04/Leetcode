public class q6_ZigZagConversion1 {
 
    public static String convert(String s, int numRows) {
        if (numRows == 1) return s;
        StringBuilder ret = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret.append(s.charAt(j + cycleLen - i));
            }
        }
        return ret.toString();
    }

    public static void main(String[] args) {
        String s = new String("PAYPALISHIRING");
        StringBuilder new_s = new StringBuilder(s);
        String reversed_s = new_s.toString();
        System.out.println(reversed_s);
        System.out.println(s);
        System.out.println(convert(s, 3));
    }
 }