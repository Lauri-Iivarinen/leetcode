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

    public int RemoveDuplicates(int[] nums) {
        return 0;
    }

    public int StrStr(string haystack, string needle) {
        return haystack.IndexOf(needle);
    }

    public int[] PlusOne(int[] digits) {
        
        if(digits[digits.Length-1] != 9){
            digits[digits.Length-1] = digits[digits.Length-1]+1;
        }else{
            int i = digits.Length-1;
            while (i > 0 && digits[i] == 9){
                digits[i] = 0;
                i--;
            }

            if (i == 0 && digits[0] == 9){
                //add new
                Array.Resize(ref digits, digits.Length + 1);
                for (int ind = digits.Length-2; ind > 0; ind--){
                    digits[ind+1] = digits[ind];
                }
                digits[0] = 1;
                
            }else{
                digits[i] += 1; 
            }
        }
        
        return digits;
    }

//Do not cut here
}
}