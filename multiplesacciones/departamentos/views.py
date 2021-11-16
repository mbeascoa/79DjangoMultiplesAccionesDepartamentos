from django.shortcuts import render


def index(request):
    return render(request, "departamentos/Inicio.html")




def crud(request):
    dato = request.POST['operacion']
    numero = request.POST['numero']
    nombre = request.POST['nombre']
    localidad = request.POST['localidad']


    if dato == 'insertar':
        print(f"proceso para insertar departamento , {numero}  {nombre}  {localidad}")
        resultado= f"  insertado un departamento con el número: {numero}, nombre:  {nombre}, localidad:  {localidad} ,"
        operacion = '" insertado"'
    elif dato =="modificar":
        print(f"proceso para modificar departamento , {numero}  {nombre}  {localidad}")
        resultado = f"   modificado un departamento con el número: {numero}, nombre:  {nombre}, localidad:  {localidad}, "
        operacion = '"modificar"'
    else:
        print(f"proceso para eliminar departamento , {numero}  {nombre}  {localidad}")
        resultado = f"  eliminado un departamento con el número: {numero}, nombre:  {nombre}, localidad:  {localidad}, "
        operacion = '" eliminar"'


    lista = {
        "operacion": operacion,
        "resultado": resultado

    }

    return render(request, "departamentos/Inicio.html", lista)


