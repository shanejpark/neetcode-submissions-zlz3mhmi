class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> targets = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (targets.get(num) != null) {
                return new int[] {targets.get(num), i};
            }
            targets.put(target - num, i);
        }
        return new int[0];
    }
}
