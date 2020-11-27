public class Main {
    public static void main(String[] args) {
        SLL sll = new SLL();
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        Node node3 = new Node(3);

        sll.add(node1);
        sll.add(node2);
        sll.add(node3);

        sll.printSLL();

        sll.remove(node2);
        sll.remove(node1);
        sll.remove(node3);
        sll.remove(new Node(5));

        sll.printSLL();
    }

}