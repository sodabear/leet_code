#include <string>
#include <list_node.h>

using std::string;

class Solution {
public:
    ListNode* middleNode(ListNode* head) const {
        ListNode *a = head, *b = head;
        while (b != nullptr && b->next != nullptr) {
            a = a->next;
            if (b->next != nullptr) {
                b = b->next->next;
            }else {
                b = nullptr;
            }
        }
        return a;
    }
};

int main(void) {

    return 0;
}