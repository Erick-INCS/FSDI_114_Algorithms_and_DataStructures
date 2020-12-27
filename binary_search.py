
def binary_search(arr, ele):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        mid = (fist+last)/2

        if arr[mid] == ele:
            found = True

        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                fist = mid + 1
    return found

def rec_bin_search(arr, ele):
    if len(arr) == 0:
        return False

    else:
        mid = len(arr)/2
        if arr[mid] == ele:
            return True
        else:
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            else:
                return rec_bin_search(arr[mid+1:], ele)