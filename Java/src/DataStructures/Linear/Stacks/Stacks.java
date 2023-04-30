package DataStructures.Linear.Stacks;

import java.util.Iterator;
import java.util.Stack;

public class Stacks {
    //inbuilt class defined in java programming
    //collection interface implemented by stack push pop and peek and isEmty
    //it's a collection same as vector


    public static void main(String[] args) {
        Stack<Integer> s1 = new Stack<>();

        //methods
        s1.push(2);
        s1.push(22);
        s1.push(92);
        System.out.println(s1);

        s1.pop();
        System.out.println(s1);

        System.out.println(s1.peek());

        boolean status = s1.isEmpty();
        System.out.println(status + "\n \n");


        //print all stack items with iterator
        Iterator<Integer> it = s1.iterator();
        while (it.hasNext()) {
            Object ob = it.next();
            System.out.println(ob);
        }


    }
}
