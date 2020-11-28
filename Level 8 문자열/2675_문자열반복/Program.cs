using System;
using static System.Console;

namespace _2675_문자열반복
{
    class Program
    {
        static void Main(string[] args)
        {
            int trial = int.Parse(ReadLine());
            for (int i = 0; i < trial; i++)
            {
                string[] input = ReadLine().Split();
                int n = int.Parse(input[0]);
                string word = input[1];
                for (int j = 0; j < word.Length; j++)
                {
                    for (int k = 0; k < n; k++)
                    {
                        Write(word[j]);
                    }
                }
                Write("\n");
            }
        }
    }
}
