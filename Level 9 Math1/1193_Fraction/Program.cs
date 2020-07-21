using System;
using static System.Console;

namespace _1193_Fraction
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = int.Parse(ReadLine());
            int nominator = 0;
            int denominator = 0;
            for (int i = 0; N - i > 0; i++)
            {
                N -= i;
                if ((N - i - 1) <= 0 && (i % 2 == 1))
                {
                    denominator = N;
                    nominator = i + 2 - N;
                }
                else if ((N - i - 1) <= 0 && (i % 2 == 0))
                {
                    denominator = i + 2 - N;
                    nominator = N;
                }
            }
            WriteLine("{0}/{1}", denominator, nominator);
        }
    }
}
