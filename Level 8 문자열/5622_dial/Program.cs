using System;
using static System.Console;

namespace _5622_dial
{
    class Program
    {
        static void Main(string[] args)
        {
            int time = 0;

            string word = ReadLine().ToUpper(); // input string 대문자 변환
            foreach (char c in word)
            {
                int value = Convert.ToInt32(c);
                if (value <= 67) { time += 3; }
                else if (value <= 70) { time += 4; }
                else if (value <= 73) { time += 5; }
                else if (value <= 76) { time += 6; }
                else if (value <= 79) { time += 7; }
                else if (value <= 83) { time += 8; }
                else if (value <= 86) { time += 9; }
                else if (value <= 90) { time += 10; }
            }
            Write(time);
        }
    }
}
