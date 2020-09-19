
public class FindMax {
    public static int max(int[] m) {
        int i = 0;
        int a = 0;
        while (i < m.length){
            if (a < m[i]) {
                a = m[i+1];
                i = i+1;
            }
        }
        return a;
    }
    public static void main(String[] args) {
       int[] numbers = new int[]{9, 2, 15, 2, 22, 10, 6}; 
       System.out.println(numbers);
       System.out.println(max(numbers));
    }
 }
