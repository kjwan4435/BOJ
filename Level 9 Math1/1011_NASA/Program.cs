using System;
using static System.Console;

namespace _1011_NASA
{
    class Program
    {
        static void Main(string[] args)
        {
            int trial = int.Parse(ReadLine());

            for (int i = 0; i < trial; i++)
            {
                string[] points = ReadLine().Split();
                int distance = int.Parse(points[1]) - int.Parse(points[0]);
                int counter = 0;

                for (int k = 1; distance > 0;)
                {
                    counter += 1;
                    distance -= k;

                    if (counter % 2 == 0) { k++; }
                }

                WriteLine(counter);
            }
        }
    }
}
