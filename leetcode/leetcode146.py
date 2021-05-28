# 146. LRU 缓存机制
# import collections
# class DLinkedNode:
#     def __init__(self,key=0,value=0):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.cache = dict()
#         self.head = DLinkedNode()
#         self.tail= DLinkedNode()
#         self.head.next = self.tail
#         self.tail.prev= self.head
#         self.capacity = capacity
#         self.size = 0
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         node = self.cache[key]
#         self.moveToHead(node)
#         return node.value
#
#
#     def put(self, key: int, value: int) -> None:
#         if key not in self.cache:
#             # 如果 key 不存在，创建一个新的节点
#             node = DLinkedNode(key, value)
#             # 添加进哈希表
#             self.cache[key] = node
#             # 添加至双向链表的头部
#             self.addToHead(node)
#             self.size += 1
#             if self.size > self.capacity:
#                 # 如果超出容量，删除双向链表的尾部节点
#                 removed = self.removeTail()
#                 # 删除哈希表中对应的项
#                 self.cache.pop(removed.key)
#                 self.size -= 1
#         else:
#             # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
#             node = self.cache[key]
#             node.value = value
#             self.moveToHead(node)
#
#     def addToHead(self,node):
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node
#
#     def removeNode(self,node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#     def moveToHead(self,node):
#         self.removeNode(node)
#         self.addToHead(node)
#
#     def removeTail(self):
#         node = self.tail.prev
#         self.removeNode(node)
#         return node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# from collections import OrderedDict
# class LRUCache(collections.OrderedDict):
#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         if key in self:
#             self.move_to_end(key)
#             return self[key]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self)>self.capacity:
#             self.popitem(last=False)


class DLinkedNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key,value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size>self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
    def addToHead(self,node):
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node


solution = LRUCache(1)
solution.put(2,1)
solution.get(2)



class DLinkedNode:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.moveToHead(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            node = DLinkedNode(key,value)
            self.dict[key] = node
            self.size += 1
            self.addToHead(node)
        else:
            node = self.dict[key]
            node.value = value
            self.moveToHead(node)
        if self.size>self.capacity:
            node = self.removeTail()
            self.dict.pop(node.key)
            self.size -= 1

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def removeNode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def addToHead(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self,node):
        self.removeNode(node)
        self.addToHead(node)




