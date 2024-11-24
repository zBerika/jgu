import random
import string

def read_orders_from_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

class VINGenerator:
    @staticmethod
    def generate_vin():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))

class Qarxana:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        return f"{self.name} - {self.location}"

class Client:
    def __init__(self, customer_name, customer_id):
        self.customer_name = customer_name
        self.customer_id = customer_id

class Engine:
    def __init__(self, engine_type, volume, h_p):
        self.engine_type = engine_type
        self.volume = volume
        self.h_p = h_p

    def display_info(self):
        return f"{self.engine_type}-{self.volume}L, {self.h_p} h.p."

class Car:
    def __init__(self, qarxana, model, color, year, engine: Engine, client: Client, car_type):
        self.qarxana = qarxana
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.client = client
        self.car_type = car_type
        self.vin = VINGenerator.generate_vin()  # Генерация VIN-кода

    def display_info(self):
        return f"{self.year} {self.model} {self.color}, Qarxana: {self.qarxana.display_info()}, Engine: {self.engine.display_info()}"

class Ford(Car):
    pass

class Toyota(Car):
    pass

class Nissan(Car):
    pass

class Chevrolet(Car):
    pass

class Honda(Car):
    pass

created_cars = []

def create_cars_from_orders(orders):
    global created_cars
    created_cars = []

    factories = {
        "Ford": Qarxana(name="Ford Factory", location="USA"),
        "Toyota": Qarxana(name="Toyota Factory", location="Japan"),
        "Nissan": Qarxana(name="Nissan Factory", location="Japan"),
        "Chevrolet": Qarxana(name="Chevrolet Factory", location="USA"),
        "Honda": Qarxana(name="Honda Factory", location="Japan")
    }

    for order in orders:
        parts = order.strip().split(', ')

        if len(parts) != 8:
            print(f"Ucnobi formati: {order}")
            continue

        customer_name, customer_id, model_info, color, car_type, engine_type, engine_volume, engine_hp = parts

        try:
            customer_id = int(customer_id)
            engine_volume = float(engine_volume)
            engine_hp = float(engine_hp)
        except ValueError:
            print(f"Invalid number format in order: {order}")
            continue

        engine = Engine(engine_type=engine_type, volume=engine_volume, h_p=engine_hp)

        brand = model_info.split()[0]

        qarxana = factories.get(brand, None)
        if not qarxana:
            print(f"Ucnobi brendi: {brand}")
            continue

        client = Client(customer_name, customer_id)

        
        if "Ford" in model_info:
            car = Ford(qarxana, model_info, color, 2024, engine, client, car_type)
        elif "Honda" in model_info:
            car = Honda(qarxana, model_info, color, 2024, engine, client, car_type)
        elif "Toyota" in model_info:
            car = Toyota(qarxana, model_info, color, 2024, engine, client, car_type)
        elif "Chevrolet" in model_info:
            car = Chevrolet(qarxana, model_info, color, 2024, engine, client, car_type)
        elif "Nissan" in model_info:
            car = Nissan(qarxana, model_info, color, 2024, engine, client, car_type)
        else:
            print(f"Ucnobi brendi: {model_info}")
            continue

        created_cars.append(car)

    return created_cars

def print_purchase_info(car):
    factory_info = car.qarxana.display_info()  
    print(f"VIN: {car.vin}, Clienti: {car.client.customer_name} ID: {car.client.customer_id}, "
          f"Modeli: {car.model}, Year: {car.year} Peri: {car.color}, Fabrika: {factory_info}, "
          f"Tipi: {car.car_type}, {car.engine.engine_type} - {car.engine.volume}L, {car.engine.h_p}HP")

def check_car_exists(customer_id):
    for car in created_cars:
        if car.client.customer_id == customer_id:  
            return car.display_info()  
    return None  

if __name__ == "__main__":
    try:
        orders = read_orders_from_file('sia.txt')
        create_cars_from_orders(orders)

        for car in created_cars:
            print_purchase_info(car)
            a1 = car

        id_to_check = input("Clientis ID: ").strip()  # Нормализация ввода

        if not id_to_check:
            print("ID daweret.")
        else:
            try:
                result = check_car_exists(int(id_to_check))  # Передаем ID как целое число
                if result:
                    print(f"Manqana momxvareblistvis ID {id_to_check} mzat aris: {result}")
                else:
                    print(f"Manqana momxvareblistvi ID {id_to_check} ar aris.")
            except ValueError:
                print("!!!!: ID unda iyos ricxvi.")
    except FileNotFoundError:
        print("'sia.txt' araris.")
    except Exception as e:
        print(f"Error: {e}")
