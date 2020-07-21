using System;
using static System.Console;

namespace _10250_ACM_hotel
{
    class Program
    {
        static void Main(string[] args)
        {
            int trial = int.Parse(ReadLine());
            for (int i = 0; i < trial; i++)
            {
                string[] input = ReadLine().Split();
                int H = int.Parse(input[0]);
                int W = int.Parse(input[1]);
                int N = int.Parse(input[2]);

                int floor = (N % H == 0) ? H : N % H;
                int room_n = (N % H == 0) ? (N / H) : 1 + (N / H);
                if (room_n < 10) { WriteLine("{0}0{1}", floor, room_n); }
                else { WriteLine("{0}{1}", floor, room_n); }

            }
        }
    }
}
