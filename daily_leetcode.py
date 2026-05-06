#!/usr/bin/env python3
import os, json, datetime, webbrowser, subprocess

DSA_FOLDER = r"C:\Users\Sheshandra Reddy\OneDrive\Desktop\dsa-practice"
README_PATH = os.path.join(DSA_FOLDER, "README.md")
PROGRESS_FILE = os.path.join(DSA_FOLDER, ".progress.json")

PROBLEMS = {
    1:  {"name":"Two Sum","difficulty":"Easy","topic":"HashMap","url":"https://leetcode.com/problems/two-sum","filename":"two_sum.py","solution":'''from typing import List\n\nclass Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        seen = {}\n        for i, num in enumerate(nums):\n            complement = target - num\n            if complement in seen:\n                return [seen[complement], i]\n            seen[num] = i''',"explanation":"\n  PATTERN: HashMap\n  - For each number, check if its complement (target-num) was seen before\n  - If yes return indices, if no store and continue\n  TIME: O(n) | SPACE: O(n)"},
    2:  {"name":"Valid Parentheses","difficulty":"Easy","topic":"Stack","url":"https://leetcode.com/problems/valid-parentheses","filename":"valid_parentheses.py","solution":'''class Solution:\n    def isValid(self, s: str) -> bool:\n        stack = []\n        pairs = {")": "(", "}": "{", "]": "["}\n        for char in s:\n            if char in "({[":\n                stack.append(char)\n            elif stack and stack[-1] == pairs[char]:\n                stack.pop()\n            else:\n                return False\n        return len(stack) == 0''',"explanation":"\n  PATTERN: Stack\n  - Push opening brackets, pop when closing matches\n  - Stack must be empty at end\n  TIME: O(n) | SPACE: O(n)"},
    3:  {"name":"Best Time to Buy and Sell Stock","difficulty":"Easy","topic":"Array","url":"https://leetcode.com/problems/best-time-to-buy-and-sell-stock","filename":"best_time_stock.py","solution":'''from typing import List\n\nclass Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        min_price = prices[0]\n        max_profit = 0\n        for price in prices[1:]:\n            min_price = min(min_price, price)\n            max_profit = max(max_profit, price - min_price)\n        return max_profit''',"explanation":"\n  PATTERN: Min/Max Tracking\n  - Track minimum price and maximum profit as you go\n  TIME: O(n) | SPACE: O(1)"},
    4:  {"name":"Contains Duplicate","difficulty":"Easy","topic":"HashSet","url":"https://leetcode.com/problems/contains-duplicate","filename":"contains_duplicate.py","solution":'''from typing import List\n\nclass Solution:\n    def containsDuplicate(self, nums: List[int]) -> bool:\n        seen = set()\n        for num in nums:\n            if num in seen:\n                return True\n            seen.add(num)\n        return False''',"explanation":"\n  PATTERN: HashSet\n  - Track seen numbers, return True if seen again\n  TIME: O(n) | SPACE: O(n)"},
    5:  {"name":"Maximum Subarray","difficulty":"Easy","topic":"Kadane's Algorithm","url":"https://leetcode.com/problems/maximum-subarray","filename":"maximum_subarray.py","solution":'''from typing import List\n\nclass Solution:\n    def maxSubArray(self, nums: List[int]) -> int:\n        current_sum = nums[0]\n        max_sum = nums[0]\n        for num in nums[1:]:\n            current_sum = max(num, current_sum + num)\n            max_sum = max(max_sum, current_sum)\n        return max_sum''',"explanation":"\n  PATTERN: Kadane's Algorithm\n  - At each step: start fresh OR extend previous sum\n  TIME: O(n) | SPACE: O(1)"},
    6:  {"name":"Reverse Linked List","difficulty":"Easy","topic":"Linked List","url":"https://leetcode.com/problems/reverse-linked-list","filename":"reverse_linked_list.py","solution":'''class Solution:\n    def reverseList(self, head):\n        prev = None\n        curr = head\n        while curr:\n            next_node = curr.next\n            curr.next = prev\n            prev = curr\n            curr = next_node\n        return prev''',"explanation":"\n  PATTERN: Pointer Manipulation\n  - Use prev, curr, next to reverse pointers one by one\n  TIME: O(n) | SPACE: O(1)"},
    7:  {"name":"Climbing Stairs","difficulty":"Easy","topic":"Dynamic Programming","url":"https://leetcode.com/problems/climbing-stairs","filename":"climbing_stairs.py","solution":'''class Solution:\n    def climbStairs(self, n: int) -> int:\n        if n <= 2:\n            return n\n        prev2, prev1 = 1, 2\n        for _ in range(3, n + 1):\n            current = prev1 + prev2\n            prev2 = prev1\n            prev1 = current\n        return prev1''',"explanation":"\n  PATTERN: Fibonacci\n  - Ways(n) = Ways(n-1) + Ways(n-2)\n  TIME: O(n) | SPACE: O(1)"},
    8:  {"name":"Merge Two Sorted Lists","difficulty":"Easy","topic":"Linked List","url":"https://leetcode.com/problems/merge-two-sorted-lists","filename":"merge_two_lists.py","solution":'''class Solution:\n    def mergeTwoLists(self, list1, list2):\n        dummy = type(list1)(0)\n        current = dummy\n        while list1 and list2:\n            if list1.val <= list2.val:\n                current.next = list1\n                list1 = list1.next\n            else:\n                current.next = list2\n                list2 = list2.next\n            current = current.next\n        current.next = list1 if list1 else list2\n        return dummy.next''',"explanation":"\n  PATTERN: Dummy Node\n  - Compare heads, attach smaller, advance that pointer\n  TIME: O(n+m) | SPACE: O(1)"},
    9:  {"name":"Linked List Cycle","difficulty":"Easy","topic":"Two Pointers","url":"https://leetcode.com/problems/linked-list-cycle","filename":"linked_list_cycle.py","solution":'''class Solution:\n    def hasCycle(self, head) -> bool:\n        slow = head\n        fast = head\n        while fast and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n            if slow == fast:\n                return True\n        return False''',"explanation":"\n  PATTERN: Floyd's Cycle Detection\n  - Slow moves 1 step, fast moves 2 steps\n  - If cycle exists they will meet!\n  TIME: O(n) | SPACE: O(1)"},
    10: {"name":"Reverse String","difficulty":"Easy","topic":"Two Pointers","url":"https://leetcode.com/problems/reverse-string","filename":"reverse_string.py","solution":'''from typing import List\n\nclass Solution:\n    def reverseString(self, s: List[str]) -> None:\n        left, right = 0, len(s) - 1\n        while left < right:\n            s[left], s[right] = s[right], s[left]\n            left += 1\n            right -= 1''',"explanation":"\n  PATTERN: Two Pointers\n  - Swap from both ends moving inward\n  - Must be done in-place!\n  TIME: O(n) | SPACE: O(1)"},
    11: {"name":"Binary Search","difficulty":"Easy","topic":"Binary Search","url":"https://leetcode.com/problems/binary-search","filename":"binary_search.py","solution":'''from typing import List\n\nclass Solution:\n    def search(self, nums: List[int], target: int) -> int:\n        left, right = 0, len(nums) - 1\n        while left <= right:\n            mid = (left + right) // 2\n            if nums[mid] == target:\n                return mid\n            elif nums[mid] < target:\n                left = mid + 1\n            else:\n                right = mid - 1\n        return -1''',"explanation":"\n  PATTERN: Binary Search\n  - Check middle, eliminate half the array each time\n  TIME: O(log n) | SPACE: O(1)"},
    12: {"name":"Flood Fill","difficulty":"Easy","topic":"BFS/DFS","url":"https://leetcode.com/problems/flood-fill","filename":"flood_fill.py","solution":'''from typing import List\n\nclass Solution:\n    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:\n        original = image[sr][sc]\n        if original == color:\n            return image\n        def dfs(r, c):\n            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original:\n                return\n            image[r][c] = color\n            dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)\n        dfs(sr, sc)\n        return image''',"explanation":"\n  PATTERN: DFS on Grid\n  - Like paint bucket tool in MS Paint!\n  - Recursively fill all connected same-color pixels\n  TIME: O(n*m) | SPACE: O(n*m)"},
    13: {"name":"Lowest Common Ancestor of BST","difficulty":"Easy","topic":"Binary Search Tree","url":"https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree","filename":"lowest_common_ancestor.py","solution":'''class Solution:\n    def lowestCommonAncestor(self, root, p, q):\n        while root:\n            if p.val < root.val and q.val < root.val:\n                root = root.left\n            elif p.val > root.val and q.val > root.val:\n                root = root.right\n            else:\n                return root''',"explanation":"\n  PATTERN: BST Property\n  - Both less than root? Go left\n  - Both greater? Go right\n  - Otherwise? Current node is LCA!\n  TIME: O(h) | SPACE: O(1)"},
    14: {"name":"Balanced Binary Tree","difficulty":"Easy","topic":"Binary Tree","url":"https://leetcode.com/problems/balanced-binary-tree","filename":"balanced_binary_tree.py","solution":'''class Solution:\n    def isBalanced(self, root) -> bool:\n        def height(node):\n            if not node: return 0\n            l = height(node.left)\n            if l == -1: return -1\n            r = height(node.right)\n            if r == -1: return -1\n            if abs(l - r) > 1: return -1\n            return max(l, r) + 1\n        return height(root) != -1''',"explanation":"\n  PATTERN: DFS Recursion\n  - Return -1 if unbalanced, height otherwise\n  TIME: O(n) | SPACE: O(h)"},
    15: {"name":"Diameter of Binary Tree","difficulty":"Easy","topic":"Binary Tree","url":"https://leetcode.com/problems/diameter-of-binary-tree","filename":"diameter_binary_tree.py","solution":'''class Solution:\n    def diameterOfBinaryTree(self, root) -> int:\n        self.res = 0\n        def depth(node):\n            if not node: return 0\n            l = depth(node.left)\n            r = depth(node.right)\n            self.res = max(self.res, l + r)\n            return max(l, r) + 1\n        depth(root)\n        return self.res''',"explanation":"\n  PATTERN: DFS\n  - Diameter at each node = left depth + right depth\n  - Track global max\n  TIME: O(n) | SPACE: O(h)"},
    16: {"name":"Middle of Linked List","difficulty":"Easy","topic":"Linked List","url":"https://leetcode.com/problems/middle-of-the-linked-list","filename":"middle_linked_list.py","solution":'''class Solution:\n    def middleNode(self, head):\n        slow = fast = head\n        while fast and fast.next:\n            slow = slow.next\n            fast = fast.next.next\n        return slow''',"explanation":"\n  PATTERN: Slow & Fast Pointers\n  - When fast reaches end, slow is at middle!\n  TIME: O(n) | SPACE: O(1)"},
    17: {"name":"Maximum Depth of Binary Tree","difficulty":"Easy","topic":"Binary Tree","url":"https://leetcode.com/problems/maximum-depth-of-binary-tree","filename":"max_depth_binary_tree.py","solution":'''class Solution:\n    def maxDepth(self, root) -> int:\n        if not root: return 0\n        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1''',"explanation":"\n  PATTERN: DFS Recursion\n  - depth = max(left depth, right depth) + 1\n  TIME: O(n) | SPACE: O(h)"},
    18: {"name":"First Bad Version","difficulty":"Easy","topic":"Binary Search","url":"https://leetcode.com/problems/first-bad-version","filename":"first_bad_version.py","solution":'''class Solution:\n    def firstBadVersion(self, n: int) -> int:\n        left, right = 1, n\n        while left < right:\n            mid = (left + right) // 2\n            if isBadVersion(mid):\n                right = mid\n            else:\n                left = mid + 1\n        return left''',"explanation":"\n  PATTERN: Binary Search\n  - If mid is bad, answer is mid or before → right = mid\n  - If mid is good, answer is after → left = mid+1\n  TIME: O(log n) | SPACE: O(1)"},
    19: {"name":"Ransom Note","difficulty":"Easy","topic":"HashMap","url":"https://leetcode.com/problems/ransom-note","filename":"ransom_note.py","solution":'''from collections import Counter\n\nclass Solution:\n    def canConstruct(self, ransomNote: str, magazine: str) -> bool:\n        mag = Counter(magazine)\n        for c in ransomNote:\n            if mag[c] <= 0: return False\n            mag[c] -= 1\n        return True''',"explanation":"\n  PATTERN: HashMap Counter\n  - Count magazine letters, check if enough for ransom note\n  TIME: O(n+m) | SPACE: O(1)"},
    20: {"name":"Move Zeroes","difficulty":"Easy","topic":"Two Pointers","url":"https://leetcode.com/problems/move-zeroes","filename":"move_zeroes.py","solution":'''from typing import List\n\nclass Solution:\n    def moveZeroes(self, nums: List[int]) -> None:\n        pos = 0\n        for num in nums:\n            if num != 0:\n                nums[pos] = num\n                pos += 1\n        while pos < len(nums):\n            nums[pos] = 0\n            pos += 1''',"explanation":"\n  PATTERN: Two Pointers\n  - Move all non-zeros forward, fill rest with zeros\n  TIME: O(n) | SPACE: O(1)"},
    21: {"name":"Squares of Sorted Array","difficulty":"Easy","topic":"Two Pointers","url":"https://leetcode.com/problems/squares-of-a-sorted-array","filename":"squares_sorted_array.py","solution":'''from typing import List\n\nclass Solution:\n    def sortedSquares(self, nums: List[int]) -> List[int]:\n        res = [0] * len(nums)\n        l, r = 0, len(nums)-1\n        pos = len(nums)-1\n        while l <= r:\n            if abs(nums[l]) > abs(nums[r]):\n                res[pos] = nums[l]**2; l += 1\n            else:\n                res[pos] = nums[r]**2; r -= 1\n            pos -= 1\n        return res''',"explanation":"\n  PATTERN: Two Pointers from both ends\n  - Largest squares come from either end\n  - Fill result from back to front\n  TIME: O(n) | SPACE: O(n)"},
    22: {"name":"Longest Substring Without Repeating","difficulty":"Medium","topic":"Sliding Window","url":"https://leetcode.com/problems/longest-substring-without-repeating-characters","filename":"longest_substring.py","solution":'''class Solution:\n    def lengthOfLongestSubstring(self, s: str) -> int:\n        char_set = set()\n        left = max_len = 0\n        for right in range(len(s)):\n            while s[right] in char_set:\n                char_set.remove(s[left])\n                left += 1\n            char_set.add(s[right])\n            max_len = max(max_len, right - left + 1)\n        return max_len''',"explanation":"\n  PATTERN: Sliding Window\n  - Expand right, shrink left when duplicate found\n  TIME: O(n) | SPACE: O(n)"},
    23: {"name":"3Sum","difficulty":"Medium","topic":"Two Pointers","url":"https://leetcode.com/problems/3sum","filename":"three_sum.py","solution":'''from typing import List\n\nclass Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        nums.sort()\n        res = []\n        for i in range(len(nums)-2):\n            if i > 0 and nums[i] == nums[i-1]: continue\n            l, r = i+1, len(nums)-1\n            while l < r:\n                s = nums[i]+nums[l]+nums[r]\n                if s == 0:\n                    res.append([nums[i],nums[l],nums[r]])\n                    while l < r and nums[l]==nums[l+1]: l+=1\n                    while l < r and nums[r]==nums[r-1]: r-=1\n                    l+=1; r-=1\n                elif s < 0: l+=1\n                else: r-=1\n        return res''',"explanation":"\n  PATTERN: Sort + Two Pointers\n  - Fix one element, two pointers for the other two\n  - Skip duplicates carefully\n  TIME: O(n²) | SPACE: O(1)"},
    24: {"name":"Product of Array Except Self","difficulty":"Medium","topic":"Array","url":"https://leetcode.com/problems/product-of-array-except-self","filename":"product_except_self.py","solution":'''from typing import List\n\nclass Solution:\n    def productExceptSelf(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        res = [1]*n\n        prefix = 1\n        for i in range(n):\n            res[i] = prefix\n            prefix *= nums[i]\n        suffix = 1\n        for i in range(n-1,-1,-1):\n            res[i] *= suffix\n            suffix *= nums[i]\n        return res''',"explanation":"\n  PATTERN: Prefix + Suffix\n  - result[i] = product of all left × product of all right\n  TIME: O(n) | SPACE: O(1)"},
    25: {"name":"Number of Islands","difficulty":"Medium","topic":"BFS/DFS","url":"https://leetcode.com/problems/number-of-islands","filename":"number_of_islands.py","solution":'''from typing import List\n\nclass Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        count = 0\n        def dfs(r,c):\n            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!="1": return\n            grid[r][c]="0"\n            dfs(r+1,c);dfs(r-1,c);dfs(r,c+1);dfs(r,c-1)\n        for r in range(len(grid)):\n            for c in range(len(grid[0])):\n                if grid[r][c]=="1":\n                    count+=1\n                    dfs(r,c)\n        return count''',"explanation":"\n  PATTERN: DFS on Grid\n  - Each unvisited '1' is a new island\n  - DFS marks all connected land as visited\n  TIME: O(n*m) | SPACE: O(n*m)"},
}


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE,'r') as f:
            return json.load(f)
    return {"completed_days":[1,2,3,4,5,6,7,8,9],"start_date":"2026-04-27"}

def save_progress(p):
    with open(PROGRESS_FILE,'w') as f:
        json.dump(p,f,indent=2)

def get_today_day(p):
    c = p["completed_days"]
    return max(c)+1 if c else 1

def calculate_streak(p):
    if not p["completed_days"]: return 0
    c = sorted(p["completed_days"])
    s = 1
    for i in range(len(c)-1,0,-1):
        if c[i]-c[i-1]==1: s+=1
        else: break
    return s

def show_notification(title, msg):
    try:
        subprocess.run(['powershell','-Command',f'Add-Type -AssemblyName System.Windows.Forms; $n=New-Object System.Windows.Forms.NotifyIcon; $n.Icon=[System.Drawing.SystemIcons]::Information; $n.Visible=$true; $n.ShowBalloonTip(8000,"{title}","{msg}",[System.Windows.Forms.ToolTipIcon]::Info); Start-Sleep 3; $n.Dispose()'],capture_output=True)
    except: pass

def show_solution(p, prob):
    print("\n"+"="*55)
    print(f"  💡 SOLUTION — {prob['name']}")
    print("="*55)
    print(f"\n  📖 EXPLANATION:{prob['explanation']}")
    print(f"\n  💻 CODE:")
    print("  "+"-"*50)
    for line in prob['solution'].split('\\n'):
        print(f"  {line}")
    print("  "+"-"*50)
    print("\n  ⚡ TYPE this on LeetCode (don't copy-paste!)")
    print("  Understanding > memorizing!")
    print("="*55)

def save_and_push(day, prob, progress):
    filepath = os.path.join(DSA_FOLDER, prob['filename'])
    content = f"# Day {day}: {prob['name']}\n# Difficulty: {prob['difficulty']}\n# Topic: {prob['topic']}\n# Date: {datetime.date.today()}\n\n{prob['solution'].replace(chr(92)+'n', chr(10))}\n"
    with open(filepath,'w') as f:
        f.write(content)
    print(f"  ✅ Saved: {prob['filename']}")
    subprocess.run(['code', filepath], capture_output=True)

    # Update README
    with open(README_PATH,'r') as f:
        content = f.read()
    new_row = f"| {day} | {prob['name']} | {prob['difficulty']} | {prob['topic']} |"
    if new_row not in content:
        lines = content.split('\n')
        last = -1
        for i,line in enumerate(lines):
            if line.startswith('|') and any(c.isdigit() for c in line.split('|')[1] if line.count('|')>2):
                last = i
        if last > 0:
            lines.insert(last+1, new_row)
            with open(README_PATH,'w') as f:
                f.write('\n'.join(lines))
            print(f"  ✅ README updated!")

    # Git push
    try:
        os.chdir(DSA_FOLDER)
        subprocess.run(['git','add','.'],check=True)
        r = subprocess.run(['git','commit','-m',f'Day {day}: Solved {prob["name"]}'],capture_output=True,text=True)
        if 'nothing to commit' not in r.stdout:
            subprocess.run(['git','push','origin','master'],check=True)
            print(f"  ✅ Pushed to GitHub! 🎉")
        else:
            print("  📁 Already up to date")
    except Exception as e:
        print(f"  ⚠️ Git error: {e}\n  Run: git pull origin master")

    if day not in progress["completed_days"]:
        progress["completed_days"].append(day)
        save_progress(progress)
    streak = calculate_streak(progress)
    print(f"\n  🎉 Day {day} COMPLETE! Streak: {streak} days!")
    print("  🟩 " * min(streak,15))
    show_notification(f"Day {day} Complete!",f"Streak: {streak} days! Keep going!")

def show_progress(p):
    done = len(p["completed_days"])
    streak = calculate_streak(p)
    pct = int((done/150)*100)
    bar = "█"*(pct//5)+"░"*(20-pct//5)
    print("\n"+"="*55)
    print("  📊 SHESHANDRA'S PROGRESS")
    print("="*55)
    print(f"  ✅ Solved  : {done}/150")
    print(f"  🔥 Streak  : {streak} days")
    print(f"  🎯 Target  : Google ML Engineer 2028")
    print(f"\n  [{bar}] {pct}%")
    print("="*55)

def main():
    print("\n"+"="*55)
    print("  🚀 SHESHANDRA'S DAILY LEETCODE TRACKER")
    print("  🎯 Target: Google ML Engineer 2028")
    print("="*55)
    progress = load_progress()
    day = get_today_day(progress)
    if day not in PROBLEMS:
        print(f"\n  Day {day} problem not added yet! Ask Claude to add more!")
        return
    prob = PROBLEMS[day]
    show_notification(f"Day {day} — LeetCode! 🔥", f"{prob['name']} ({prob['difficulty']})")
    while True:
        print("\n"+"="*55)
        print(f"  🔥 DAY {day} — {prob['name']}")
        print(f"     {prob['difficulty']} | {prob['topic']}")
        print(f"  🔗 {prob['url']}")
        print("-"*55)
        print("  [1] 🌐 Open LeetCode in browser")
        print("  [2] 💡 Show solution + explanation")
        print("  [3] 🚀 Save + Push GitHub + Update README")
        print("  [4] 📊 My progress")
        print("  [5] ❌ Exit")
        print("="*55)
        choice = input("\n  Choice (1-5): ").strip()
        if choice=='1':
            webbrowser.open(prob['url'])
            print("  🌐 LeetCode opened!")
        elif choice=='2':
            show_solution(progress, prob)
        elif choice=='3':
            save_and_push(day, prob, progress)
        elif choice=='4':
            show_progress(progress)
        elif choice=='5':
            print("\n  👋 See you tomorrow! 💪")
            break
        else:
            print("  ⚠️ Enter 1-5!")

if __name__=="__main__":
    main()