class Solution:
    def insert(self, intervals, newInterval):
        result = []
        for interval in intervals:
            # case1: if interval is before newInterval, append to the result
            if interval[1] < newInterval[0]:
                result.append(interval)
            
            # case2: interval starts after newInterval ends
            # at this step, we have dont updating newInterval
            # we should append newInterval to result
            # and the key step is set interval to newInterval
            # because there might be more intervals to check and each
            # of them will start after current interval, so we can
            # append them properly to result
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            # case3: overlaping, we want to compare current interval with
            # newInterval, and update newInterval
            # that way we can use the updated newInterval to compare with 
            # next interval
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        
        # we want to append newInterval to result at the end, because
        # newInterval will be pointing to the last interval (or the
        # newInterval could be the last one)
        result.append(newInterval)
        return result

def main():
    solution = Solution()
    test_cases = [
        # 1️⃣ Basic overlap in middle
        {
            "intervals": [[1,3],[6,9]],
            "newInterval": [2,5],
            "expected": [[1,5],[6,9]]
        },
        # 2️⃣ Multiple merges
        {
            "intervals": [[1,2],[3,5],[6,7],[8,10],[12,16]],
            "newInterval": [4,8],
            "expected": [[1,2],[3,10],[12,16]]
        },
        # 3️⃣ New interval comes after all
        {
            "intervals": [[1,2],[3,5]],
            "newInterval": [6,7],
            "expected": [[1,2],[3,5],[6,7]]
        },
        # 4️⃣ New interval comes before all
        {
            "intervals": [[3,5],[7,9]],
            "newInterval": [1,2],
            "expected": [[1,2],[3,5],[7,9]]
        },
        # 5️⃣ New interval overlaps with all
        {
            "intervals": [[1,3],[4,6],[7,9]],
            "newInterval": [0,10],
            "expected": [[0,10]]
        },
        # 6️⃣ Single interval merge
        {
            "intervals": [[1,5]],
            "newInterval": [2,3],
            "expected": [[1,5]]
        },
        # 7️⃣ Empty input
        {
            "intervals": [],
            "newInterval": [2,3],
            "expected": [[2,3]]
        },
        # 8️⃣ Touching but not overlapping
        {
            "intervals": [[1,2],[5,7]],
            "newInterval": [3,4],
            "expected": [[1,2],[3,4],[5,7]]
        },
        # 9️⃣ Overlap at boundary
        {
            "intervals": [[1,2],[3,5]],
            "newInterval": [2,3],
            "expected": [[1,5]]
        },
        # 🔟 Complex merge chain
        {
            "intervals": [[1,2],[4,5],[6,7],[8,9],[10,12]],
            "newInterval": [5,10],
            "expected": [[1,2],[4,12]]
        },
    ]

    for idx, test in enumerate(test_cases):
        result = solution.insert(list(map(list, test["intervals"])), list(test["newInterval"]))
        print(f"Test {idx + 1}:")
        print(f"  Input intervals: {test['intervals']}")
        print(f"  New interval: {test['newInterval']}")
        print(f"  Output:   {result}")
        print(f"  Expected: {test['expected']}")
        print(f"  ✅ Pass\n" if result == test["expected"] else f"  ❌ Fail\n")

if __name__ == "__main__":
    main()
