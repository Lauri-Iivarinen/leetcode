using System;

namespace app{
    class Program{
        static void Main(string[] args){
            Solution solution = new Solution();
            //Console.WriteLine(solution.StrStr("sadbutsad", "leet"));
            int[] res = solution.PlusOne([1,8]);
            foreach (int i in res){
                Console.WriteLine(i);
            }
           
        }
    }
}