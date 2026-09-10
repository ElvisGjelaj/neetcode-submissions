class HashTable:

    _DELETED = object()

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0


    def _find(self, key: int) -> int:
        """Return index of key, or -1 if it doesn't exist."""
        idx = key % self.capacity
        start = idx

        while self.arr[idx] is not None:

            if (
                self.arr[idx] is not self._DELETED
                and self.arr[idx][0] == key
            ):
                return idx

            idx = (idx + 1) % self.capacity

            if idx == start:
                break

        return -1


    def _find_empty(self, key: int) -> int:
        """Find a slot where a new key can be inserted."""
        idx = key % self.capacity
        start = idx
        first_deleted = -1

        while self.arr[idx] is not None:

            if self.arr[idx] is self._DELETED and first_deleted == -1:
                first_deleted = idx

            idx = (idx + 1) % self.capacity

            if idx == start:
                break

        # Prefer recycling a deleted position
        if first_deleted != -1:
            return first_deleted

        return idx


    def insert(self, key: int, value: int) -> None:
        # First check if the key already exists
        idx = self._find(key)

        if idx != -1:
            self.arr[idx] = (key, value)
            return

        # New key would bring load factor to >= 0.5
        if (self.size + 1) / self.capacity >= 0.5:
            self.resize()

        idx = self._find_empty(key)

        self.arr[idx] = (key, value)
        self.size += 1


    def get(self, key: int) -> int:
        idx = self._find(key)

        if idx == -1:
            return -1

        return self.arr[idx][1]


    def remove(self, key: int) -> bool:
        idx = self._find(key)

        if idx == -1:
            return False

        self.arr[idx] = self._DELETED
        self.size -= 1

        return True


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        old_arr = self.arr

        self.capacity *= 2
        self.arr = [None] * self.capacity

        for item in old_arr:
            if item is None or item is self._DELETED:
                continue

            key, value = item
            idx = self._find_empty(key)
            self.arr[idx] = (key, value)


            