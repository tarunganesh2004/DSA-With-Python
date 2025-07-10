import java.util.*;
class generateSubsets{
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3 };
        List<List<Integer>> res = generate(arr);
        System.out.println(res);
    }

    public static List<List<Integer>> generate(int[] arr) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(arr);
        backtrack(res, new ArrayList<>(), arr, 0);
        return res;
    }

    private static void backtrack(List<List<Integer>> res,
            List<Integer> curSubset,int[] arr, int start) {
        res.add(new ArrayList<>(curSubset));
        for (int i = start; i < arr.length; i++) {
            curSubset.add(arr[i]);
            backtrack(res, curSubset, arr, i + 1);
            curSubset.remove(curSubset.size() - 1); // backtrack
        }
    }
}
