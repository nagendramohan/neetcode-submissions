int findMin(vector<int> arr){
    int left = 0, right = arr.size()-1;
    
    while(left < right){
        int mid = left + (right-left)/2; // if arr size is even or odd;
        if(arr[mid] > arr[right]){ 6 > 1
            left = mid + 1;  4, 4
        }
        else{
            right = mid;
        }
    }
    
    return arr[left];
}