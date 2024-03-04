class solution:
    def mergeSortedArray(self, a1: list[int], m: int, a2: list[int], n: int)->list[int]:
        last = m+n-1
        #merge in reverse order
        while m > 0 and n > 0:
            if a1[m-1] > a2[n-1]:
                a1[last] = a1[m-1]
                m -= 1
            else:
                a1[last] = a2[n-1]
                n -= 1
            last -= 1

        while n>0:
            a1[last] = a2[n-1]
            last, n = last-1, n-1
        return a1


s = solution()
print(s.mergeSortedArray([2, 2, 3, 5, 0, 0, 0], 4, [1, 4, 10], 3))