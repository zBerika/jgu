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

class Engine:
    def __init__(self, engine_type, volume, h_p):
        self.engine_type = engine_type
        self.volume = volume
        self.h_p = h_p

    def display_info(self):
        return f"{self.engine_type}-{self.volume}L, {self.h_p} h.p."

class Car(Qarxana):
    def __init__(self, qarxana, model, color, year, engine: Engine, customer_info, car_type):
        self.qarxana = qarxana
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        self.customer_info = customer_info
        self.car_type = car_type
        self.vin = None

    def display_info(self):
        return f"{self.year} {self.model} {self.color}, Qarxana: {self.qarxana.display_info()}, Engine: {self.engine.display_info()}"

class Ford(Car, VINGenerator):
    def __init__(self, qarxana, model, color, year, engine: Engine, customer_info, car_type):
        super().__init__(qarxana, model, color, year, engine, customer_info, car_type)
        self.vin = self.generate_vin()
class Toyota(Ford):
    pass

class Nissan(Ford):
    pass

class Chevrolet(Ford):
    pass

class Honda(Ford):
    pass

def create_cars_from_orders(orders):
    cars = []

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


        engine_volume = float(engine_volume)
        engine_hp = float(engine_hp)

        engine = Engine(engine_type=engine_type, volume=engine_volume, h_p=engine_hp)

        brand = model_info.split()[0]

        qarxana = factories.get(brand, None)
        if not qarxana:
            print(f"Ucnobi brendi: {brand}")
            continue

        if "Ford" in model_info:
            car = Ford(qarxana, model_info, color, 2024, engine, f"{customer_name}, {customer_id}",  car_type)
        elif "Honda" in model_info:
            car = Honda(qarxana, model_info, color, 2024, engine, f"{customer_name}, {customer_id}", car_type)
        elif "Toyota" in model_info:
            car = Toyota(qarxana, model_info, color, 2024, engine, f"{customer_name}, {customer_id}", car_type)
        elif "Chevrolet" in model_info:
            car = Chevrolet(qarxana, model_info, color, 2024, engine, f"{customer_name}, {customer_id}", car_type)
        elif "Nissan" in model_info:
            car = Nissan(qarxana, model_info, color, 2024, engine, f"{customer_name}, {customer_id}", car_type)
        else:
            print(f"Ucnobi brendi: {model_info}")
            continue

        cars.append(car)

    return cars


def print_purchase_info(car):
    customer_name, customer_id = car.customer_info.split(', ')
    factory_info = car.qarxana.display_info()  # Получаем информацию о заводе
    print(f"VIN: {car.vin}, Clienti: {customer_name} ID: {customer_id}, "
          f"Modeli: {car.model}, Year: {car.year} Peri: {car.color}, Fabrika: {factory_info}, "
          f"Tipi: {car.car_type}, {car.engine.engine_type} - {car.engine.volume}L, {car.engine.h_p}HP")

if __name__ == "__main__":
    #try:
        orders = read_orders_from_file('sia.txt')
        created_cars = create_cars_from_orders(orders)

        for car in created_cars:
            print_purchase_info(car)
    #except FileNotFoundError:
    #    print("'sia.txt'")
    #except Exception as e:
    #    print(f"KRASHHHHHHH: {e}")
