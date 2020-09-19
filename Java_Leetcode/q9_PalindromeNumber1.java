public class q9_PalindromeNumber1 {
    public static boolean IsPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        else{
            int revertedNumber = 0;
            while(x > revertedNumber) {
                revertedNumber = revertedNumber * 10 + x % 10;
                x /= 10;
            }
            return x == revertedNumber || x == revertedNumber/10;
        }
    }
    public static void main(String[] args) {
        int numbers = 1231;
        System.out.println(numbers);
        System.out.println(IsPalindrome(numbers));
    }
 }