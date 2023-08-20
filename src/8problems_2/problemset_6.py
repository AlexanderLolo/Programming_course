def TRC_sort(trc: list) -> list:

    if len(trc) < 2:
        return trc

    low = 0
    mid = 0
    hi = len(trc) - 1
    trc1 = [x for x in trc]
    order_sort(trc1, low, mid, hi)

    return trc1


def order_sort(trc: list, low: int, mid: int, hi: int):

    if mid > hi:
        return None

    if trc[low] == 0:
        order_sort(trc, low + 1, mid + 1, hi)

    if trc[low] == 2:
        trc[low], trc[hi] = trc[hi], trc[low]
        order_sort(trc, low, mid, hi-1)

    if trc[low] == 1 and trc[mid] == 1:
        order_sort(trc, low, mid + 1, hi)

    if trc[low] == 1 and trc[mid] == 0:
        trc[low], trc[mid] = trc[mid], trc[low]
        order_sort(trc, low + 1, mid + 1, hi)
        
    if trc[low] == 1 and trc[mid] == 2:
        trc[mid], trc[hi] = trc[hi], trc[mid]
        order_sort(trc, low, mid, hi-1)
