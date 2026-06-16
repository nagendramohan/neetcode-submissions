class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Set<Double> set = new HashSet<>();
        int n = speed.length;
        for(int i=0;i<n;i++){
            double time = (target - position[i])/speed[i];
            set.add(time);
        }

        return set.size();

    }
}