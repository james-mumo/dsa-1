package DataStructures.Hierarchichal.BinarySearchTrees;


class Node {
    char key;
    Node left, right;

    Node(char key) {
        this.key = key;
    }
}

class BinarySolution {
    Node root;

    void insertKey(char key) {
        root = insertInTree(root, key);
    }

    Node insertInTree(Node root, char key) {
        if (root == null) {
            root = new Node(key);
            return root;
        }
        if (key < root.key) {
            root.left = insertInTree(root.left, key);
        } else if (key > root.key) {
            root.left = insertInTree(root.right, key);
        }
        return root;
    }

    void preorderTraversal(Node root) {
        if (root != null) {
            System.out.println(root.key + " ");
            preorderTraversal(root.left);
            preorderTraversal(root.right);
        }
    }
}

public class BST {

    public static void main(String[] args) {
        BinarySolution binarySolution = new BinarySolution();
        binarySolution.insertKey('D');
        binarySolution.insertKey('B');
        binarySolution.insertKey('Z');
        binarySolution.insertKey('K');

        binarySolution.preorderTraversal(binarySolution.root);
    }
}
