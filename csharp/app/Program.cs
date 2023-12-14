using System;

namespace app{
    public class Program{
        public static void Main(string[] args){
            Solution solution = new Solution();
            Console.WriteLine(solution.IsValid("()"));
            Console.WriteLine(solution.IsValid("(("));
            Console.WriteLine(solution.IsValid("("));
            Console.WriteLine(solution.IsValid("(]"));
            Console.WriteLine(solution.IsValid("([]){}"));
        }
    }
}