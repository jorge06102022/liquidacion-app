def calcular_liquidacion(salario, ingreso, retiro):
    dias = (retiro - ingreso).days

    cesantias = (salario * dias) / 360
    intereses = cesantias * 0.12 * (dias / 360)
    prima = (salario * dias) / 360
    vacaciones = (salario * dias) / 720

    total = cesantias + intereses + prima + vacaciones

    return {
        "cesantias": round(cesantias, 2),
        "intereses": round(intereses, 2),
        "prima": round(prima, 2),
        "vacaciones": round(vacaciones, 2),
        "total": round(total, 2),
    }