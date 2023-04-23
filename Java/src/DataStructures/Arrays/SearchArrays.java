package DataStructures.Arrays;

public class SearchArrays {

    public static int[] newArr = new int[]{2, 5, 6, 7, 78, 99};

    public static int SearchArray(int[] array, int key) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == key) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int indexValue = SearchArray(newArr, 6);
        if (indexValue == -1) {
            System.out.println("Item not found");

        } else {
            System.out.println("Found at index : " + indexValue);
        }
    }
}
