using System;
using static System.Console;

namespace _2775_apart
{
    class Program
    {
        static void Main(string[] args)
        {
            int trial = int.Parse(ReadLine());
            int[,] population = new int[15, 15];

            for (int i = 0; i < 15; i++)
            {
                population[0, i] = i + 1;
                population[i, 0] = 1;
            }

            for (int i = 1; i < 15; i++)
            {
                for (int j = 1; j < 15; j++)
                {
                    population[i, j] = population[i, j - 1] + population[i - 1, j];
                }
            }

            for (int i = 0; i < trial; i++)
            {
                int k = int.Parse(ReadLine());
                int n = int.Parse(ReadLine());
                WriteLine(population[k, n - 1]);
            }
        }
    }
}
