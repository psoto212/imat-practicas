class Device
{
    public string Vendor { get; private set; }
    public string Model { get; private set; }
    public int Year { get; private set; }
    public double Price { get; private set; }

    public Device(string vendor, string model, int year, double price)
    {
        Vendor = vendor;
        Model = model;
        Year = year;
        Price = price;
    }

    public virtual double Garantia()
    {
        return Price * 0.03;
    }
}


class Laptop : Device
{
    public int RAMGB { get; private set; }

    public Laptop(string vendor, string model, int year, double price, int ramGB)
        : base(vendor, model, year, price)
    {
        RAMGB = ramGB;
    }
}


class GamingLaptop : Laptop
{
    public bool DedicatedGPU { get; private set; }
    public bool Overclocked { get; private set; }

    public GamingLaptop(string vendor, string model, int year, double price,
        int ramGB, bool dedicatedGPU, bool overclocked)
        : base(vendor, model, year, price, ramGB)
    {
        DedicatedGPU = dedicatedGPU;
        Overclocked = overclocked;
    }

    public override double Garantia()
    {
        if (Overclocked)
        {
            return base.Garantia() + 100;
        }

        return base.Garantia();
    }
}


class Smartphone : Device
{
    public int StorageGB { get; private set; }
    public bool Is5G { get; private set; }

    public Smartphone(string vendor, string model, int year, double price,
        int storageGB, bool is5G)
        : base(vendor, model, year, price)
    {
        StorageGB = storageGB;
        Is5G = is5G;
    }

    public override double Garantia()
    {
        if (Is5G)
        {
            return base.Garantia() + 50;
        }

        return base.Garantia();
    }
}


class Person
{
    public string Name { get; private set; }
    public int Age { get; private set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}


class Client : Person
{
    public double Budget { get; private set; }
    public List<Device> Devices { get; private set; }

    public Client(string name, int age, double budget)
        : base(name, age)
    {
        Budget = budget;
        Devices = new List<Device>();
    }

    public virtual double PurchasePrice(Device device)
    {
        return device.Price;
    }

    public void BuyDevice(Device device)
    {
        double price = PurchasePrice(device);

        Budget = Budget - price;
        Devices.Add(device);
    }
}


class Student : Client
{
    public Student(string name, int age, double budget)
        : base(name, age, budget)
    {
    }

    public override double PurchasePrice(Device device)
    {
        return device.Price * 0.92;
    }
}


class Seller : Person
{
    public List<Device> SoldDevices { get; private set; }

    private List<double> SoldPrices;

    public Seller(string name, int age)
        : base(name, age)
    {
        SoldDevices = new List<Device>();
        SoldPrices = new List<double>();
    }

    public void SellDevice(Device device, double price)
    {
        SoldDevices.Add(device);
        SoldPrices.Add(price);
    }

    public int TotalUnits()
    {
        return SoldDevices.Count;
    }

    public double TotalSales()
    {
        double total = 0;

        foreach (double price in SoldPrices)
        {
            total = total + price;
        }

        return total;
    }
}

class Program
{
    static void Main()
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        Seller sergio = new Seller("Sergio", 35);
        Seller marta = new Seller("Marta", 29);

        Client diego = new Client("Diego", 45, 3500);
        Student elena = new Student("Elena", 20, 1200);


        Laptop dell = new Laptop(
            "Dell", "XPS 13", 2023, 1200, 16);

        GamingLaptop asus = new GamingLaptop(
            "ASUS", "ROG Strix", 2022, 2200,
            32, true, true);

        Smartphone iphone = new Smartphone(
            "Apple", "iPhone 14", 2022, 999,
            128, true);

        Smartphone samsung = new Smartphone(
            "Samsung", "Galaxy A54", 2023, 450,
            128, false);

        Laptop hp = new Laptop(
            "HP", "Pavilion", 2021, 700, 8);


        if (diego.Budget >= diego.PurchasePrice(asus))
        {
            double price = diego.PurchasePrice(asus);

            diego.BuyDevice(asus);
            sergio.SellDevice(asus, price);

            Console.WriteLine("Sergio vendió ASUS ROG Strix a Diego");
        }


        if (elena.Budget >= elena.PurchasePrice(samsung))
        {
            double price = elena.PurchasePrice(samsung);

            elena.BuyDevice(samsung);
            sergio.SellDevice(samsung, price);

            Console.WriteLine("Sergio vendió Samsung Galaxy A54 a Elena");
        }


        if (diego.Budget >= diego.PurchasePrice(dell))
        {
            double price = diego.PurchasePrice(dell);

            diego.BuyDevice(dell);
            marta.SellDevice(dell, price);

            Console.WriteLine("Marta vendió Dell XPS 13 a Diego");
        }


        if (diego.Budget >= diego.PurchasePrice(iphone))
        {
            double price = diego.PurchasePrice(iphone);

            diego.BuyDevice(iphone);
            marta.SellDevice(iphone, price);

            Console.WriteLine("Marta vendió iPhone 14 a Diego");
        }
        else
        {
            Console.WriteLine(
                "Diego no pudo comprar iPhone 14 (presupuesto insuficiente)");
        }


        if (elena.Budget >= elena.PurchasePrice(hp))
        {
            double price = elena.PurchasePrice(hp);

            elena.BuyDevice(hp);
            marta.SellDevice(hp, price);

            Console.WriteLine("Marta vendió HP Pavilion a Elena");
        }

        Console.WriteLine();
        Console.WriteLine("--- ESTADO DE CLIENTES ---");

        Console.WriteLine(
            DiegoString(diego));

        foreach (Device device in diego.Devices)
        {
            Console.WriteLine(
                "- " + device.Vendor + " " + device.Model +
                " (" + device.Year + ") - " + device.Price + "€");
        }


        Console.WriteLine(
            ElenaString(elena));

        foreach (Device device in elena.Devices)
        {
            Console.WriteLine(
                "- " + device.Vendor + " " + device.Model +
                " (" + device.Year + ")");
        }

        Console.WriteLine();
        Console.WriteLine("--- ESTADO DE VENDEDORES ---");

        Console.WriteLine(
            "Sergio ha vendido " +
            sergio.TotalUnits() +
            " dispositivo(s) por un total de " +
            sergio.TotalSales() + "€"
        );

        Console.WriteLine(
            "Marta ha vendido " +
            marta.TotalUnits() +
            " dispositivo(s) por un total de " +
            marta.TotalSales() + "€"
        );



        Console.WriteLine();
        Console.WriteLine(
            "--- GARANTÍA EXTENDIDA DE DISPOSITIVOS DE DIEGO ---");

        foreach (Device device in diego.Devices)
        {
            Console.WriteLine(
                device.Vendor + " " +
                device.Model + ": " +
                device.Garantia() + "€"
            );
        }
    }


    static string DiegoString(Client client)
    {
        return client.Name +
               " posee " +
               client.Devices.Count +
               " dispositivo(s), Presupuesto restante: " +
               client.Budget + "€";
    }


    static string ElenaString(Client client)
    {
        return client.Name +
               " posee " +
               client.Devices.Count +
               " dispositivo(s), Presupuesto restante: " +
               client.Budget + "€";
    }

}




