package Algorithims;

public class Random {
    static boolean reverse(int[] array) {
        for (int i = 0; i < array.length / 2; i++) {
            int other = array.length - i - 1;
            int temp = array[i];
            array[i] = array[other];
            array[other] = temp;
        }
        return false;
    }

    public static void main(String[] args) {
        int[] myArr = {2, 3, 4};

        System.out.println(reverse(myArr));

    }
}
