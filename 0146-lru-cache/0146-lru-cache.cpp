struct Node {
    int key, val;
    Node *next;
    Node *prev;
    Node(int key, int val) : key(key), val(val), next(nullptr), prev(nullptr) {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> map;
    Node *head = new Node(-1, -1);
    Node *tail = new Node(-1, -1);

    void add(Node* node) {
        Node *tailp = tail->prev;
        tailp->next = node;
        node->next = tail;
        node->prev = tailp;
        tail->prev = node;
    }

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

public:

    LRUCache(int capacity) {
        this->capacity = capacity;
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if(map.find(key) == map.end()) {
            return -1;
        }

        Node *node = map[key];
        remove(node);
        add(node);

        return node->val;
    }
    
    void put(int key, int value) {
        if(map.find(key) != map.end()) {
            Node *old = map[key];
            remove(old);
        }
        
        Node *node = new Node(key, value);
        map[key] = node;

        if(map.size() > this->capacity) {
            map.erase(head->next->key);
            remove(head->next);
        }

        add(node);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */