import Heap as heap


def main():


    h = heap.MinHeap(1000)

    h.insert(2, 2)
    h.insert(3, 3)
    h.insert(5, 5)

    last = 0
    for _ in range(0, 20):
        i, el = h.extract_min()

        if last != el:
            last = el
            print(str(_) + ". " + str(el) + ", ")
            h.insert(2 * el, 2 * el)
            h.insert(3 * el, 3 * el)
            h.insert(5 * el, 5 * el)






if __name__ == "__main__":
    main()
