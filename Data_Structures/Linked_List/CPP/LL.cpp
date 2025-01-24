#include <iostream>
using namespace std;

class Node{
    public:
        int data;
        Node *next=NULL;

    Node(int data){
        this->data = data;
        next = NULL;
    }
};

class LinkedList{
    public:
    Node *head = NULL;
    Node *tail = NULL;
    int size = 0;

    LinkedList(){}

    LinkedList(int arr[], int length){
        for(int i = 0; i<length; i++){
            this->append(arr[i]);
        }
        size = length;
    }

    void print(){
        Node *temp = head;
        while (temp!=NULL)
        {
            cout<<temp->data<<"->";
            temp = temp->next;
        }
        cout<<"NULL"<<endl;
    }

    void append(int num){
        if(head == NULL){ // If LinkedList is Empty
            Node *temp = new Node(num);
            head = temp;
            tail = temp;
            size++; 
        }else{
            Node *temp = new Node(num);
            tail->next = temp;
            tail = tail->next;
            size++;
        }
    }

    void insert(int item, int place){
        if(head == NULL){ // If Linked List is Empty
            this->append(item);

        }
        else if(place <= 0){ // At Head(For 0 or negative places)
            Node *temp = new Node(item);
            temp->next = head;
            head = temp;
            size++;
        }
        else if(place >= size){ // At Tail(For Equal Size or Greater size place)
            this->append(item);

        }
        else{ // In Between Head or Tail
            int count = 0;
            Node *a = head;
            Node *b = head->next;
            for(int i = 0;i<=place-2; i++){
                a = a->next;
                b = b->next;
            }
            // Create New Node
            Node *temp = new Node(item);
            temp->next = b;
            a->next = temp;
            size++;
        }
    }

    void deleteith(int place){
        if(head == NULL){
            cout<<"Linked List is Empty"<<endl;
        }else if(place <0 || place >= size){
            cout<<"List Index Out of Bounds"<<endl;
        }
        else if(place ==0){ //Delete Head
            Node *temp = head;
            head = head->next;
            temp->next = NULL;
            free(temp); // Remove from memory
            size--;
        }else if(place == size-1){ // Remove Tail
            Node *front = head;
            Node *back = head->next;
            while (back != tail)
            {
                front = front->next;
                back = back->next;
            }
            front->next = NULL;
            tail = front;
            free(back);
            size--;
        }else{
            int count = 0;
            Node *front = head;
            Node *todelete = head->next;
            //Node *back = todelete->next;
            for(int i = 0;i<=place-2; i++){
                front = front->next;
                todelete = todelete->next;
               // back = back->next;
            }
            // Remove Links
            front->next = todelete->next;
            todelete->next = NULL;
            free(todelete);
            size--;
        }
    }

    int search(int num){
        int count = 0;
        Node *temp = head;
        while(temp->data != num){
            if (temp->next == NULL){
                count = -1;
                break;
            }
            temp = temp->next;
            count++;
        }
        return count;
    }

    // Middle Of Linked List Using Two Pointer Approach
    static Node *Middle(LinkedList *LL){
        if (LL == NULL){
            return NULL;
        }
        int count = 1;
        Node *pt1 = LL->head;
        Node *pt2 = LL->head;
        while (pt2->next != NULL)
        {
            if(count %2 == 0){
                pt1 = pt1->next;
            }
            pt2 = pt2->next;
            count++;
        }
        return pt1;
    }
};

int main(){
    int arr[] = {1,2,3,4,5,6};
    int length = sizeof(arr)/sizeof(arr[0]);
    cout<<length<<endl;
    LinkedList *l1 = new LinkedList(arr, length);
    l1->print();
    cout<<l1->size<<endl;


    l1->insert(20,-2);
    l1->print();
    cout<<l1->size<<endl;

    l1->insert(70,20);
    l1->print();
    cout<<l1->size<<endl;

    l1->deleteith(0);

    l1->print();

    cout<<"Location of 6: "<<l1->search(6)<<endl;

    // Middle Of Linked List
    Node *Middle = LinkedList::Middle(l1);

    cout<<"Middle Of Linked List: "<<Middle->data<<endl;

    
    return 0;
}