package Algorithims;

public class BinarySearch {
    //we use the divide and conquer strategy
    //for ordered items and space complexity is reduced everytime
    //there is recursive and

    //iterative approach {beginning and end


    //recursive approach
    static int recursiveBinSearch(int[] myArr, int key, int first, int last) {
        int mid = (first + last) / 2;
        if (myArr[mid] == key) {
            return mid;
        }
        if (key < myArr[last]) {
            if (key < myArr[mid]) {
                return recursiveBinSearch(myArr, key, first, mid - 1);

            } else if (key > myArr[mid]) {
                return recursiveBinSearch(myArr, key, mid + 1, last);
            }
        }
        return -1;
    }

    //iterative approach
    static int iterativeBinSearch(int[] myArr, int key) {
        int first, last, mid;
        first = 0;
        last = myArr.length - 1;
        while (first <= last) {
            mid = (last + first) / 2;
            if (myArr[mid] == key) {
                return mid;
            }
            if (key < myArr[mid]) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        }


        return -1;
    }

    public static void main(String[] args) {
        int[] myArr = {1, 3, 4, 5, 6};
        int ans = recursiveBinSearch(myArr, 88, 0, myArr.length - 1);
        System.out.println(ans);

        System.out.println();
        int ans2 = iterativeBinSearch(myArr, 3);
        System.out.println(ans2);
    }

}
