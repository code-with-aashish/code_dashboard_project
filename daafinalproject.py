import heapq
from collections import defaultdict
import time
import matplotlib.pyplot as plt

# UnionFind class for Kruskal's MST
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's MST
def kruskal_mst(graph, vertices):
    edges = sorted(graph, key=lambda x: x[2])  # Sort edges by weight
    uf = UnionFind(vertices)
    mst = []
    mst_cost = 0

    print("Executing Kruskal’s MST Algorithm")
    for u, v, weight in edges:
        print(f"Checking edge ({u}, {v}) with weight {weight}")
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            mst_cost += weight
            print(f"Added edge ({u}, {v}) to MST")

    print(f"MST Completed with cost: {mst_cost}")
    return mst, mst_cost

# Fractional Knapsack
def fractional_knapsack(values, weights, capacity):
    items = [(values[i] / weights[i], values[i], weights[i]) for i in range(len(values))]
    items.sort(reverse=True, key=lambda x: x[0])  # Sort by value-to-weight ratio

    total_value = 0
    print("Executing Fractional Knapsack Algorithm")
    for ratio, value, weight in items:
        if capacity >= weight:
            print(f"Taking full item with weight {weight} and value {value}")
            total_value += value
            capacity -= weight
        else:
            print(f"Taking {capacity} out of {weight} with value {ratio * capacity}")
            total_value += ratio * capacity
            break

    print(f"Total value for given capacity: {total_value}")
    return total_value

# Activity Selection
def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])  # Sort by finish time
    selected_activities = [0]  # Initialize with the first activity
    last_finish = activities[0][1]
    
    print("Executing Activity Selection Algorithm")
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish:
            selected_activities.append(i)
            last_finish = activities[i][1]
            print(f"Selected activity {i} with start {activities[i][0]} and finish {activities[i][1]}")

    print(f"Total activities selected: {len(selected_activities)}")
    return selected_activities

# Huffman Coding
class HuffmanNode:
    def __init__(self, freq, char=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [HuffmanNode(freq, char) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    print("Building Huffman Tree")
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]  # Root node of the Huffman Tree

def generate_huffman_codes(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        print(f"Character: {root.char}, Code: {current_code}")
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

def huffman_coding(char_freq):
    root = build_huffman_tree(char_freq)
    codes = {}
    generate_huffman_codes(root, "", codes)
    return codes

# Job Sequencing with Deadlines
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs, max_deadline):
    jobs.sort(key=lambda x: x.profit, reverse=True)  # Sort by profit in descending order
    result = [None] * max_deadline
    total_profit = 0

    print("Executing Job Sequencing with Deadlines")
    for job in jobs:
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if result[slot] is None:
                result[slot] = job.job_id
                total_profit += job.profit
                print(f"Job {job.job_id} scheduled at slot {slot} with profit {job.profit}")
                break

    print(f"Total Profit: {total_profit}")
    return result, total_profit

# Comparison Function with Plotting
def compare_all_algorithms():
    # Data for Kruskal's MST
    graph = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    vertices = 4

    # Data for Fractional Knapsack
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    # Data for Activity Selection
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]

    # Data for Huffman Coding
    char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}

    # Data for Job Sequencing with Deadlines
    jobs = [Job('a', 2, 100), Job('b', 1, 19), Job('c', 2, 27), Job('d', 1, 25), Job('e', 3, 15)]
    max_deadline = 3

    print("\nComparing Greedy Algorithms\n")

    # Dictionary to store execution times
    times = {}
    
    # Kruskal's MST
    start_time = time.time()
    mst, mst_cost = kruskal_mst(graph, vertices)
    times['Kruskal'] = time.time() - start_time
    print(f"Kruskal’s MST Result: {mst}, Cost: {mst_cost}, Time: {times['Kruskal']:.6f} seconds\n")

    # Fractional Knapsack
    start_time = time.time()
    knapsack_value = fractional_knapsack(values, weights, capacity)
    times['Knapsack'] = time.time() - start_time
    print(f"Fractional Knapsack Value: {knapsack_value}, Time: {times['Knapsack']:.6f} seconds\n")

    # Activity Selection
    start_time = time.time()
    selected_activities = activity_selection(start, finish)
    times['Activity Selection'] = time.time() - start_time
    print(f"Selected Activities: {selected_activities}, Time: {times['Activity Selection']:.6f} seconds\n")

    # Huffman Coding
    start_time = time.time()
    huffman_codes = huffman_coding(char_freq)
    times['Huffman Coding'] = time.time() - start_time
    print(f"Huffman Codes: {huffman_codes}, Time: {times['Huffman Coding']:.6f} seconds\n")

    # Job Sequencing with Deadlines
    start_time = time.time()
    scheduled_jobs, total_profit = job_sequencing_with_deadlines(jobs, max_deadline)
    times['Job Sequencing'] = time.time() - start_time
    print(f"Job Sequencing Result: {scheduled_jobs}, Total Profit: {total_profit}, Time: {times['Job Sequencing']:.6f} seconds\n")

    # Plotting Execution Times
    algorithms = list(times.keys())
    execution_times = list(times.values())
    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, execution_times, color='skyblue')
    plt.xlabel('Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison of Greedy Algorithms')
    plt.show()

    # Plotting Knapsack Value
    plt.figure(figsize=(10, 6))
    plt.bar(['Fractional Knapsack'], [knapsack_value], color='green')
    plt.xlabel('Algorithm')
    plt.ylabel('Total Value')
    plt.title('Total Value of Fractional Knapsack Solution')
    plt.show()

    # Plotting Job Sequencing Profit
    plt.figure(figsize=(10, 6))
    plt.bar(['Job Sequencing'], [total_profit], color='orange')
    plt.xlabel('Algorithm')
    plt.ylabel('Total Profit')
    plt.title('Total Profit from Job Sequencing with Deadlines')
    plt.show()

# Execute the comparison with plots
compare_all_algorithms()
