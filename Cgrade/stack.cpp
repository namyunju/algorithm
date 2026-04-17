#include <stdio.h> 
int stack[10000];
int top_index = -1; 

void push(int x) {
    top_index++;
    stack[top_index] = x;
}

int pop() {
    if (top_index == -1) {
        return -1; 
    } else {
        int target = stack[top_index];
        top_index--; 
        return target;
    }
}

int top() {
    if (top_index == -1) return -1;
    return stack[top_index];
}

int main() {
    push(10);
    push(20);
    push(30);

    printf("Current Top: %d\n", top());

    printf("Pop: %d\n", pop());
    printf("Pop: %d\n", pop());
    printf("Pop: %d\n", pop());
    printf("Pop: %d\n", pop()); 

    return 0;
}