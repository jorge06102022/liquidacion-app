from django.shortcuts import render
from datetime import datetime
from .utils import calcular_liquidacion



def formato_moneda(valor):
    return "${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


def parse_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d")
    except:
        try:
            return datetime.strptime(fecha_str, "%d/%m/%Y")
        except:
            return None


def index(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            salario_str = request.POST.get("salario")
            ingreso_str = request.POST.get("ingreso")
            retiro_str = request.POST.get("retiro")

            if not salario_str:
                raise ValueError("Salario vacío")

            salario = float(salario_str)

            ingreso = parse_fecha(ingreso_str)
            retiro = parse_fecha(retiro_str)

            if ingreso is None or retiro is None:
                error = "Formato de fecha inválido"
            else:
                dias = (retiro - ingreso).days

                if dias <= 0:
                    error = "La fecha de retiro debe ser mayor que la de ingreso"

                elif dias > 3660:
                    error = "El rango es demasiado grande"

                else:
                    datos = calcular_liquidacion(salario, ingreso, retiro)

                    resultado = {
                        "cesantias": formato_moneda(datos["cesantias"]),
                        "intereses": formato_moneda(datos["intereses"]),
                        "prima": formato_moneda(datos["prima"]),
                        "vacaciones": formato_moneda(datos["vacaciones"]),
                        "total": formato_moneda(datos["total"]),
                    }

        except Exception as e:
            print("ERROR:", e)
            error = "Error en los datos ingresados"

    return render(request, "calculadora/index.html", {
        "resultado": resultado,
        "error": error
    })


# 🔥 ESTO DÉJALO FUERA (CORRECTO)
def privacidad(request):
    return render(request, 'calculadora/privacidad.html')

def terminos(request):
    return render(request, 'calculadora/terminos.html')

def contacto(request):
    return render(request, 'calculadora/contacto.html')

def calcular_prima(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            salario = float(request.POST.get("salario"))
            ingreso = request.POST.get("ingreso")
            retiro = request.POST.get("retiro")

            from datetime import datetime
            ingreso = datetime.strptime(ingreso, "%Y-%m-%d")
            retiro = datetime.strptime(retiro, "%Y-%m-%d")

            dias = (retiro - ingreso).days

            if dias <= 0:
                error = "Fechas inválidas"
            else:
                prima = (salario * dias) / 360

                def formato(valor):
                    return "${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

                resultado = formato(prima)

        except:
            error = "Error en los datos"

    return render(request, "calculadora/prima.html", {
        "resultado": resultado,
        "error": error
    })
def home(request):
    return render(request, "calculadora/home.html")

def calcular_cesantias(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            salario = float(request.POST.get("salario"))
            ingreso = request.POST.get("ingreso")
            retiro = request.POST.get("retiro")

            from datetime import datetime
            ingreso = datetime.strptime(ingreso, "%Y-%m-%d")
            retiro = datetime.strptime(retiro, "%Y-%m-%d")

            dias = (retiro - ingreso).days

            if dias <= 0:
                error = "Fechas inválidas"
            else:
                cesantias = (salario * dias) / 360

                def formato(valor):
                    return "${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

                resultado = formato(cesantias)

        except:
            error = "Error en los datos"

    return render(request, "calculadora/cesantias.html", {
        "resultado": resultado,
        "error": error
    })


def calcular_vacaciones(request):
    resultado = None
    error = None

    if request.method == "POST":
        try:
            salario = float(request.POST.get("salario"))
            ingreso = request.POST.get("ingreso")
            retiro = request.POST.get("retiro")

            from datetime import datetime
            ingreso = datetime.strptime(ingreso, "%Y-%m-%d")
            retiro = datetime.strptime(retiro, "%Y-%m-%d")

            dias = (retiro - ingreso).days

            if dias <= 0:
                error = "Fechas inválidas"
            else:
                vacaciones = (salario * dias) / 720

                def formato(valor):
                    return "${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

                resultado = formato(vacaciones)

        except:
            error = "Error en los datos"

    return render(request, "calculadora/vacaciones.html", {
        "resultado": resultado,
        "error": error
    })