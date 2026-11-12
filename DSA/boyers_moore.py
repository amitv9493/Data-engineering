def main(nums: list[int]):
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


print(
    main(
        [
            1,
            2,
            3,
            4,
            5,
        ]
    )
)
