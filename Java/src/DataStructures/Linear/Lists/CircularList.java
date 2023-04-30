package DataStructures.Linear.Lists;


public class CircularList {
    Node head, tail;

    class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    void insertElements(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            tail = newNode;
            tail.next = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
            tail.next = head;
        }
    }

    void displayElements() {
        Node nn = head;
        if (tail == null && head == null) {
            System.out.println("Circular LinkedList is Empty");
        } else {
            do {
                System.out.println(nn.data);
                nn = nn.next;
            } while (nn != head);
        }

    }

    void deleteElements() {
        if (tail != head) {
            head = head.next;
            tail.next = head;
        } else {
            head = tail = null;
        }
    }

    public static void main(String[] args) {
        CircularList circularList = new CircularList();
        circularList.insertElements(88);
        circularList.insertElements(89);
        circularList.insertElements(90);

        circularList.displayElements();

        circularList.deleteElements();

        System.out.println();

        circularList.displayElements();
    }
}
