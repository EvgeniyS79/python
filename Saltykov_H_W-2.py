#не плохо было бы разобрать эту задачу подробнее пошагово,
# я её с 9й строки скопировал и не понял ничего.
# код прислали, но мне важно разобраться и понять.
nums = []
summ1 = 0
summ2 = 0
for i in range(1, 1000, 2):
      nums.append(i**3)
#print(nums)
for idx in range(len(nums)):
    num_sum = 0
    j = nums[idx]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        summ1 += nums[idx]
    nums[idx] += 17
    num_sum = 0
    j = nums[idx]
    while j:
        num_sum += j % 10
        j = j // 10
    if num_sum % 7 == 0:
        summ2 += nums[idx]
print(summ1)  # 17485588610
print(summ2)  # 15392909930

