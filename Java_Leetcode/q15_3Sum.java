import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class q15_3Sum{
    public static List<List<Integer>> threeSum(int[] num) {
        Arrays.sort(num);
        List<List<Integer>> res = new LinkedList<>(); 
        for (int i = 0; i < num.length-2; i++) {
            if (i == 0 || (i > 0 && num[i] != num[i-1])) {
                int lo = i+1, hi = num.length-1, sum = 0 - num[i];
                while (lo < hi) {
                    if (num[lo] + num[hi] == sum) {
                        res.add(Arrays.asList(num[i], num[lo], num[hi]));
                        while (lo < hi && num[lo] == num[lo+1]) lo++;
                        while (lo < hi && num[hi] == num[hi-1]) hi--;
                        lo++; hi--;
                    } else if (num[lo] + num[hi] < sum) lo++;
                    else hi--;
               }
            }
        }
        return res;
    }
    // public static List<List<Integer>> threeSum(int[] nums) {
    //     List<List<Integer>> trips = new ArrayList<List<Integer>>();
    //     List<Integer> elements = new ArrayList<Integer>();
    //     for (int i=0; i<nums.length; i++){
    //         for (int j = i+1; j< nums.length; j++){
    //             for (int k = i+2; k<nums.length; k++){
    //                 if (nums[i]+nums[j]+nums[k]==0){
    //                     elements.add(nums[i]);
    //                     elements.add(nums[j]);
    //                     elements.add(nums[k]);
    //                     trips.add(elements);
    //                 }
    //             }
    //         }
    //     }
    //     return trips;
    // }
    public static void main(String[] args) {
        int numbers[] = {-1, 0, 1, 2, -1, -4};
        System.out.println(numbers);
        System.out.println(threeSum(numbers));
    }
 }