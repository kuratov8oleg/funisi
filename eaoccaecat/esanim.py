def highest_product_of_three(nums):
    nums.sort()
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]
    return max(product1, product2)

# Example usage
nums = [1, 10, 2, 6, 5, 3]
print(highest_product_of_three(nums))  # Output: 300
