using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace lista
{
    class Program
    {

        class Nodo
        {
            public int valor;
            public Nodo sig;
            public Nodo(int v, Nodo s)
            {
                valor = v;
                sig = s;
            }
        }
        static void Pedir(string m, ref int x)
        {
            Console.Write("{0} ",m);
            x = int.Parse(Console.ReadLine());
        }

        static void Imp(Nodo q)
        {
            while (q != null)
            {
                Console.Write("|| {0} |", q.valor);
                q = q.sig;
            }
        }

        static void CrearNodo(ref Nodo q, int d)
        {
            q = new Nodo(d, q);
            q.sig = null;
        }

        static void InsertaralFinal(ref Nodo l, ref Nodo u)
        {
            int resp = 1, d = 0;
            Nodo p = null;
            while (resp == 1)
            {
                Pedir("De el dato a insertar: ",ref d);
                if (l == null)
                {
                    CrearNodo(ref l, d);
                    u = l;
                }
                else
                {
                    CrearNodo(ref p, d);
                    u.sig = p;
                    u = p;
                }
                Pedir("Hay más datos 1 para seguir 0 para detener: ",ref resp);
           }
        }

        static void Main(string[] args)
        {
            Nodo l = null, u = null;
            InsertaralFinal(ref l, ref u);
            Imp(l);
            Console.ReadKey();
        }

    }
}