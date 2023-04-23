package DataStructures.Queue;

public class Queues {
    int front, rear;
    int Capacity;
    static int[] arr;

    Queues(int size) {
        this.Capacity = size;
        arr = new int[Capacity];
    }

    void enqueue(int val) {
        if (rear == Capacity) {
            System.out.println("Queue is full");
        } else {
            arr[rear] = val;
            rear++;
        }
    }

    void deque() {
        if (rear == 0) {
            System.out.println("Its empty nothing to delete");
        } else {
            for (int i = 0; i < rear - 1; i++) {
                arr[i] = arr[i + 1];
            }
            rear--;
        }
    }

    void display() {
        if (rear == 0) {
            System.out.println("Queue is empty");
        } else {
            for (int j : arr) {
                System.out.println(j);
            }
        }
    }

    public static class Queue {
        public static void main(String[] args) {
            Queues q = new Queues(3);
            q.enqueue(8);
            q.enqueue(9);
            q.enqueue(10);

            q.display();

            System.out.println("");
            q.deque();
            q.display();
        }
    }

}


