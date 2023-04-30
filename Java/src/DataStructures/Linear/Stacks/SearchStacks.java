package DataStructures.Linear.Stacks;

import java.util.Iterator;
import java.util.Stack;

public class SearchStacks {
    public static void main(String[] args) {
        Stack<Integer> ss = new Stack<>();
        //search
        ss.push(0);
        ss.push(1);
        ss.push(2);
        ss.push(4);
        ss.push(5);
        System.out.println(ss + "\n");


        int answer = ss.search(2);
        System.out.println(answer);


        //iterating over a stack
        Iterator it = ss.iterator();
        System.out.println("Iterator Has been Called");

        while (it.hasNext()) {
            Object ob = it.next();
            System.out.println(ob);
        }


    }
}
