class UnionFind:
    def __init__(self, nums):
        self.parent = {n:n for n in nums}
        self.rank = {n:0 for n in nums}
    
    def find(self, x):
        if x == self.parent[x]:
            return x

        self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootY] < self.rank[rootX]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1

    def max_length(self):
        root_counter = {}
        for n in self.parent:
            root_counter[self.find(n)] = root_counter.get(self.find(n), 0) + 1
        return root_counter[max(root_counter, key= lambda x:root_counter[x])]


class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        unions = UnionFind(nums)

        nums = set(nums)
        for _, n in enumerate(nums):
            if n + 1 in nums:
                unions.union(n, n+1)
            if n - 1 in nums:
                unions.union(n, n-1)


        return unions.max_length()


def main():
    solution = Solution()

    nums = [0, 1, 2, 3, 4, 5]
    print(solution.longestConsecutive(nums))  # Output: 6
    nums = [100, 4, 200, 1, 3, 2]
    print(solution.longestConsecutive(nums))  # Output: 4
    nums = [10, 20, 30, 40]
    print(solution.longestConsecutive(nums))  # Output: 1



if __name__ == "__main__":
    main()
