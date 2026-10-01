class Producto:
    def __init__(self, codigo: int, nombre: str, stock: int, precio_compra: float, precio_venta: float):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta

    def calcular_beneficio(self, unidades_vendidas: int) -> float:
        """Calcula el beneficio obtenido por la venta de unidades."""
        return (self.precio_venta - self.precio_compra) * unidades_vendidas

    def vender(self, unidades: int):
        """Reduce el stock por la cantidad vendida."""
        if unidades > self.stock:
            raise FueraDeStockError(f"Solo hay {self.stock} unidades disponibles.")
        self.stock -= unidades
class FueraDeStockError(Exception):
    pass


def cargar_productos(ruta: str) -> dict[int, Producto]:
    """Carga los productos desde un archivo y devuelve un diccionario con el código como clave."""
    productos = {}
    errores = 0

    try:
        with open(ruta, encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    partes = linea.strip().split(";")
                    if len(partes) != 5:
                        raise ValueError("Formato incorrecto en línea.")
                    codigo = int(partes[0])
                    nombre = partes[1]
                    stock = int(partes[2])
                    precio_compra = float(partes[3])
                    precio_venta = float(partes[4])
                    productos[codigo] = Producto(codigo, nombre, stock, precio_compra, precio_venta)
                except (ValueError, IndexError) as e:
                    errores += 1
        print(f"Errores encontrados: {errores}")
    except FileNotFoundError:
        print("Error: No se encontró el archivo de productos.")
        exit(1)

    return productos



def guardar_pedido(ruta: str, codigo: int, unidades: int):
    """Agrega un pedido al archivo pedidos.txt."""
    with open(ruta, "a", encoding="utf-8") as archivo:
        archivo.write(f"{codigo}:{unidades}\n")

def desea_comprar_otra(respuesta: str) -> bool:
    """Valida si el usuario desea continuar comprando."""
    n_count = respuesta.lower().count("n")
    return n_count < len(respuesta) - n_count


def main():
    productos = cargar_productos("data/productos.txt")
    pedidos_ruta = "data/pedidos.txt"
    beneficio_total = 0.0

    while True:
        try:
            codigo = input("Introduce el código del producto (o 'x' para salir): ").strip()
            if codigo.lower() == 'x':
                break

            codigo = int(codigo)
            if codigo not in productos:
                print("El código no existe. Inténtalo de nuevo.")
                continue

            producto = productos[codigo]
            try:
                unidades = int(input(f"¿Cuántas unidades de {producto.nombre} quieres comprar?: ").strip())
                producto.vender(unidades)
                beneficio_total += producto.calcular_beneficio(unidades)
                print(f"Compra realizada. Quedan {producto.stock} unidades en stock.")
            except FueraDeStockError as e:
                print(e)
                unidades_comprables = producto.stock
                producto.vender(unidades_comprables)
                unidades_a_pedir = unidades - unidades_comprables
                guardar_pedido(pedidos_ruta, codigo, unidades_a_pedir)
                print(f"Se vendieron {unidades_comprables} unidades y se realizó un pedido de {unidades_a_pedir}.")

        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Continuando...")

        respuesta = input("¿Desea comprar otro producto? (NO para salir): ").strip()
        if not desea_comprar_otra(respuesta):
            break

    print("\nGracias por comprar en PC iMAT...")
    print(f"****Info solo para la tienda****\n Beneficio total: {beneficio_total:.2f}€")
