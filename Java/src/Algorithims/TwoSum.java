package Algorithims;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {
    public static int[] sol(int[] arr, int target) {
        for (int i = 0; i <= arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                int com = target - arr[i];
                if (com == arr[j]) {
                    return new int[]{arr[i], arr[j]};
                }
            }
        }
        throw new IllegalArgumentException("No Matching values");
    }

    public static int[] bestSol(int[] arr, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int complement = target - arr[i];
            if (map.containsKey(complement)) {
                return new int[]{i, map.get(complement)};
            }
            map.put(arr[i], i);
        }
        throw new IllegalArgumentException("None found");
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 3, 4, 5, 6};
        int target = 10;
        System.out.println(Arrays.toString(sol(arr, target)));
        System.out.println(Arrays.toString(bestSol(arr, target)));
    }
}
