package Adobe.Container_With_Most_Water;

public class Main {

    public static void main(String args[]) {

        System.out.println(maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));

    }

    public static int maxArea(int[] height) {

        int area = 0;

        int i = 0;
        int j = height.length - 1;

        while (i <= j) {
            int w = j - i;
            int h = Math.min(height[i], height[j]);
            area = Math.max(area, w * h);
            if (height[i] > height[j]) j--;
            else i++;
        }

        return area;

    }

}
