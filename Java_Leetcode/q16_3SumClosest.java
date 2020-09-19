public class q16_3SumClosest{

    // public static List<List<Integer>> threeSum(int[] num) {
    //     Arrays.sort(num);
    //     List<List<Integer>> res = new LinkedList<>(); 
    //     for (int i = 0; i < num.length-2; i++) {
    //         if (i == 0 || (i > 0 && num[i] != num[i-1])) {
    //             int lo = i+1, hi = num.length-1, sum = 0 - num[i];
    //             while (lo < hi) {
    //                 if (num[lo] + num[hi] == sum) {
    //                     res.add(Arrays.asList(num[i], num[lo], num[hi]));
    //                     while (lo < hi && num[lo] == num[lo+1]) lo++;
    //                     while (lo < hi && num[hi] == num[hi-1]) hi--;
    //                     lo++; hi--;
    //                 } else if (num[lo] + num[hi] < sum) lo++;
    //                 else hi--;
    //            }
    //         }
    //     }
    //     return res;
    // }

    public static int threeSumClosest(int[] nums, int target) {
        int min = 999999999;
        int min_distance = 999999999;
        for (int i=0; i<nums.length; i++){
            for (int j=i+1; j<nums.length; j++){
                for (int k=j+1; k< nums.length; k++){
                    int distance = Math.abs(nums[i] + nums[j] + nums[k] - target);  
                    if (distance < min_distance){
                        min_distance = distance;
                        min = nums[i] + nums[j] + nums[k];
                    }
                }
            }
        }
        return min;
    }


    public static void main(String[] args) {
        int numbers[] = {-1, 2, 1, -4};
        int target = 1;
        System.out.println(numbers);
        System.out.println(threeSumClosest(numbers, target));
    }
 }