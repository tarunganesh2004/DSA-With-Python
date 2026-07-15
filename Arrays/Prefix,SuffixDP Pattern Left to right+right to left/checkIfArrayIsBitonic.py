# check if array is bitonic

arr = [1, 2, 5, 7, 6, 4, 2]


def isBitonic(arr):

    phase = "inc"

    for i in range(1, len(arr)):

        if phase == "inc":

            if arr[i] > arr[i - 1]:
                continue
            else:
                phase = "dec"

        if phase == "dec":

            if arr[i] < arr[i - 1]:
                continue
            else:
                return False

    return True


print(isBitonic(arr))