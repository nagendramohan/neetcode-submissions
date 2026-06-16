class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Set<Double> set = new HashSet<>();
        List<Double> list = new ArrayList<>();
        int n = speed.length;
        for(int i=0;i<n;i++){
            double time = (target - position[i])/speed[i];
            list.add(time);
            set.add(time);
        }
        System.out.println(set);
        System.out.println(list);
        return set.size();

    }
}
// // target=12
// // position=[10,8,0,5,3]
// // speed=[2,4,1,1,3]
// [1.0, 1.0, 12.0, 7.0, 3.0]