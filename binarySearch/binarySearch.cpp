//
//  binarySearch.cpp
//  
//
//  Created by Jenwei Peng on 1/25/22.
//

#include "binarySearch.hpp"
#include <vector>

using namespace std;

class BinarySearch {
public:
    int search(vector<int> array, int target) {
        int leftIndex = 0;
        int rightIndex = array.size() - 1;
        
        while (leftIndex <= rightIndex) {
            int middleIndex = (leftIndex + rightIndex) / 2;
            int middleValue = array[middleIndex];
            
            if (target == array[middleIndex]) {
                return middleIndex;
            } else if (target < middleValue) {
                rightIndex = middleIndex - 1;
            } else {
                leftIndex = middle + 1;
            }
        }
        
        return -1;
    }
}
