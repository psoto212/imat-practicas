using System;
using System.Collections.Generic;
using System.Linq;

class Cliente
{
    public string Name;
    public int ArrivalTime;
    public int ServiceTime;
}

class Ventanilla
{
    public string Name;
    private int freeAt;
    private List<int> tiemposEspera;
    private int clients_served;

    public Ventanilla()
    {
        freeAt = 0;
        tiemposEspera = new List<int>();
        clients_served = 0;
    }

    public void AttendNext(Cliente c)
    {
        int inicioAtencion = Math.Max(freeAt, c.ArrivalTime);
        int tiempoEspera = inicioAtencion - c.ArrivalTime;
        freeAt = inicioAtencion + c.ServiceTime;

        tiemposEspera.Add(tiempoEspera);
        clients_served += 1;

        Console.WriteLine($"{Name} atiende a {c.Name} (esperó {tiempoEspera} min)");
    }

    public int ClientsServed()
    {
        return clients_served;
    }

    public double AverageWait()
    {
        if (tiemposEspera.Count == 0)
        {
            return 0;
        }

        return tiemposEspera.Average();
    }

    public int GetFreeAt()
    {
        return freeAt;
    }
}

class Bank
{
    private Dictionary<string, double> balances = new Dictionary<string, double>();
    private Stack<string> OperationHistory = new Stack<string>();

    public void AddClient(string name, double initialBalance)
    {
        balances[name] = initialBalance;
    }

    public void Deposit(string name, double amount)
    {
        if (balances.ContainsKey(name))
        {
            balances[name] += amount;

            OperationHistory.Push("Deposit;" + name + ";" + amount);

            Console.WriteLine($"{name} ingresa {amount}€ -> Saldo: {balances[name]}€");
        }
    }

    public void Withdraw(string name, double amount)
    {
        if (balances.ContainsKey(name) && balances[name] >= amount)
        {
            balances[name] -= amount;

            OperationHistory.Push("Withdraw;" + name + ";" + amount);

            Console.WriteLine(
                $"{name} retira {amount}€ -> Saldo: {balances[name]}€"
            );
        }
    }

    public void UndoLastOperation()
    {
        if (OperationHistory.Count > 0)
        {
            Console.WriteLine("Deshaciendo última operación...");

            string lastOperation = OperationHistory.Pop();
            string[] parts = lastOperation.Split(';');

            string operation = parts[0];
            string name = parts[1];
            double amount = Convert.ToDouble(parts[2]);

            if (operation == "Deposit")
            {
                balances[name] -= amount;

                Console.WriteLine(
                    $"{name}: se deshace el ingreso de {amount}€ -> Saldo: {balances[name]}€"
                );
            }
            else if (operation == "Withdraw")
            {
                balances[name] += amount;

                Console.WriteLine(
                    $"{name}: se deshace la retirada de {amount}€ -> Saldo: {balances[name]}€"
                );
            }
        }
    }
}

class ScenarioResult
{
    public string Name { get; set; }
    public double GlobalAverageWait { get; set; }
    public Ventanilla Ventanilla1 { get; set; }
    public Ventanilla Ventanilla2 { get; set; }
}

class Program
{
    static ScenarioResult RunSeparateQueues(List<Cliente> clients)
    {
        Console.WriteLine();
        Console.WriteLine("=== ESCENARIO 1: una cola por ventanilla ===");

        Queue<Cliente> cola1 = new Queue<Cliente>();
        Queue<Cliente> cola2 = new Queue<Cliente>();

        Ventanilla ventanilla1 = new Ventanilla();
        Ventanilla ventanilla2 = new Ventanilla();

        ventanilla1.Name = "Ventanilla 1";
        ventanilla2.Name = "Ventanilla 2";

        for (int i = 0; i < clients.Count; i++)
        {
            if (i % 2 == 0)
            {
                cola1.Enqueue(clients[i]);
            }
            else
            {
                cola2.Enqueue(clients[i]);
            }
        }

        while (cola1.Count > 0)
        {
            Cliente cliente = cola1.Dequeue();
            ventanilla1.AttendNext(cliente);
        }

        while (cola2.Count > 0)
        {
            Cliente cliente = cola2.Dequeue();
            ventanilla2.AttendNext(cliente);
        }

        ScenarioResult resultado = new ScenarioResult();

        resultado.Name = "Escenario 1 (colas separadas)";
        resultado.Ventanilla1 = ventanilla1;
        resultado.Ventanilla2 = ventanilla2;

        resultado.GlobalAverageWait =
            (ventanilla1.AverageWait() * ventanilla1.ClientsServed()
            + ventanilla2.AverageWait() * ventanilla2.ClientsServed())
            / clients.Count;

        Console.WriteLine(
            $"Ventanilla 1: {ventanilla1.ClientsServed()} clientes, espera media {ventanilla1.AverageWait():F2} min"
        );

        Console.WriteLine(
            $"Ventanilla 2: {ventanilla2.ClientsServed()} clientes, espera media {ventanilla2.AverageWait():F2} min"
        );

        Console.WriteLine(
            $"Espera media global Escenario 1: {resultado.GlobalAverageWait:F2} min"
        );

        return resultado;
    }

    static ScenarioResult RunSharedQueue(List<Cliente> clients)
    {
        Console.WriteLine();
        Console.WriteLine("=== ESCENARIO 2: cola única compartida ===");

        Queue<Cliente> cola = new Queue<Cliente>();

        Ventanilla ventanilla1 = new Ventanilla();
        Ventanilla ventanilla2 = new Ventanilla();

        ventanilla1.Name = "Ventanilla 1";
        ventanilla2.Name = "Ventanilla 2";

        foreach (Cliente cliente in clients)
        {
            cola.Enqueue(cliente);
        }

        while (cola.Count > 0)
        {
            Cliente cliente = cola.Dequeue();

            if (ventanilla1.GetFreeAt() <= ventanilla2.GetFreeAt())
            {
                ventanilla1.AttendNext(cliente);
            }
            else
            {
                ventanilla2.AttendNext(cliente);
            }
        }

        ScenarioResult resultado = new ScenarioResult();

        resultado.Name = "Escenario 2 (cola única)";
        resultado.Ventanilla1 = ventanilla1;
        resultado.Ventanilla2 = ventanilla2;

        resultado.GlobalAverageWait =
            (ventanilla1.AverageWait() * ventanilla1.ClientsServed()
            + ventanilla2.AverageWait() * ventanilla2.ClientsServed())
            / clients.Count;

        Console.WriteLine(
            $"Ventanilla 1: {ventanilla1.ClientsServed()} clientes, espera media {ventanilla1.AverageWait():F2} min"
        );

        Console.WriteLine(
            $"Ventanilla 2: {ventanilla2.ClientsServed()} clientes, espera media {ventanilla2.AverageWait():F2} min"
        );

        Console.WriteLine(
            $"Espera media global Escenario 2: {resultado.GlobalAverageWait:F2} min"
        );

        return resultado;
    }

    static void CompareScenarios(ScenarioResult r1, ScenarioResult r2)
    {
        Console.WriteLine();
        Console.WriteLine("=== COMPARACIÓN FINAL ===");

        Console.WriteLine(
            $"{r1.Name}: espera media {r1.GlobalAverageWait:F2} min"
        );

        Console.WriteLine(
            $"{r2.Name}: espera media {r2.GlobalAverageWait:F2} min"
        );

        if (r1.GlobalAverageWait < r2.GlobalAverageWait)
        {
            Console.WriteLine(
                "-> Las colas separadas han resultado más eficientes en esta simulación."
            );
        }
        else if (r2.GlobalAverageWait < r1.GlobalAverageWait)
        {
            Console.WriteLine(
                "-> La cola única ha resultado más eficiente en esta simulación."
            );
        }
        else
        {
            Console.WriteLine(
                "-> Ambos escenarios tienen la misma espera media."
            );
        }
    }

    static void Main(string[] args)

    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Console.WriteLine("--- Operaciones bancarias ---");

        Bank banco = new Bank();

        banco.AddClient("Laura", 500);
        banco.AddClient("Marcos", 200);
        banco.AddClient("Ana", 300);

        banco.Deposit("Laura", 200);
        banco.Withdraw("Marcos", 50);
        banco.UndoLastOperation();

        List<Cliente> clientes = new List<Cliente>();

        clientes.Add(new Cliente { Name = "Laura", ArrivalTime = 0, ServiceTime = 4 });
        clientes.Add(new Cliente { Name = "Marcos", ArrivalTime = 1, ServiceTime = 6 });
        clientes.Add(new Cliente { Name = "Ana", ArrivalTime = 2, ServiceTime = 2 });
        clientes.Add(new Cliente { Name = "Pedro", ArrivalTime = 3, ServiceTime = 3 });
        clientes.Add(new Cliente { Name = "Sofía", ArrivalTime = 4, ServiceTime = 2 });
        clientes.Add(new Cliente { Name = "Diego", ArrivalTime = 5, ServiceTime = 3 });

        ScenarioResult resultado1 = RunSeparateQueues(clientes);
        ScenarioResult resultado2 = RunSharedQueue(clientes);

        CompareScenarios(resultado1, resultado2);
    }
}