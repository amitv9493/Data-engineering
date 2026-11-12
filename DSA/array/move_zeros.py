def main(nums: list[int]):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1

    return nums


print(
    main(
        [
            1,
            0,
            0,
            0,
            4,
        ]
    )
)
