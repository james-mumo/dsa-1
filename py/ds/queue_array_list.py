def prin(q):
    for i in q:
        print(i)


# make the queue an array
q = [1, 2, 29, 27, 21, 22, 23]

# this is the enqueue
prin(q)

# this is the de queue
q.pop(-1)

prin(q)
