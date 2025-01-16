func xorAllNums(nums1 []int, nums2 []int) int {
    res := 0
    nums1_xor := 0
    nums2_xor := 0
    for _,num := range(nums1){
        nums1_xor ^= num
    }
    for _,num := range(nums2){
        nums2_xor ^= num
    }

    if len(nums1) % 2 != 0{
        res ^= nums2_xor
    }
    if len(nums2) % 2 != 0{
        res ^= nums1_xor
    }
    return res
}