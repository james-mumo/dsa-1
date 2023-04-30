package DataStructures.Linear.Lists;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.Stack;

public class StackToLinkedList {
    public static void main(String[] args) {
        Stack<String> ss = new Stack<>();

        ss.push("James");
        ss.push("Miek");
        ss.push("ghgh");
        ss.push("James");

        //copyng to the linkedList

        LinkedList<String> ll = new LinkedList<>(ss);
        Iterator<String> it = ll.iterator();

        while (it.hasNext()) {
            System.out.println(it.next());
        }


    }
}
