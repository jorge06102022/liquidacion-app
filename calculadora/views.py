from django.shortcuts import render
from datetime import datetime
from .models import Calculo
from .utils import calcular_liquidacion



def formato_moneda(valor):
    return "${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def parse_fecha(fecha_str):
    """
    Acepta:
    - 2024-01-01
    - 01/01/2024
    """
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

            # 🔥 VALIDAR SALARIO
            if not salario_str:
                raise ValueError("Salario vacío")

            salario = float(salario_str)

            # 🔥 PARSEAR FECHAS
            ingreso = parse_fecha(ingreso_str)
            retiro = parse_fecha(retiro_str)

            if not ingreso or not retiro:
                error = "Formato de fecha inválido"
            else:
                dias = (retiro - ingreso).days
                print("DIAS:", dias)  # 🔍 debug

                # 🔥 VALIDACIONES PRO
                if dias <= 0:
                    error = "La fecha de retiro debe ser mayor que la de ingreso"

                elif dias > 3660:  # máximo 10 años
                    error = "El rango es demasiado grande (revisa las fechas)"

                else:
                    datos = calcular_liquidacion(salario, ingreso, retiro)

                    calculo = Calculo.objects.create(
                        salario=salario,
                        fecha_ingreso=ingreso,
                        fecha_retiro=retiro,
                        **datos
                    )

                    resultado = {
                        "cesantias": formato_moneda(calculo.cesantias),
                        "intereses": formato_moneda(calculo.intereses),
                        "prima": formato_moneda(calculo.prima),
                        "vacaciones": formato_moneda(calculo.vacaciones),
                        "total": formato_moneda(calculo.total),
}
        except Exception as e:
            print("ERROR:", e)
            error = "Error en los datos ingresados"

    return render(request, "calculadora/index.html", {
        "resultado": resultado,
        "error": error
    })