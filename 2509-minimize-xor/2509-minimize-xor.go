func countSetBits(num int) int {
    count := 0
    for i := 0; i < 32; i++ {
        mask := 1 << i
        if mask&num != 0 { 
            count++
        }
    }
    return count
}

func setMinBit(num int, count int) int {
    res := 0
    for i := 31; i >= 0; i-- {
        if count == 0 {
            break
        }
        mask := 1 << i
        if mask&num != 0 { 
            res |= mask
            count--
        }
    }

    for i := 0; i < 32; i++ {
        if count == 0 {
            break
        }
        mask := 1 << i
        if res&mask == 0 {
            res |= mask
            count--
        }
    }
    return res
}

func minimizeXor(num1 int, num2 int) int {
    count := countSetBits(num2)
    return setMinBit(num1, count)
}

