public class q11_ContainerWithMostWater {
 
    public static int maxArea(int[] height) {

        int maxArea = 0;
        int area = 0;
        for (int i = 0; i < height.length - 1; i++){
            for (int j = i+1; j < height.length; j++){
                area = (j-i)*(Math.min(height[i], height[j]));
                if (area>maxArea){
                    maxArea = area;
                }
            }

        }
        return maxArea;
    }
    
    public static void main(String[] args) {
        int a1[]={1,8,6,2,5,4,8,3,7};
        System.out.println(maxArea(a1));
    }
 }