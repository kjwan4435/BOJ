using System;
using System.Linq;
using static System.Console;


namespace _1157_FreqWord
{
    class Program
    {
        static void Main(string[] args)
        {
            int maxFreq = 0;
            int[] freq = Enumerable.Repeat(0, 32).ToArray(); // 32개의 0값을 가지는 배열 생성
            string word = ReadLine().ToUpper(); // input string 대문자 변환
            foreach (char c in word)
            {
                int value = Convert.ToInt32(c);
                freq[value - 65] += 1;
            }
            maxFreq = freq.Max();
            int index_Fword = Array.IndexOf(freq, maxFreq);
            int index_Lword = Array.LastIndexOf(freq, maxFreq);
            if (index_Fword == index_Lword)
            {
                WriteLine(Convert.ToChar(index_Fword + 65));
            }
            else
            {
                WriteLine("?");
            }
        }
    }
}
