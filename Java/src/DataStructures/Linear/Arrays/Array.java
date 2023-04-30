package DataStructures.Linear.Arrays;//continous in memory and same data types for all
//elements


public class Array {
    public static void main(String[] args) {
//        int[] myArr = new int[6];
//        int arrItem = 1;
//
//        for (int i = 0; i < myArr.length; i++) {
//            myArr[i] = arrItem;
//            arrItem++;
//        }
//        for (int i : myArr) {
//            System.out.println(i);
//        }


        //the 2d array
        int[][] newArr = new int[3][10];
        int count = 1;
        for (int i = 0; i < newArr.length; i++) {
            for (int j = 0; j < newArr[i].length; j++) {
                newArr[i][j] = count;
                count++;
            }
        }
        for (int i = 0; i < newArr.length; i++) {
            for (int j = 0; j < newArr[i].length; j++) {
                System.out.print(newArr[i][j] + "  ");
            }
            System.out.println("\n");
        }

        System.out.println(newArr[0][0]);

    }
}