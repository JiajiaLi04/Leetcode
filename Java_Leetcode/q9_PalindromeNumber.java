public class q9_PalindromeNumber {
    public static boolean isPalindrome(int x) {
        int p = x;

        if (p>0){
            int rev = 0; 
            while (p != 0) {
                int pop = p % 10;
                p /= 10;
                rev = rev * 10 + pop;
            }
            if (x==rev){
                return true;
            }
            else{
                return false;
            }
        }
        else if (x<0){
            return false;
        }
        else{
            return true;
        }
        
    }
    public static void main(String[] args) {
        int numbers = 1231;
        System.out.println(numbers);
        System.out.println(isPalindrome(numbers));
    }
 }