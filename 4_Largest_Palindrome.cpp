// https://projecteuler.net/problem=4

/*
Correct Answer: 906609
*/

#include <iostream>
#include <cmath>
#include <vector>

#define DIGITS 3

using namespace std;   

bool isPalindrome(int num) {

    int n = 0;
    int num_cpy = num;

    while (num > 0) {
        n = n * 10 + num % 10;
        num = num / 10 | 0;
    }
    return n == num_cpy;
}

//Correct but ugly
int main() {
    int start = pow(10, DIGITS-1);
    int end = pow(10, DIGITS) - 1;
    int lp = 0;

    //Walk through range backwards
    for (size_t i = end; i >= start; i--) {
        for (size_t j = end; j >= start; j--) {
            int num = i * j;
            if (isPalindrome(num) && num > lp) {
                lp = num;
            }
        }
    }
    
    cout << "Largest Palidrome Found: " << lp << endl;

    return 0;
}