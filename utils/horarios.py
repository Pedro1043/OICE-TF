def hora_a_minutos(hora_str: str) -> int:
    """
    Convierte una hora en formato HH:MM a minutos desde medianoche.
    
    Args:
        hora_str: Hora en formato "HH:MM"
    
    Returns:
        int: Minutos desde medianoche
    """
    hora, minutos = map(int, hora_str.split(':'))
    return hora * 60 + minutos


def horario_incluye_jueves_prohibido(horario_str: str) -> bool:
    """
    Verifica si un horario incluye el rango prohibido de jueves 10:00-14:00.
    
    Args:
        horario_str: String del horario en formato "Días HH:MM - HH:MM"
    
    Returns:
        bool: True si incluye el rango prohibido, False en caso contrario
    """
    if 'J' not in horario_str:
        return False
    
    # Extraer información del horario
    partes = horario_str.split(' ')
    if len(partes) < 3:
        return False
    
    hora_inicio = partes[1]
    hora_fin = partes[3]
    
    inicio_min = hora_a_minutos(hora_inicio)
    fin_min = hora_a_minutos(hora_fin)
    
    # Rango prohibido: 10:00-14:00 (600-840 minutos)
    rango_prohibido_inicio = 10 * 60  # 600 minutos
    rango_prohibido_fin = 14 * 60     # 840 minutos
    
    # Verificar si hay solapamiento
    return not (fin_min <= rango_prohibido_inicio or inicio_min >= rango_prohibido_fin)


def validar_horarios_disponibles(horarios_dict: dict) -> dict:
    """
    Valida todos los horarios contra restricciones y retorna información.
    
    Args:
        horarios_dict: Diccionario de horarios {id: descripción}
    
    Returns:
        dict: Información de validación para cada horario
    """
    resultados = {}
    for horario_id, horario_str in horarios_dict.items():
        prohibido = horario_incluye_jueves_prohibido(horario_str)
        resultados[horario_id] = {
            'horario': horario_str,
            'jueves_prohibido': prohibido,
            'disponible': not prohibido
        }
    return resultados