// Eximple of sorts for task 5.6

void insertionSort(int *array, int size, int &comparisons, int &movements)
{
    for (int i = 1; i < size; ++i)
    {
        int swap = array[i];
        int j = i - 1;
        while (j >= 0 && swap < array[j])
        {
            array[j + 1] = array[j];
            --j;
        }
        array[j + 1] = swap;
    }
}

void binaryInsertionSort(int *array, int size, int &comparisons, int &movements)
{
    for (int i = 1; i < size; ++i)
    {
        int swap = array[i];
        int left = 0, right = i - 1;
        while (left <= right)
        {
            int mid = (left + right) / 2;
            if (swap < array[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }
        for (int j = i - 1; j >= left; --j)
            array[j + 1] = array[j];
        array[left] = swap;
    }
}

void selectionSort(int *array, int size, int &comparisons, int &movements)
{
    for (int i = 0; i < size - 1; ++i)
    {
        // 'min' -- index of the smallest element which we will find
        int min = i;
        for (int j = i + 1; j < size; ++j)
            if (array[min] > array[j])
                min = j;
        int swap = array[min];
        array[min] = array[i];
        array[i] = swap;
    }
}

void bubbleSort(int *array, int size, int &comparisons, int &movements)
{
    for(int i = 1; i < size; ++i)
    {
        for (int j = size - 1; j >= i; --j)
            if (array[j - 1] > array[j]) {
                int swap = array[j - 1];
                array[j - 1] = array[j];
                array[j] = swap;
            }
    }
}

void quickSort(int *array, int left, int right, int &comparisons, int &movements)
{
    int i = left, j = right;
    // 'mid' -- value of element which locates in middle of array
    int mid = array[(left + right) / 2];
    do
    {
        while (array[i] < mid)
            ++i;
        while (array[j] > mid)
            --j;
        if (i <= j) {
            int swap = array[i];
            array[i] = array[j];
            array[j] = swap;
            ++i;
            --j;
        }
    }
    while(i < j);
    if ( left < j )
        quickSort(array, left, j, comparisons, movements);
    if (i < right)
        quickSort(array, i, right, comparisons, movements);
}
