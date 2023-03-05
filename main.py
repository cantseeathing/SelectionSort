def selection_sort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


ex = [2, 1, 7, 6, 5, 3, 4, 9, 8]
selection_sort(customList=ex)
