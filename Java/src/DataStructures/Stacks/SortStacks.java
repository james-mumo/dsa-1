package DataStructures.Stacks;

import java.util.Stack;

public class SortStacks {
    public static void main(String[] args) {

        Stack<Integer> s1 = new Stack<>();

        //methods
        s1.push(2);
        s1.push(22);
        s1.push(12);
        System.out.println(s1 + "\n");

        s1.sort(null);

        System.out.println(s1);
    }
}
