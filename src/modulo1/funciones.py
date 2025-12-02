def esBinario(strbinario):
    
    """Verifica si una cadena representa un número binario válido.
        Solo acepta caracteres '0' y '1'."""
    if not isinstance(strbinario, str):
        return False
        
    if len(strbinario) == 0:
        return False
        
    for char in strbinario:
        if char not in ('0', '1'):
            return False
            
    return True

def estaEnRango(valor, minimo, maximo):
   
    """Determina si un valor se encuentra dentro de un rango [minimo, maximo]."""
    try:
        return minimo <= valor <= maximo
    except TypeError:
        return False

def estaEnLista(valor, lista):
   
    """Verifica si un valor existe dentro de una lista dada. """
    if not isinstance(lista, list):
        return False
        
    return valor in lista