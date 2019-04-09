from collections import deque
graph = {}
search_queue = deque()
search_queue += graph['you']
def main():
    while search_queue:
        person = search_queue.popleft()
        if 