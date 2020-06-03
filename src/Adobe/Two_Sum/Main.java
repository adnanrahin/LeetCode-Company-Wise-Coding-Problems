package Adobe.Two_Sum;

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String args[]) {

    }

    public static int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> sumMaps = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            sumMaps.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i++) {
            int sum = target - nums[i];
            if (sumMaps.containsKey(sum) && sumMaps.get(sum) != i)
                return new int[]{Math.min(i, sumMaps.get(i)), Math.max(i, sumMaps.get(i))};
        }

        return new int[]{};

    }
}
