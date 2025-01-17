class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Пример использования очереди
if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())  # True
    queue.enqueue("действие 1")
    queue.enqueue("действие 2")
    queue.enqueue("действие 3")
    print(queue.is_empty())  # False
    print(queue.size())      # 3
    print(queue.dequeue())   # действие 1
    print(queue.size())      # 2
