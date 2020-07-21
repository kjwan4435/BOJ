using System;
using static System.Console;

namespace _2292_beeHouse
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(ReadLine());
            int step = 1;

            if (N != 1)
            {
                N--;
                for (int i = 1; ; i++)
                {
                    step++;
                    N -= 6 * i;
                    if (N <= 0) { break; }
                }
            }
            WriteLine(step);
        }
    }
}
