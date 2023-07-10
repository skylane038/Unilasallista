using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using RabbitMQ.Client;
using System.Threading.Tasks;

namespace Publicador
{
    class Program
    {
        static void Main(string[] args)
        {

            var factory = new ConnectionFactory() { HostName = "fly.rmq.cloudamqp.com" ,
                                                                UserName = "knqwjfhx" ,
                                                                VirtualHost = "knqwjfhx"
            };
            using (var connection = factory.CreateConnection())
            using (var channel = connection.CreateModel())
            {
                channel.ExchangeDeclare(exchange: "videojuegos", type: ExchangeType.Topic);

                var message = GetMessage(args);
                var body = Encoding.UTF8.GetBytes("Disponible en consolas de nueva generacion");
                channel.BasicPublish(exchange: "videojuegos",
                                     routingKey: "warzone",
                                     basicProperties: null,
                                     body: body);
                Console.WriteLine(" [x] Sent {0}", message);
            }

            Console.WriteLine(" Press [enter] to exit.");
            Console.ReadLine();
        }

        private static string GetMessage(string[] args)
        {
            return ((args.Length > 0)
                   ? string.Join(" ", args)
                   : "info: Hello World!");
        }







    }
    }

