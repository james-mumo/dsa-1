package Algorithims;

public class InsertionSort {
    static void insertionSort(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int j = i - 1; //prev element
            int b = arr[i]; ///current item

            while (j >= 0 && b <= arr[j]) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = b;
        }
        for (int i : arr) {
            System.out.println(i);
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[]{2,53,6,6,77};
        insertionSort(arr);
    }
}
