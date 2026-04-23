class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> res = new HashMap<>(); 
        for (int i = 0; i < strs.length; i++) {
            String str = strs[i];
            Map<Character, Integer> freq = new HashMap<>();
            for (char c : str.toCharArray()) {
                freq.put(c, freq.getOrDefault(c,0) + 1);
            }
            res.computeIfAbsent(freq, k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<List<String>>(res.values());
    }
}
