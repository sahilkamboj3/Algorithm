public class Node {
    private int val;
    private Node next;

    public Node(int val) {
        this.val = val;
        this.next = null;
    }

    public boolean hasNext() {
        if (this.next == null) {
            return false;
        }
        return true;
    }

    // @Override
    public boolean equals(Node node) {
        if (node.getVal() == this.val) {
            return true;
        }
        return false;
    }

    // getter methods
    public int getVal() {
        return this.val;
    }

    public Node getNext() {
        return this.next;
    }

    // setter methods
    public void setNext(Node next) {
        this.next = next;
    }

    public void setVal(int val) {
        this.val = val;
    }
}
