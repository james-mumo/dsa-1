package DataStructures.Linear.Lists;

import java.util.LinkedList;

public class LinkedLists {
    //there are 3 types -->singly Lists, doubly linked list and circular linked list

    public static void main(String[] args) {
        LinkedList<Integer> ll = new LinkedList<>();

        //adding elements
        ll.add(3);
        ll.add(4);
        ll.add(4);
        ll.add(4);
        ll.add(1, 3);

        //removing elements
        ll.remove();
        ll.removeFirst();
        ll.removeLast();

        for (Integer integer : ll) {
            System.out.print(integer + " ");

        }
        System.out.println(ll.contains(3));
        System.out.println(ll.size());
    }
}
