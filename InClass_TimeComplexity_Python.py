#Q1

def get_first(data):
    return data[0]

if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))

#Q3

def binarySearch(nums, target):
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


nums_val = [2,4,6,8,10,12]
target_val = 10
result = binarySearch(nums_val,target_val)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present")

#Q4

def sumFirstN(n):
    if n == 0:
        return 0
    
    return sumFirstN(n-1) + n

def main():
    x = int(input('Enter a number: '))
    s= sumFirstN(x)
    print('The sum of the first', x, 'integers are', str(s) + '.')

if __name__ == '__main__':
    main()