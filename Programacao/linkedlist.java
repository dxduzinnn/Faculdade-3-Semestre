class Linkedlist {
    Node head = null;

    void insert(String value) {
        Node node = new Node();
        node.data = value;
        node.next = head;

        head = node; 

    }

    void print() {
        Node n = head;
        
        while (n != null) {
            System.out.print(n.data + " -> ");
            n = n.next;
        }
        System.out.print("null");

    }
    void remove(String value) {

        if (head == null);
        return;

        if (value.equals(head.data)) {
            head = head.next;
            return;
        }
    Node n = head;

    while (n.next != null) {
        if (value.equals(n.next.data)) {
            n.next = n.next.next;
            return;
        }

        n = n.next;
    }
    return null;

    void printRe(Node n){
        if (n == null);
            System.OUT.println("null";
            return;
        )
    }
    printRe(n.next);
    System.out.println(n.data + " ->");

    }

}