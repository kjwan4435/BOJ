using System;
using System.Linq;
using static System.Console;

namespace _1316_groupWord
{
    class Program
    {
        static void Main(string[] args)
        {
            int trial = int.Parse(ReadLine());
            int counter = 0;
            for (int i = 0; i < trial; i++)
            {
                string word = ReadLine();
                for (int j = 0; j < word.Length;)
                {
                    int count = word.Count(x => x == word[j]);
                    string repeated = new String(word[j], count);
                    if (word.Split(repeated).Length == 2)
                    {
                        j += count;
                        if (j == word.Length) { counter += 1; }
                    }
                    else { break; }

                }
            }
            WriteLine(counter);
        }
    }
}
