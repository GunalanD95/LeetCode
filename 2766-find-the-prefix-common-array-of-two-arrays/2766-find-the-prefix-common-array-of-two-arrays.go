func findThePrefixCommonArray(A []int, B []int) []int {
    N := len(A)
    res := make([]int, N)

    a_map := make(map[int]int)
    b_map := make(map[int]int)

    var count = 0
    for i:=0; i < N; i++ {
        a_map[A[i]] += 1
        b_map[B[i]] += 1

        if A[i] !=  B[i]{
            count += a_map[B[i]]
            count += b_map[A[i]]
        }else {
            count += a_map[A[i]]
        }
        res[i] = count
    }
    return res
}