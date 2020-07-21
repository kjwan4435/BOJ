using System;
using static System.Console;

namespace _2869_snail
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = ReadLine().Split();
            int A = int.Parse(input[0]);
            int B = int.Parse(input[1]);
            int V = int.Parse(input[2]);
            int answer = 0;
            if (V - A <= 0)
            {
                WriteLine(1);
            }
            else
            {
                answer = (V - A) / (A - B) + 1;
                if ((V - A) % (A - B) != 0) { answer += 1; }

                WriteLine(answer);
            }
        }
    }
}
