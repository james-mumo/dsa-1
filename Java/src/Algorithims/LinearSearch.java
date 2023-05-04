package Algorithims;

import java.util.Objects;
import java.util.Scanner;

public class LinearSearch {
//    best case is O(1)
//    because I made one iteration


    static int searchItem(String[] myArr, String item) {

        for (int i = 0; i < myArr.length; i++) {
            if (Objects.equals(myArr[i], item)) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] myArr = new String[]{"Mike", "Jane", "John", "James"};
        int[] nums = new int[1000];
        for (int k = 0; k < nums.length; k++) {
            nums[k] = k;
            System.out.println(nums[k]);
        }
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter item to be searched?");
        String item = scanner.next();
        int ans = searchItem(myArr, item);
//        System.out.println(ans);
        if (ans == -1) {
            System.out.println("Item not found");
        } else {
            System.out.println(myArr[ans] + " was found at index : " + ans);
        }
    }


}

