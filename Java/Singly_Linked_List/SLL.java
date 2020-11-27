public class SLL {
    private Node start;

    public SLL() {
        this.start = null;
    }

    public void add(Node node) {
        if (this.start == null) {
            this.start = node;
            return;
        }

        Node pointer = this.start;

        while (pointer.hasNext()) {
            pointer = pointer.getNext();
        }

        pointer.setNext(node);
    }

    public void remove(Node node) {
        if (this.start == null) {
            return;
        }

        if (!this.start.hasNext() && this.start == node) {
            this.start = null;
            return;
        }

        Node prev = null;
        Node cur = this.start;

        while (cur != null && !cur.equals(node)) {
            prev = cur;
            cur = cur.getNext();
        }

        if (cur == this.start) {
            this.start = this.start.getNext();
            return;
        }

        if (cur == null) {
            return;
        }

        prev.setNext(cur.getNext());
        cur.setNext(null);
    }

    public void printSLL() {
        if (this.start == null) {
            return;
        }

        Node pointer = this.start;
        System.out.print("[ ");

        while (pointer != null) {
            System.out.print(pointer.getVal() + " ");
            pointer = pointer.getNext();
        }

        System.out.println("]");
    }
}
