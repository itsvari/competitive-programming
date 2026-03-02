class Solution {

    public int getMinSwaps(String num, int k) {
        char[] current = num.toCharArray();
        char[] target = num.toCharArray();

        for (int i = 0; i < k; i++) {
            nextPermutation(target);
        }

        return countSwaps(current, target);
    }

    private void nextPermutation(char[] arr) {
        int n = arr.length;

        int i = n - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            i--;
        }

        if (i < 0) {
            return;
        }

        int j = n - 1;
        while (j > i && arr[j] <= arr[i]) {
            j--;
        }

        swap(arr, i, j);

        reverse(arr, i + 1, n - 1);
    }

    private int countSwaps(char[] current, char[] target) {
        char[] tmp = current.clone();
        int swaps = 0;

        for (int i = 0; i < tmp.length; i++) {
            if (tmp[i] == target[i]) {
                continue;
            }

            int j = i + 1;
            while (j < tmp.length && tmp[j] != target[i]) {
                j++;
            }

            while (j > i) {
                swap(tmp, j, j - 1);
                j--;
                swaps++;
            }
        }

        return swaps;
    }

    private void swap(char[] arr, int i, int j) {
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private void reverse(char[] arr, int start, int end) {
        while (start < end) {
            swap(arr, start, end);
            start++;
            end--;
        }
    }
}
