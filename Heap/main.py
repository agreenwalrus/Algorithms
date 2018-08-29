import Heap as heap


def main():
    h = heap.MinHeap(5)
    print(h)



    #h.insert(1, 1)
    #print(h)

    h.insert(1, 1)
    print(h)

    h.insert(2, 2)
    print(h)

    h.insert(3, 3)
    print(h)

    h.insert(1, 1)
    print(h)

    #h.insert(0, 0)
    #print(h)

    h.extract_min()
    print(h)

    h.extract_min()
    print(h)

    h.extract_min()
    print(h)

    h.extract_min()
    print(h)

    h.extract_min()
    print(h)

    h.extract_min()
    print(h)


if __name__ == "__main__":
    main()
