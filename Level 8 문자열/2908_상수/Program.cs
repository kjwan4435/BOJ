using System;
using static System.Console;

namespace _2908_상수
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] inputSTR = ReadLine().Split();
            int[] input = new int[2];
            input[0] = int.Parse(inputSTR[0]);
            input[1] = int.Parse(inputSTR[1]);
            int reversed_1 = (input[0] / 100) + (input[0] % 100 / 10) * 10 + (input[0] % 10) * 100;
            int reversed_2 = (input[1] / 100) + (input[1] % 100 / 10) * 10 + (input[1] % 10) * 100;
            WriteLine(Math.Max(reversed_1, reversed_2));
        }
    }
}
