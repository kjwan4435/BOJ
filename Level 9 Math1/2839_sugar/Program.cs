using System;
using static System.Console;

namespace _2839_sugar
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(ReadLine());
            int max5 = N / 5;
            int answer = -1;
            for (int i = max5; i >= 0; i--)
            {
                int max3 = (N - 5 * i) / 3;
                if ((i * 5 + max3 * 3) == N)
                {
                    answer = i + max3;
                    break;
                }
            }
            WriteLine(answer);
        }
    }
}
