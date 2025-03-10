# Sistema de Diagnóstico de Cólera

Este proyecto es un sistema de diagnóstico basado en reglas para detectar y gestionar posibles casos de cólera en pacientes, utilizando la inferencia lógica. El sistema utiliza un motor de inferencia basado en el enfoque de **experta** y sigue un conjunto de reglas definidas para diagnosticar la condición de un paciente, y dar recomendaciones según los síntomas presentados.

## Descripción

El sistema implementa un conjunto de reglas de diagnóstico para cólera y sus complicaciones asociadas, como la deshidratación severa, el shock hipovolémico y otros síntomas relacionados. El motor de inferencia procesa los datos del paciente (como diarrea acuosa, vómitos frecuentes, calambres musculares, entre otros) y, según los valores de estos datos, genera diagnósticos y recomendaciones.

## Características

- Diagnóstico de cólera basado en síntomas comunes.
- Identificación de casos de deshidratación severa.
- Recomendaciones de tratamiento según el diagnóstico.
- Identificación de riesgo en grupos vulnerables como niños y adultos mayores.
- Registro de los diagnósticos y recomendaciones en un archivo de texto.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado Python 3.x y las siguientes dependencias:

- **experta**: una biblioteca para motores de inferencia en Python.
- **frozendict**: se utiliza en la biblioteca **experta**.

Puedes instalar estas dependencias ejecutando:

```bash
pip install experta frozendict
