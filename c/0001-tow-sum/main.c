#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i, j;
    int *ret = malloc(sizeof(int) * 2);
    for (i = 0; i < numsSize - 1; i++) {
        for (j = i+1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                ret[0] = i;
                ret[1] = j;
                *returnSize = 2;
                return ret;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

void test1() {
    int *nums = malloc(sizeof(int) * 4);
    nums[0] = 2, nums[1] = 7, nums[2] = 11, nums[3]=15;
    int *size = malloc(sizeof(int));
    int *ret = twoSum(nums, 4, 9, size);
    if (ret != NULL) {
        printf("%d, %d\n", ret[0], ret[1]);
        free(ret);
    }
    free(size);
    free(nums);
}

void test2() {
    int *nums = malloc(sizeof(int) * 3);
    nums[0] = 3, nums[1] = 2, nums[2] = 3;
    int *size = malloc(sizeof(int));
    int *ret = twoSum(nums, 3, 6, size);
    if (ret != NULL) {
        printf("%d, %d\n", ret[0], ret[1]);
        free(ret);
    }
    free(size);
    free(nums);
}

int main(int argc, char *argv[]) {
    test1();
    test2();
    return 0;
}