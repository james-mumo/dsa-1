package DataStructures.Lists;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

public class StackToLinkedList {
    public static void main(String[] args) {
        Stack<Integer> ss = new Stack<>();

        ss.push(2);
        ss.push(3);

        LinkedList<Integer> ll = new LinkedList<>(ss);

        //displaying
        Iterator it = ll.iterator();
        for(Integer i :ll){
            System.out.println(i);
        }
    }
}
