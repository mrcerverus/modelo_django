from app.models import Vehiculo, Chofer, RegistroContabilidad


def crear_vehiculo(patente, marca, modelo, year):
    auto = Vehiculo(patente=patente, marca=marca,modelo=modelo, year=year)
    auto.save()

def crear_chofer(rut, nombre, apellido, activo, vehiculo_id):
    if not rut.isdigit():
        print("por favor validar los datos del conductor")
        return
    chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo, vehiculo_id=vehiculo_id)
    chofer.save()

def crear_registro_contable(fecha_compra, valor, vehiculo_id):
    contable = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo_id=vehiculo_id)
    contable.save()

def deshabilitar_chofer(rut):
    Chofer.objects.filter(rut=rut).update(activo=False)

def deshabilitar_vehiculo(patente):
    Vehiculo.objects.filter(patente=patente).update(activo=False)

def habilitar_chofer(rut):
    Chofer.objects.filter(rut=rut).update(activo=True)

def habilitar_vehiculo(patente):
    Vehiculo.objects.filter(patente=patente).update(activo=True)

def obtener_vehiculo(patente):
    auto = Vehiculo.objects.get(patente=patente)
    return auto

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer

def asignar_chofer_a_vehiculo(rut, patente):
    mode = Chofer.objects.filter(rut=rut).update(vehiculo_id=patente)
    print(f'{mode.rut}, {mode.nombre} {mode.apellido}, le corresponde vehiculo: {mode.vehiculo_id}')

def imprimir_datos_vehiculos():
    autos = Vehiculo.objects.all()
    for a in autos:
        print(f"[{a.patente}]: {a.marca} - {a.modelo} - {a.year}, estado: {a.activo}")
        if hasattr(a, "Chofer"):
            p = a.Chofer
            print(f"Nombre: {a.nombre} {a.apellido}, Rut: {a.rut} , Activo:{a.activo}")
        if hasattr(a, "RegistroContabilidad"):
            c = a.RegistroContabilidad
            print(f"Fecha Compra: {c.fecha_compra}, Valor: {c.valor}")