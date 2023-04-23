package DataStructures.Arrays;

import java.util.Arrays;

public class SortArrays {
    public static void main(String[] args) {
        int[] newArr = new int[]{8, 5, 2};

        for (int i : newArr) {
            System.out.print(i);
        }

        Arrays.sort(newArr);

        System.out.println("");
        for (int j : newArr) {
            System.out.print(j);
        }
        ;

        for (int h = 0; h < newArr.length; h++) {
            System.out.println(newArr[h]);
        }
    }
}
