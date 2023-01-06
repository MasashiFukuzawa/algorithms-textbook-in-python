import queue

MAX = 10

print('キュー')
q = queue.Queue()
for i in range(MAX):
    q.put(i)
for i in range(MAX):
    print(q.get(), end='->')

print('\n')

print('スタック')
q = queue.LifoQueue()
for i in range(MAX):
    q.put(i)
for i in range(MAX):
    print(q.get(), end='->')
