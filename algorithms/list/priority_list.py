from typing import TypeVar, Generic, List, Optional
from heapq import heappush, heappop

T = TypeVar('T')

class PriorityList(Generic[T]):
    def __init__(self):
        """
        Initialize an empty priority list.
        Time complexity: O(1)
        """
        self._heap: List[tuple[float, T]] = []
        self._counter = 0  # Used to break ties when priorities are equal
    
    def push(self, item: T, priority: float) -> None:
        """
        Add an item to the priority list with the given priority.
        Lower priority values indicate higher priority.
        Time complexity: O(log n) where n is the number of items in the list
        """
        entry = (priority, self._counter, item)
        heappush(self._heap, entry)
        self._counter += 1
    
    def pop(self) -> Optional[T]:
        """
        Remove and return the item with the highest priority (lowest priority value).
        Returns None if the list is empty.
        Time complexity: O(log n) where n is the number of items in the list
        """
        if not self._heap:
            return None
        return heappop(self._heap)[2]
    
    def peek(self) -> Optional[T]:
        """
        Return the item with the highest priority without removing it.
        Returns None if the list is empty.
        Time complexity: O(1)
        """
        if not self._heap:
            return None
        return self._heap[0][2]
    
    def is_empty(self) -> bool:
        """
        Check if the priority list is empty.
        Time complexity: O(1)
        """
        return len(self._heap) == 0
    
    def clear(self) -> None:
        """
        Remove all items from the priority list.
        Time complexity: O(1)
        """
        self._heap.clear()
        self._counter = 0
    
    def __len__(self) -> int:
        """
        Return the number of items in the priority list.
        Time complexity: O(1)
        """
        return len(self._heap)
    
    def __str__(self) -> str:
        """
        Return a string representation of the priority list.
        Time complexity: O(n log n) where n is the number of items in the list
        """
        items = [(priority, item) for priority, _, item in sorted(self._heap)]
        return f"PriorityList(items={items})"


# Example usage
if __name__ == "__main__":
    # Create a priority list
    pl = PriorityList[str]()
    
    # Add some items with priorities
    pl.push("Task 1", 1.0)
    pl.push("Task 2", 2.0)
    pl.push("Task 3", 0.5)
    pl.push("Task 4", 1.5)
    
    print("Initial priority list:", pl)
    
    # Process items in priority order
    while not pl.is_empty():
        task = pl.pop()
        print(f"Processing task: {task}") 
