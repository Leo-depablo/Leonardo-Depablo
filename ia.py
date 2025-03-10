from experta import *

class ColeraDiagnostico(KnowledgeEngine):

    @Rule(Fact(diarrea_acuosa=True))
    def sospecha_colera(self):
        self.declare(Fact(sospecha_colera=True))
        print("Diagnóstico: Sospecha de cólera.")

    @Rule(Fact(sospecha_colera=True), Fact(vomitos_frecuentes=True))
    def alto_riesgo_deshidratacion(self):
        self.declare(Fact(alto_riesgo_deshidratacion=True))
        print("Diagnóstico: Alto riesgo de deshidratación.")

    @Rule(Fact(alto_riesgo_deshidratacion=True), Fact(ojos_hundidos=True), Fact(piel_seca=True))
    def deshidratacion_severa(self):
        self.declare(Fact(deshidratacion_severa=True))
        print("Diagnóstico: Deshidratación severa. Requiere atención médica urgente.")

    @Rule(Fact(deshidratacion_severa=True), Fact(pulso_rapido=True))
    def urgencia_medica(self):
        print("Diagnóstico: URGENCIA MÉDICA. Traslado inmediato al hospital.")

    @Rule(Fact(sospecha_colera=True), Fact(agua_contaminada=True))
    def alta_probabilidad(self):
        self.declare(Fact(alta_probabilidad=True))
        print("Diagnóstico: Alta probabilidad de cólera. Se recomienda prueba de laboratorio.")

    @Rule(Fact(alta_probabilidad=True), Fact(brote_activo=True))
    def confirmacion_requerida(self):
        print("Diagnóstico: Confirmación requerida mediante pruebas.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(deshidratacion_severa=True))
    def hospitalizacion_inmediata(self):
        print("Recomendación: Hospitalización inmediata con rehidratación intravenosa.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(deshidratacion_leve=True))
    def tratamiento_oral(self):
        print("Recomendación: Administración de sales de rehidratación oral y monitoreo.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(fiebre=True))
    def posible_infeccion_secundaria(self):
        print("Diagnóstico: Posible infección secundaria. Evaluar uso de antibióticos.")

    @Rule(Fact(diarrea_acuosa=True), Fact(calambres_musculares=True))
    def desequilibrio_electrolitico(self):
        print("Diagnóstico: Posible desequilibrio electrolítico. Se recomienda suero oral.")

    @Rule(Fact(diarrea_acuosa=True), Fact(niño_menor=True))
    def riesgo_infante(self):
        print("Diagnóstico: Alto riesgo en infantes. Referir a centro de salud.")

    @Rule(Fact(diarrea_acuosa=True), Fact(adulto_mayor=True))
    def riesgo_adulto_mayor(self):
        print("Diagnóstico: Alto riesgo en adultos mayores. Monitoreo constante.")

    @Rule(Fact(diarrea_acuosa=True), Fact(labios_secos=True), Fact(orina_oscura=True))
    def signos_deshidratacion(self):
        print("Diagnóstico: Signos de deshidratación. Aumentar hidratación.")

    @Rule(Fact(viaje_reciente=True))
    def mayor_probabilidad(self):
        print("Diagnóstico: Mayor probabilidad de infección. Realizar pruebas.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(hipotension_severa=True))
    def shock_hipovolemico(self):
        print("Diagnóstico: Riesgo de shock hipovolémico. Hospitalización urgente.")

    @Rule(Fact(contacto_con_paciente=True))
    def posible_contagio(self):
        print("Diagnóstico: Posible contagio. Realizar seguimiento.")

    @Rule(Fact(no_acceso_agua_potable=True))
    def riesgo_sanitario(self):
        print("Diagnóstico: Aumentar precaución. Promover purificación de agua.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(brote_activo=True))
    def alerta_sanitaria(self):
        print("Diagnóstico: Notificar a autoridades sanitarias.")

    @Rule(Fact(diagnostico_confirmado=True), Fact(mejoria_tras_tratamiento=True))
    def prevencion_recaidas(self):
        print("Diagnóstico: Seguir recomendaciones para evitar recaídas.")

    @Rule(Fact(sospecha_colera=False))
    def considerar_otras(self):
        print("Diagnóstico: No se cumplen criterios de cólera. Considerar otras enfermedades.")

# Crear motor de inferencia
motor = ColeraDiagnostico()

# Casos de prueba
casos_prueba = [
    {"diarrea_acuosa": True, "vomitos_frecuentes": True, "ojos_hundidos": True, "piel_seca": True, "pulso_rapido": True},  # Caso de urgencia médica
    {"diarrea_acuosa": True, "agua_contaminada": True, "brote_activo": True},  # Confirmación de cólera
    {"diarrea_acuosa": True, "calambres_musculares": True},  # Desequilibrio electrolítico
    {"diarrea_acuosa": True, "labios_secos": True, "orina_oscura": True},  # Signos de deshidratación
    {"diagnostico_confirmado": True, "mejoria_tras_tratamiento": True},  # Prevención de recaídas
]

# Guardar los resultados de las pruebas en un archivo txt
resultados_path = "/mnt/data/resultados_pruebas_colera.txt"

with open(resultados_path, "w") as archivo:
    for i, caso in enumerate(casos_prueba):
        archivo.write(f"--- Ejecutando Caso de Prueba {i+1} ---\n")
        motor.reset()
        for clave, valor in caso.items():
            motor.declare(Fact(**{clave: valor}))
        motor.run()
        archivo.write("\n")  # Separar los resultados de cada prueba

