#!/usr/bin/env python3
"""
AI-Powered Daily LeetCode Automation for Sheshandra
- Shows today's problem automatically
- Opens LeetCode in browser
- Uses Claude AI to generate solution + explanation
- Saves solution to dsa-practice folder
- Auto pushes to GitHub
- Auto updates README
"""

import os
import sys
import json
import datetime
import webbrowser
import subprocess
import time
import urllib.request
import urllib.error

# ============================================================
# CONFIGURATION
# ============================================================
DSA_FOLDER = r"C:\Users\Sheshandra Reddy\OneDrive\Desktop\dsa-practice"
README_PATH = os.path.join(DSA_FOLDER, "README.md")
PROGRESS_FILE = os.path.join(DSA_FOLDER, ".progress.json")

# ============================================================
# LEETCODE PROBLEM SCHEDULE — 150 problems!
# ============================================================
PROBLEMS = [
    (1,  "Two Sum",                             "Easy",   "HashMap",             "https://leetcode.com/problems/two-sum",                                        "two_sum.py",                  "Given an array nums and target, return indices of two numbers that add up to target."),
    (2,  "Valid Parentheses",                   "Easy",   "Stack",               "https://leetcode.com/problems/valid-parentheses",                              "valid_parentheses.py",        "Given a string of brackets, return true if it is valid (every open bracket has a matching close bracket in correct order)."),
    (3,  "Best Time to Buy and Sell Stock",     "Easy",   "Array",               "https://leetcode.com/problems/best-time-to-buy-and-sell-stock",                "best_time_stock.py",          "Given prices array, find maximum profit by buying on one day and selling on a later day."),
    (4,  "Contains Duplicate",                  "Easy",   "HashSet",             "https://leetcode.com/problems/contains-duplicate",                             "contains_duplicate.py",       "Given an integer array, return true if any value appears at least twice."),
    (5,  "Maximum Subarray",                    "Easy",   "Kadane's Algorithm",  "https://leetcode.com/problems/maximum-subarray",                               "maximum_subarray.py",         "Given an integer array, find the subarray with the largest sum and return its sum."),
    (6,  "Reverse Linked List",                 "Easy",   "Linked List",         "https://leetcode.com/problems/reverse-linked-list",                            "reverse_linked_list.py",      "Given the head of a singly linked list, reverse the list and return the reversed list."),
    (7,  "Climbing Stairs",                     "Easy",   "Dynamic Programming", "https://leetcode.com/problems/climbing-stairs",                                "climbing_stairs.py",          "You can climb 1 or 2 steps. Given n steps, how many distinct ways can you climb to the top?"),
    (8,  "Merge Two Sorted Lists",              "Easy",   "Linked List",         "https://leetcode.com/problems/merge-two-sorted-lists",                         "merge_two_lists.py",          "Merge two sorted linked lists and return the merged list sorted."),
    (9,  "Linked List Cycle",                   "Easy",   "Two Pointers",        "https://leetcode.com/problems/linked-list-cycle",                              "linked_list_cycle.py",        "Given head of linked list, determine if it has a cycle using Floyd's algorithm."),
    (10, "Reverse String",                      "Easy",   "Two Pointers",        "https://leetcode.com/problems/reverse-string",                                 "reverse_string.py",           "Write a function that reverses a string in-place. Input is a character array."),
    (11, "Binary Search",                       "Easy",   "Binary Search",       "https://leetcode.com/problems/binary-search",                                  "binary_search.py",            "Given a sorted array and target, return index of target or -1 if not found. Must be O(log n)."),
    (12, "Flood Fill",                          "Easy",   "BFS/DFS",             "https://leetcode.com/problems/flood-fill",                                     "flood_fill.py",               "Given an image (2D array), starting pixel, and new color, flood fill from starting pixel."),
    (13, "Lowest Common Ancestor of BST",       "Easy",   "Binary Search Tree",  "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree", "lowest_common_ancestor.py",   "Find the lowest common ancestor of two nodes in a BST."),
    (14, "Balanced Binary Tree",                "Easy",   "Binary Tree",         "https://leetcode.com/problems/balanced-binary-tree",                           "balanced_binary_tree.py",     "Determine if a binary tree is height-balanced (depth of subtrees never differ by more than 1)."),
    (15, "Diameter of Binary Tree",             "Easy",   "Binary Tree",         "https://leetcode.com/problems/diameter-of-binary-tree",                        "diameter_binary_tree.py",     "Given root of binary tree, return the length of the diameter (longest path between any two nodes)."),
    (16, "Middle of Linked List",               "Easy",   "Linked List",         "https://leetcode.com/problems/middle-of-the-linked-list",                      "middle_linked_list.py",       "Given head of linked list, return the middle node. If two middles, return second."),
    (17, "Maximum Depth of Binary Tree",        "Easy",   "Binary Tree",         "https://leetcode.com/problems/maximum-depth-of-binary-tree",                   "max_depth_binary_tree.py",    "Given root of binary tree, return its maximum depth (number of nodes along longest path)."),
    (18, "First Bad Version",                   "Easy",   "Binary Search",       "https://leetcode.com/problems/first-bad-version",                              "first_bad_version.py",        "Find the first bad version using minimum API calls with binary search."),
    (19, "Ransom Note",                         "Easy",   "HashMap",             "https://leetcode.com/problems/ransom-note",                                    "ransom_note.py",              "Given ransomNote and magazine strings, return true if ransomNote can be constructed from magazine letters."),
    (20, "Move Zeroes",                         "Easy",   "Two Pointers",        "https://leetcode.com/problems/move-zeroes",                                    "move_zeroes.py",              "Move all zeroes to end of array while maintaining relative order of non-zero elements. In-place."),
    (21, "Squares of Sorted Array",             "Easy",   "Two Pointers",        "https://leetcode.com/problems/squares-of-a-sorted-array",                      "squares_sorted_array.py",     "Given sorted array, return sorted array of squares of each number."),
    (22, "Longest Substring Without Repeating", "Medium", "Sliding Window",      "https://leetcode.com/problems/longest-substring-without-repeating-characters", "longest_substring.py",        "Find length of longest substring without repeating characters."),
    (23, "3Sum",                                "Medium", "Two Pointers",        "https://leetcode.com/problems/3sum",                                           "three_sum.py",                "Find all unique triplets in array that sum to zero."),
    (24, "Product of Array Except Self",        "Medium", "Array",               "https://leetcode.com/problems/product-of-array-except-self",                   "product_except_self.py",      "Return array where each element is product of all other elements. No division. O(n)."),
    (25, "Number of Islands",                   "Medium", "BFS/DFS",             "https://leetcode.com/problems/number-of-islands",                              "number_of_islands.py",        "Given 2D grid of 1s (land) and 0s (water), count the number of islands."),
    (26, "Coin Change",                         "Medium", "Dynamic Programming", "https://leetcode.com/problems/coin-change",                                    "coin_change.py",              "Given coins and amount, find fewest coins needed to make up amount. Return -1 if impossible."),
    (27, "Word Search",                         "Medium", "Backtracking",        "https://leetcode.com/problems/word-search",                                    "word_search.py",              "Given 2D board and word, return true if word exists in grid (adjacent cells, no reuse)."),
    (28, "Binary Tree Level Order Traversal",   "Medium", "BFS",                 "https://leetcode.com/problems/binary-tree-level-order-traversal",              "binary_tree_level_order.py",  "Return level order traversal of binary tree nodes as list of lists."),
    (29, "Clone Graph",                         "Medium", "Graph",               "https://leetcode.com/problems/clone-graph",                                    "clone_graph.py",              "Return a deep copy of the graph where each node has val and list of neighbors."),
    (30, "Max Area of Island",                  "Medium", "BFS/DFS",             "https://leetcode.com/problems/max-area-of-island",                             "max_area_island.py",          "Given 2D grid, return maximum area of an island (connected 1s)."),
    (31, "Find Minimum in Rotated Array",       "Medium", "Binary Search",       "https://leetcode.com/problems/find-minimum-in-rotated-sorted-array",           "find_minimum_rotated.py",     "Find minimum element in rotated sorted array in O(log n)."),
    (32, "Search in Rotated Array",             "Medium", "Binary Search",       "https://leetcode.com/problems/search-in-rotated-sorted-array",                 "search_rotated_array.py",     "Search target in rotated sorted array. Return index or -1. Must be O(log n)."),
    (33, "Reorder List",                        "Medium", "Linked List",         "https://leetcode.com/problems/reorder-list",                                   "reorder_list.py",             "Reorder linked list: L0→L1→...→Ln becomes L0→Ln→L1→Ln-1→..."),
    (34, "Remove Nth Node From End",            "Medium", "Linked List",         "https://leetcode.com/problems/remove-nth-node-from-end-of-list",               "remove_nth_node.py",          "Remove nth node from end of linked list in one pass."),
    (35, "Container With Most Water",           "Medium", "Two Pointers",        "https://leetcode.com/problems/container-with-most-water",                      "container_most_water.py",     "Find two lines that together with x-axis forms container holding most water."),
    (36, "Combination Sum",                     "Medium", "Backtracking",        "https://leetcode.com/problems/combination-sum",                                "combination_sum.py",          "Find all unique combinations of candidates that sum to target. Same number can be chosen unlimited times."),
    (37, "Unique Paths",                        "Medium", "Dynamic Programming", "https://leetcode.com/problems/unique-paths",                                   "unique_paths.py",             "Robot in m x n grid. Count unique paths from top-left to bottom-right moving only right or down."),
    (38, "House Robber",                        "Medium", "Dynamic Programming", "https://leetcode.com/problems/house-robber",                                   "house_robber.py",             "Rob houses without alerting police (no adjacent houses). Return maximum amount you can rob."),
    (39, "Jump Game",                           "Medium", "Greedy",              "https://leetcode.com/problems/jump-game",                                      "jump_game.py",                "Given array of jump lengths, determine if you can reach the last index."),
    (40, "Rotate Image",                        "Medium", "Array",               "https://leetcode.com/problems/rotate-image",                                   "rotate_image.py",             "Rotate n x n matrix 90 degrees clockwise. Must do it in-place."),
    (41, "Group Anagrams",                      "Medium", "HashMap",             "https://leetcode.com/problems/group-anagrams",                                 "group_anagrams.py",           "Given array of strings, group anagrams together. Order doesn't matter."),
    (42, "Top K Frequent Elements",             "Medium", "Heap",                "https://leetcode.com/problems/top-k-frequent-elements",                        "top_k_frequent.py",           "Given array and k, return k most frequent elements. Order doesn't matter."),
    (43, "Longest Consecutive Sequence",        "Medium", "HashSet",             "https://leetcode.com/problems/longest-consecutive-sequence",                   "longest_consecutive.py",      "Find length of longest consecutive elements sequence in unsorted array. Must be O(n)."),
    (44, "Valid Sudoku",                        "Medium", "Array",               "https://leetcode.com/problems/valid-sudoku",                                   "valid_sudoku.py",             "Determine if 9x9 Sudoku board is valid based on filled cells only."),
    (45, "Spiral Matrix",                       "Medium", "Array",               "https://leetcode.com/problems/spiral-matrix",                                  "spiral_matrix.py",            "Return all elements of m x n matrix in spiral order."),
    (46, "Set Matrix Zeroes",                   "Medium", "Array",               "https://leetcode.com/problems/set-matrix-zeroes",                              "set_matrix_zeroes.py",        "If element is 0, set its entire row and column to 0. Do it in-place."),
    (47, "Pacific Atlantic Water Flow",         "Medium", "BFS/DFS",             "https://leetcode.com/problems/pacific-atlantic-water-flow",                    "pacific_atlantic.py",         "Find cells where water can flow to both Pacific and Atlantic oceans."),
    (48, "Course Schedule",                     "Medium", "Graph",               "https://leetcode.com/problems/course-schedule",                                "course_schedule.py",          "Given numCourses and prerequisites, determine if you can finish all courses (detect cycle)."),
    (49, "Number of Connected Components",      "Medium", "Graph",               "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph", "connected_components.py", "Count connected components in undirected graph with n nodes."),
    (50, "LRU Cache",                           "Medium", "Design",              "https://leetcode.com/problems/lru-cache",                                      "lru_cache.py",                "Design LRU Cache with get and put operations both in O(1) time."),
]


# ============================================================
# PROGRESS MANAGEMENT
# ============================================================
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {
        "completed_days": [1, 2, 3, 4, 5, 6, 7, 8, 9,],
        "start_date": "2026-04-27"
    }


def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)


def get_today_day(progress):
    """Get next uncompleted day — based on problems done, not calendar"""
    completed = progress["completed_days"]
    if not completed:
        return 1
    return max(completed) + 1


def calculate_streak(progress):
    if not progress["completed_days"]:
        return 0
    completed = sorted(progress["completed_days"])
    streak = 1
    for i in range(len(completed) - 1, 0, -1):
        if completed[i] - completed[i - 1] == 1:
            streak += 1
        else:
            break
    return streak


# ============================================================
# AI SOLUTION GENERATOR — Uses Claude API
# ============================================================
def generate_ai_solution(problem_name, description, topic):
    """Call Claude API to generate solution + explanation"""
    print("\n  🤖 Asking Claude AI to generate solution...")

    prompt = f"""You are helping a BTech ECE student learn Python and DSA for Google interviews.

Problem: {problem_name}
Topic: {topic}
Description: {description}

Generate a clean Python3 LeetCode solution with:
1. The complete Solution class with correct method
2. Clear comments explaining each step
3. Time and space complexity at the bottom

Format exactly like this:
```python
from typing import List, Optional

class Solution:
    def methodName(self, ...):
        # Step 1: explanation
        # Step 2: explanation
        # your code here
        pass

# Time Complexity: O(?)
# Space Complexity: O(?)
# Pattern used: {topic}
```

Only output the code block. No other text."""

    try:
        import urllib.request
        import json as json_module

        data = json_module.dumps({
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1000,
            "messages": [{"role": "user", "content": prompt}]
        }).encode('utf-8')

        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=data,
            headers={
                "Content-Type": "application/json",
                "anthropic-version": "2023-06-01",
                "x-api-key": "YOUR_API_KEY_HERE"
            }
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json_module.loads(response.read().decode('utf-8'))
            raw = result['content'][0]['text']

            # Extract code from markdown block
            if '```python' in raw:
                code = raw.split('```python')[1].split('```')[0].strip()
            else:
                code = raw.strip()
            return code

    except Exception as e:
        print(f"  ⚠️ AI generation failed: {e}")
        print("  💡 Using template instead...")
        return f"""from typing import List, Optional

class Solution:
    def solve(self):
        # TODO: Paste your accepted LeetCode solution here!
        # Problem: {problem_name}
        # Topic: {topic}
        # Hint: {description}
        pass

# Time Complexity: O(?)
# Space Complexity: O(?)
# Pattern: {topic}
"""


# ============================================================
# FILE & GITHUB OPERATIONS
# ============================================================
def create_solution_file(day, problem_name, filename, description, topic):
    """Create solution file with AI-generated code"""
    filepath = os.path.join(DSA_FOLDER, filename)

    # Generate AI solution
    ai_code = generate_ai_solution(problem_name, description, topic)

    file_content = f"""# Day {day}: {problem_name}
# Date: {datetime.date.today()}
# Difficulty: See README
# Topic: {topic}
# LeetCode: https://leetcode.com/problems/{filename.replace('_', '-').replace('.py', '')}
# Status: ✅ Accepted
#
# ============================================================
# SOLUTION
# ============================================================

{ai_code}
"""
    with open(filepath, 'w') as f:
        f.write(file_content)

    print(f"  ✅ Solution file created: {filename}")
    return filepath


def update_readme(day, problem_name, difficulty, topic):
    """Auto update README table"""
    with open(README_PATH, 'r') as f:
        content = f.read()

    new_row = f"| {day} | {problem_name} | {difficulty} | {topic} |"

    if new_row in content:
        print(f"  ✅ README already updated for Day {day}")
        return

    lines = content.split('\n')
    new_lines = []
    last_table_row = -1

    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.startswith('|') and '|' in line:
            parts = line.split('|')
            if len(parts) > 1 and any(char.isdigit() for char in parts[1]):
                last_table_row = i

    if last_table_row > 0:
        new_lines.insert(last_table_row + 1, new_row)
        with open(README_PATH, 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"  ✅ README updated: Day {day} — {problem_name}")
    else:
        print("  ⚠️ Couldn't find table. Update README manually.")


def git_push(day, problem_name):
    """Auto push to GitHub"""
    print(f"\n  🚀 Pushing to GitHub...")
    try:
        os.chdir(DSA_FOLDER)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        result = subprocess.run(
            ['git', 'commit', '-m', f'Day {day}: Solved {problem_name}'],
            capture_output=True, text=True
        )
        if 'nothing to commit' in result.stdout:
            print("  📁 Nothing new to commit!")
        else:
            # Try push, if rejected do pull first
            push = subprocess.run(
                ['git', 'push', 'origin', 'master'],
                capture_output=True, text=True
            )
            if 'rejected' in push.stderr:
                print("  🔄 Pulling first...")
                subprocess.run(['git', 'pull', '--rebase', 'origin', 'master'],
                               capture_output=True)
                subprocess.run(['git', 'push', 'origin', 'master'], check=True,
                               capture_output=True)
            print(f"  ✅ Pushed Day {day} to GitHub! 🎉")
    except Exception as e:
        print(f"  ⚠️ Git error: {e}")


def show_notification(title, message):
    """Show Windows toast notification"""
    try:
        subprocess.run([
            'powershell', '-Command',
            f'''
            Add-Type -AssemblyName System.Windows.Forms
            $n = New-Object System.Windows.Forms.NotifyIcon
            $n.Icon = [System.Drawing.SystemIcons]::Information
            $n.Visible = $true
            $n.ShowBalloonTip(8000, "{title}", "{message}", [System.Windows.Forms.ToolTipIcon]::Info)
            Start-Sleep -Seconds 2
            $n.Dispose()
            '''
        ], capture_output=True)
    except Exception:
        print(f"\n  🔔 {title}: {message}")


# ============================================================
# UI
# ============================================================
def show_progress(progress):
    completed = len(progress["completed_days"])
    streak = calculate_streak(progress)
    pct = int((completed / 150) * 100)
    bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
    print("\n" + "=" * 58)
    print("  📊 SHESHANDRA'S GOOGLE JOURNEY — PROGRESS")
    print("=" * 58)
    print(f"  ✅ Problems solved  : {completed} / 150")
    print(f"  🔥 Current streak   : {streak} days")
    print(f"  🎯 Goal             : Google ML Engineer 2028")
    print(f"  🏆 Salary target    : ₹30-50 LPA")
    print(f"\n  Progress: [{bar}] {pct}%")
    print("=" * 58)


def show_menu(day, problem):
    day_num, name, difficulty, topic, url, filename, desc = problem
    print("\n" + "=" * 58)
    print(f"  🔥 DAY {day} — SHESHANDRA'S GOOGLE JOURNEY")
    print("=" * 58)
    print(f"  📌 Problem   : {name}")
    print(f"  💡 Difficulty: {difficulty}")
    print(f"  🧠 Topic     : {topic}")
    print(f"  🔗 URL       : {url}")
    print("\n" + "-" * 58)
    print("  [1] 🌐 Open LeetCode problem in browser")
    print("  [2] 🤖 Generate AI solution + Save to VS Code")
    print("  [3] 🚀 Mark Accepted + Push GitHub + Update README")
    print("  [4] 📊 Show my progress dashboard")
    print("  [5] ❌ Exit")
    print("=" * 58)


def main():
    print("\n" + "=" * 58)
    print("  🚀 SHESHANDRA'S AI-POWERED LEETCODE TRACKER")
    print("  🎯 Target: Google ML Engineer | ₹30-50 LPA")
    print("=" * 58)

    progress = load_progress()
    day = get_today_day(progress)

    # Find today's problem
    today_problem = None
    for p in PROBLEMS:
        if p[0] == day:
            today_problem = p
            break

    if not today_problem:
        idx = min(day - 1, len(PROBLEMS) - 1)
        p = PROBLEMS[idx]
        today_problem = (day,) + p[1:]

    day_num, name, difficulty, topic, url, filename, desc = today_problem

    # Windows notification
    show_notification(
        f"🔥 Day {day} — Time to Code!",
        f"{name} ({difficulty}) | Keep the streak alive!"
    )

    while True:
        show_menu(day, today_problem)
        choice = input("\n  Enter choice (1-5): ").strip()

        if choice == '1':
            print(f"\n  🌐 Opening {name} on LeetCode...")
            webbrowser.open(url)
            print("  ✅ LeetCode opened! Solve it, then come back and press 3.")

        elif choice == '2':
            filepath = create_solution_file(day, name, filename, desc, topic)
            print(f"\n  📝 Opening solution in VS Code...")
            try:
                subprocess.run(['code', filepath])
                print("  ✅ File opened in VS Code!")
                print("  📖 Study the AI solution, understand it, then submit on LeetCode!")
            except Exception:
                print(f"  ✅ File saved at: {filepath}")
                print("  Open it manually in VS Code!")

        elif choice == '3':
            print(f"\n  🎉 Great job solving Day {day}!")
            update_readme(day, name, difficulty, topic)
            git_push(day, name)
            if day not in progress["completed_days"]:
                progress["completed_days"].append(day)
                save_progress(progress)
            streak = calculate_streak(progress)
            print(f"\n  🔥 Streak: {streak} days! 🟩" * 1)
            show_notification(
                f"🎉 Day {day} Complete!",
                f"Streak: {streak} days! One step closer to Google!"
            )
            print(f"\n  Next problem: Day {day + 1}!")
            print("  See you tomorrow Sheshandra! 💪")
            break

        elif choice == '4':
            show_progress(progress)

        elif choice == '5':
            print("\n  👋 Keep the streak alive! See you tomorrow! 💪")
            break

        else:
            print("\n  ⚠️ Enter 1 to 5 only!")


if __name__ == "__main__":
    main()