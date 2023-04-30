package DataStructures.Hierarchichal.BinaryTrees;

class Node {
    char key; //value
    Node left, right;

    Node(char key) {
        this.key = key;
    }
}

class Tree {
    Node root;

    void preorderTraversal(Node n) {
        if (n != null) {
            System.out.print(n.key + " ");
            preorderTraversal(n.left);
            preorderTraversal(n.right);
        }
    }

    void postorderTraversal(Node n) {
        if (n != null) {
            postorderTraversal(n.left);
            postorderTraversal(n.right);
            System.out.print(n.key + " ");
        }
    }

    void inorderTraversal(Node n) {
        if (n != null) {
            inorderTraversal(n.left);
            System.out.print(n.key + " ");
            inorderTraversal(n.right);
        }
    }
}

public class TreeTraversal {
    public static void main(String[] args) {
        Tree tt = new Tree();
        tt.root = new Node('A');
        tt.root.left = new Node('B');
        tt.root.right = new Node('C');

        tt.preorderTraversal(tt.root);
        System.out.println();
        tt.postorderTraversal(tt.root);
        System.out.println();
        tt.inorderTraversal(tt.root);
    }
}
