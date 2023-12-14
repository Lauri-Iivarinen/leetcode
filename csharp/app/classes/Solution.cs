namespace app{
public class Solution {
    public bool IsPalindrome(int x) {
        string y = x.ToString();
        int left = 0;
        int right = y.Length -1;
        while (left <= right){
            if (y[left] != y[right]){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public string LongestCommonPrefix(string[] strs) {
        int index = 0;
        string prefixStr = "";
        while (true){
            if (strs[0].Length == 0){
                return "";
            }
            char input = strs[0][index];
            foreach (string str in strs){
                if (prefixStr.Equals(str)){
                    return prefixStr;
                }
                if (!str[index].Equals(input)){
                    return prefixStr;
                } 
            }
            prefixStr += input;
            index++;
            if(prefixStr.Equals(strs[0])){
                return prefixStr;
            }
        }
        
    }

    public bool IsValid(string s) {
        char[] open = {'(', '{', '['};
        char[] close = {')', '}', ']'};
        List<char> openBrackets = new List<char>();
        for(int i = 0; i < s.Length; i++){
            if (Array.IndexOf(open, s[i]) != -1){
                openBrackets.Add(s[i]);
            }else{
                if (openBrackets.Count == 0) return false;
                char bracket = open[Array.IndexOf(close, s[i])];
                if (!openBrackets[(openBrackets.Count-1)].Equals(bracket)){
                    return false;
                }
                openBrackets.RemoveAt(openBrackets.Count-1);
            }
        }
        return openBrackets.Count == 0;
    }
}
}
