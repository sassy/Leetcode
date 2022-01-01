use std::convert::TryInto;

pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: &Vec<i32>, target: i32) -> Vec<i32> {
        let mut ret = Vec::<i32>::new();
        for (i, x) in nums.iter().enumerate() {
            for (j, y) in nums.iter().enumerate() {
                if i >= j {
                    continue;
                } else if x + y == target {
                    ret.push(i.try_into().unwrap());
                    ret.push(j.try_into().unwrap());
                }
            }
        }
        println!("{}", target);
        ret
    }
}

fn main() {
    let test_data = vec![2, 7, 11, 15];
    let ret = Solution::two_sum(&test_data, 9);
    println!("{:?}", ret);
    let test_data = vec![3, 2, 3];
    let ret = Solution::two_sum(&test_data, 6);
    println!("{:?}", ret);
}
