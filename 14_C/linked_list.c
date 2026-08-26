#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};
int main()
{
    struct Node *head;
    struct Node *node1;
    struct Node *node2;
    struct Node *node3;
    
    node1 = (struct Node*)malloc(sizeof(struct Node));
    node2 = (struct Node*)malloc(sizeof(struct Node));
    node3 = (struct Node*)malloc(sizeof(struct Node));
    
    node1->data = 10;
    node1->next = node2;
    node2->data = 20;
    node2->next = node3;
    node3->data = 30;
    node3->next = NULL;

    printf("Node 1 details: \n%d\t",*node1);
    printf("%p",node1);
    printf("\nNode 2 details: \n%d\t",*node2);
    printf("%p",node2);
    printf("\nNode 3 details: \n%d\t",*node3);
    printf("%p",node3);

    return 0;
}