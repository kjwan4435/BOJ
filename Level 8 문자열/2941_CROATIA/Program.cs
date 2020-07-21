using System;
using System.Linq;
using static System.Console;

namespace _2941_CROATIA
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;
            string input = ReadLine();
            char[] inputArr;
            inputArr = input.ToCharArray();
            count += (input.Split("c=").Length - 1);
            count += (input.Split("c-").Length - 1);
            count += (input.Split("dz=").Length - 1);
            count += (input.Split("d-").Length - 1);
            count += (input.Split("lj").Length - 1);
            count += (input.Split("nj").Length - 1);
            count += (input.Split("s=").Length - 1);
            count += (input.Split("z=").Length - 1);
            WriteLine(input.Length - count);
        }
    }
}
