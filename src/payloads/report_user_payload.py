
def crear_payload_report_user(usuario, razon):
    return {
        "user": usuario,
        "reason": razon,      
    }

def crear_payload_report_user_sin_reason(usuario):
    return {
        "user": usuario,
    }