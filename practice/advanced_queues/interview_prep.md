# Queue-based Interview Problems

This is a list of common interview problems that utilize queues or deques.

## Fundamental Level
1. **Implement Queue using Stacks**: (Implemented in `practice/stacks/queue_using_two_stacks.py`)
2. **Reverse First K elements of Queue**: Use a stack to reverse the first K elements.
3. **Generate Binary Numbers from 1 to N**: Use a queue to generate strings "1", "10", "11", "100", etc.

## Intermediate Level
1. **LRU Cache**: (Implemented in `practice/queues/lru_cache.py`)
2. **First Non-repeating Character in a Stream**: Use a queue and a frequency hash map.
3. **Sliding Window Maximum**: (Implemented in `practice/queues/sliding_window_max.py`)
4. **Binary Tree Level Order Traversal**: Classic BFS application.

## Advanced Level
1. **Rotten Oranges**: (Implemented in `practice/queues/rotten_oranges.py`)
2. **Shortest Path in Binary Matrix**: (Implemented concept in `practice/advanced_queues/maze_solver.py`)
3. **Sliding Window Median**: Requires two heaps or a balanced BST, but can be conceptualized with deques.
4. **Casting Vote Problem**: Simulation using circular queues.

## System Design Concepts
1. **Pub/Sub Systems**: (Implemented concept in `practice/advanced_queues/message_queue.py`)
2. **Rate Limiters**: Token Bucket or Leaky Bucket algorithms often use queues.
3. **Task Schedulers**: Priority queues or time-bucketed queues.
