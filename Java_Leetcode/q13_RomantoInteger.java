public class q13_RomantoInteger {
 
    public static int romanToInt(String s) {
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'M': {
                    if (i > 0 && s.charAt(i-1) == 'C') res += 800;
                    else res += 1000;
                    break;
                }
                case 'D': {
                    if (i > 0 && s.charAt(i-1) == 'C') res += 300;
                    else res += 500;
                    break;
                }
                case 'C': {
                    if (i > 0 && s.charAt(i-1) == 'X') res += 80;
                    else res += 100;
                    break;
                }
                case 'L': {
                    if (i > 0 && s.charAt(i-1) == 'X') res += 30;
                    else res += 50;
                    break;
                }
                case 'X': {
                    if (i > 0 && s.charAt(i-1) == 'I') res += 8;
                    else res += 10;
                    break;
                }
                case 'V': {
                    if (i > 0 && s.charAt(i-1) == 'I') res += 3;
                    else res += 5;
                    break;
                }
                case 'I': {
                    res += 1;
                    break;
                }
                default: return 0;
            }
        }
        return res;   
    }

    public static void main(String[] args) {
        String s = new String("MCMXCIV");
        StringBuilder new_s = new StringBuilder(s);
        String reversed_s = new_s.toString();
        System.out.println(reversed_s);
        System.out.println(s);
        System.out.println(romanToInt(s));
    }
 }