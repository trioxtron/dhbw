from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        pre = defaultdict(list)

        for c, p in prerequisites:
            pre[c].append(p)

        taken = set()
        visited = []

        def dfs(course):
            if not pre[course]:
                return True

            if course in taken:
                return False

            taken.add(course)

            for p in pre[course]:
                if p not in visited:
                    visited.append(p)
                if not dfs(p): return False

            if course not in visited:
                visited.append(course)
            
            pre[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course): return []

        visited = visited + [x for x in list(range(numCourses)) if x not in visited]
        

        return visited


def main():
    sol = Solution()
    numCourses = 3
    prerequisites = [[1, 0]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2] or any valid topological order

    numCourses = 3
    prerequisites = [[2,0],[2,1]] 
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2] or any valid topological order


    return
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2, 3] or any valid topological order

    # Example usage
    numCourses = 5
    prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [1, 2, 3, 4, 0] or any valid topological order

    numCourses = 2
    prerequisites = [[1, 0]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0, 1] or any valid topological order

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0, 1, 2, 3] or any valid topological order

    numCourses = 1
    prerequisites = []
    print(sol.findOrder(numCourses, prerequisites))  # Output: [0] or any valid topological order


if __name__ == "__main__":
    main()
