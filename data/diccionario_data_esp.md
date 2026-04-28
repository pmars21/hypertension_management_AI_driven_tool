# Resumen del Conjunto de Datos: Conjunto de Datos Combinado de NHANES (merged_all.csv)

## Información General
- **Nombre de la Encuesta:** Encuesta Nacional de Examen de Salud y Nutrición (NHANES)
- **Ciclo de Datos:** Agosto 2021 - Agosto 2023 (principalmente)
- **Componente:** Conjunto de datos combinado de múltiples componentes
- **Archivo de Datos:** `merged_all.csv`
- **Población Objetivo:** Varía según el componente (generalmente participantes de 1 a 80+ años, con restricciones de edad específicas para componentes como presión arterial, equilibrio y elastografía).

## Alcance y Metodología
Este conjunto de datos es un archivo consolidado que combina múltiples componentes de NHANES en un solo archivo plano. Se basa en el número de secuencia del encuestado (`ID` / `SEQN`) para vincular los datos demográficos, de examen, de laboratorio y de cuestionario para cada participante.

**Componentes incluidos según las variables:**
- Demografía (`DEMO_L`)
- Medidas Corporales (`BMX_L`)
- Presión Arterial (`BPXO_L`)
- Equilibrio (`BAX_L`)
- Elastografía Transitoria por Ultrasonido Hepático (`LUX_L`)
- Suplementos Dietéticos (`DSQTOT_L`)
- Datos de Laboratorio (Hemograma Completo, Lípidos, Metales Pesados, Albúmina/Creatinina en Orina)

**Notas Analíticas:**
- **Pesos:** Debido a que este conjunto de datos fusiona múltiples componentes (Demografía, Exámenes MEC, Dieta y Submuestras de Laboratorio), los analistas deben elegir cuidadosamente la variable de peso adecuada (por ejemplo, `Peso Entrevista`, `Peso Examen`, `Peso Dieta`, `Peso Sangre`, `Peso Ayuno`) dependiendo de las variables específicas y las subpoblaciones que se analicen.
- **Datos Faltantes:** Muchas columnas contienen valores faltantes (`NaN`) como resultado de exclusiones intencionales (por ejemplo, mujeres embarazadas para elastografía) o restricciones de protocolo basadas en la edad.

## Resumen de Variables Clave

### 1. Identificadores y Demografía (DEMO_L)
**Población Objetivo:** Todos los participantes en la muestra de NHANES de agosto de 2021 a agosto de 2023.
**Publicado por primera vez:** Septiembre 2024
**Valores Faltantes:** Los valores faltantes están codificados como *.*

**Contexto de la Encuesta y Notas Analíticas (Impacto de COVID-19):**
- **Reanudación de Operaciones:** La recolección de datos se reanudó en agosto de 2021 después de haber sido suspendida en marzo de 2020.
- **Cambios en el Diseño de la Muestra:** No hubo sobremuestreo a nivel de persona por origen hispano/raza o ingresos (a diferencia de ciclos anteriores), pero se añadió un sobremuestreo por grupo de edad. Esto puede resultar en una menor precisión estadística para ciertos subgrupos demográficos.
- **Precaución por Brecha de Datos:** Existe una brecha de datos de 15 meses entre el ciclo anterior y este. Los analistas deben tener estricta precaución al combinar estos datos con ciclos anteriores o al realizar análisis de tendencias.
- **Protecciones de Confidencialidad:** Debido a los riesgos de divulgación, algunas variables (como el estado civil, embarazo, edad 80+, tamaños de familia de más de 7) han sido limitadas superiormente o restringidas a ciertas bandas de edad. Otras solo son accesibles a través del Centro de Datos de Investigación del NCHS.

**Variables Clave:**
*   **Identificadores y Administración de la Encuesta:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado (identificador único).
    *   **`Ciclo`** (`SDDSRVYR`): Ciclo de liberación de datos (`12` indica el ciclo de agosto 2021 - agosto 2023).
    *   **`Estado`** (`RIDSTATR`): Estado de entrevista/examen (1 = Solo entrevistado; 2 = Entrevistado y examinado en MEC).
    *   **`Mes Examen`** (`RIDEXMON`): Periodo de seis meses en que se realizó el examen.
*   **Demografía:**
    *   **`Genero`** (`RIAGENDR`): Género (Masculino, Femenino).
    *   **`Edad`** (`RIDAGEYR`): Edad en años en la evaluación (límite superior en 80 años).
    *   **`RIDAGEMN` / `RIDEXAGM`**: Edad en meses (para niños pequeños/jóvenes).
    *   **`Etnia 1` / `Etnia 3`** (`RIDRETH1` / `RIDRETH3`): Raza/Origen hispano (Incluye categorías para México-americano, Otro hispano, Blanco no hispano, Negro no hispano, Asiático no hispano, y Otro/Multirracial).
    *   **`DMDEDUC2`**: Nivel de educación para adultos de 20+ años.
    *   **`DMDMARTZ`**: Estado civil.
    *   **`DMQMILIZ`**: Sirvió en servicio activo en las Fuerzas Armadas de EE.UU.
*   **Lugar de Nacimiento y Residencia:**
    *   **`Pais Nacimiento`** (`DMDBORN4`): País de nacimiento (Nacido en EE.UU. vs. Nacido en otros países).
    *   **`DMDYRUSR`**: Tiempo viviendo en los EE.UU. (categórico).
*   **Hogar e Ingresos:**
    *   **`Tamano Hogar`** (`DMDHHSIZ`): Número total de personas en el hogar (límite superior de 7 o más).
    *   **`Ratio Pobreza`** (`INDFMPIR`): Proporción de ingresos familiares respecto a las pautas de pobreza (límite superior de 5.00).
    *   **Variables `DMDHR***`**: Información sobre la Persona de Referencia del Hogar (por ejemplo, género `DMDHRGND`, edad `DMDHRAGZ`, educación `DMDHREDZ`, estado civil `DMDHRMAZ`).
*   **Estado Médico / Físico:**
    *   **`RIDEXPRG`**: Estado de embarazo al momento del examen (solo publicado para mujeres de 20-44 años).
*   **Pesos de la Muestra y Estimación de Varianza:**
    *   **`Peso Entrevista`** (`WTINT2YR`): Peso de entrevista de 2 años de la muestra completa.
    *   **`Peso Examen`** (`WTMEC2YR`): Peso del examen MEC de 2 años de la muestra completa.
    *   **`Estrato` / `PSU`** (`SDMVSTRA` / `SDMVPSU`): Pseudo-estrato y pseudo-PSU de varianza enmascarada (vitales para la estimación precisa de la varianza).

### 2. Suplementos Dietéticos (DSQTOT_L)
**Población Objetivo:** Todos los participantes de la encuesta
**Publicado por primera vez:** Febrero 2025

**Alcance y Contenido:**
Este componente captura el uso en 30 días de:
1. **Suplementos Dietéticos (DS):** Tanto recetados como no recetados (ej., vitaminas, minerales, hierbas).
2. **Antiácidos:** Específicamente, antiácidos no recetados que contienen **calcio y/o magnesio**.

Se generan dos archivos principales de este componente:
*   **Total de Suplementos Dietéticos (`DSQTOT_L`):** Resume la **ingesta diaria promedio total** de 34 nutrientes por participante a partir de *todos* sus suplementos y antiácidos reportados combinados. (Este es el archivo descrito aquí).
*   **Suplementos Dietéticos Individuales (`DSQIDS_L`):** Desglose detallado de cada producto específico reportado por el usuario.

**Aspectos Destacados del Protocolo e Impacto del COVID-19:**
- **Modo de Administración:** Para adaptarse a la pandemia de COVID-19, la recolección de datos pasó de presencial a **entrevistas telefónicas** (Entrevista Telefónica Asistida por Computadora - CATI). Esto se llevó a cabo tras el primer recordatorio dietético de 24 horas.
- **Reporte:** Se pidió a los participantes que leyeran las etiquetas de los envases de los suplementos al entrevistador por teléfono.
- **Preguntas Eliminadas:** Las preguntas sobre *cuánto tiempo* se había tomado un suplemento y la *razón* para tomarlo se descontinuaron en este ciclo de la encuesta.

**Procesamiento de Datos y Emparejamiento:**
- **Emparejamiento con la Base de Datos:** Los suplementos reportados fueron emparejados por nutricionistas del NCHS con etiquetas conocidas en la Base de Datos de Suplementos Dietéticos de NHANES (NHANES-DSD).
- **Confianza de Emparejamiento (`DSDMTCH`):** Dado que los participantes leyeron las etiquetas por teléfono, la precisión varió. Los productos se emparejaron como exactos, probables, genéricos, razonables o por defecto (según las concentraciones comunes del mercado). Los analistas deben saber que se asignan perfiles de nutrientes genéricos o por defecto cuando faltan datos exactos de la marca.
- **Exclusiones:** Se eliminaron de este conjunto de datos los alimentos, bebidas, remedios homeopáticos y la mayoría de los medicamentos recetados.

**Notas Analíticas y Pesos de la Muestra:**
- **Pesos de la Muestra (`Peso Dieta` / `WTDRD1`):** Debido a que esta encuesta específica se realizó simultáneamente con el recordatorio dietético del Día 1, los analistas **deben usar el peso de la muestra Dietética del Día Uno (`Peso Dieta`).** No utilice pesos MEC o de entrevista estándar.
- **Nutrientes Faltantes:** Si el participante reportó tomar un suplemento pero la cantidad/dosis específica era desconocida (o el envase no estaba disponible), las cantidades agregadas de nutrientes (ej., Vitamina C total) para ese participante se establecerán como faltantes, aunque se cuente como usuario del suplemento.
- **Ingesta Dietética Total:** Para calcular la ingesta *total* de nutrientes de una persona, los analistas deben combinar los nutrientes de los suplementos de este archivo con las ingestas de nutrientes de alimentos/bebidas de los archivos de recordatorio dietético de 24 horas.

**Variables Clave:**
*   **Identificadores de Encuesta y Peso:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado.
    *   **`Peso Dieta`** (`WTDRD1`): Peso de la muestra dietética del día uno.
*   **Uso General y Conteos:**
    *   **`Uso Suplementos`** (`DSD010`): ¿Tomó algún suplemento dietético? (1 = Sí, 2 = No)
    *   **`Uso Antiacidos`** (`DSD010AN`): ¿Tomó algún antiácido? (1 = Sí, 2 = No)
    *   **`Total Suplementos`** (`DSDCOUNT`): Número total de suplementos dietéticos tomados.
    *   **`Total Antiacidos`** (`DSDANCNT`): Número total de antiácidos tomados.
*   **Ingestas Diarias Agregadas de Nutrientes:**
    *Las variables que comienzan con `DSQT` representan la ingesta diaria media agregada total de todos los suplementos/antiácidos consumidos por el individuo.*
    *   **Macronutrientes:** Energía (`DSQTKCAL`), Proteína (`DSQTPROT`), Carbohidratos (`DSQTCARB`), Azúcar (`DSQTSUGR`), Fibra (`DSQTFIBE`), Grasas (`DSQTTFAT`, `DSQTSFAT`, etc.).
    *   **Vitaminas:** Vitamina C (`DSQTVC`), Vitamina D (`DSQTVD`), Vitamina B12 (`DSQTVB12`), Ácido Fólico (`DSQTFA`), etc.
    *   **Minerales/Otros:** Calcio (`DSQTCALC`), Hierro (`DSQTIRON`), Magnesio (`DSQTMAGN`), Zinc (`DSQTZINC`), Cafeína (`DSQTCAFF`), Luteína/Zeaxantina (`DSQTLZ`), etc.
    *   *(Consulte el Apéndice 2 de la documentación para la lista completa de los 34 nutrientes calculados).*

### 3. Equilibrio (BAX_L)
**Población Objetivo:** Participantes de 20 a 69 años.
**Publicado por primera vez:** Octubre 2024

**Elegibilidad y Exclusiones:**
Se **excluyó** a los participantes de la prueba si cumplían con ciertos criterios:
- Embarazada o con un peso superior a 315 libras (límite de peso para la superficie de espuma).
- Discapacidad visual severa, incapacidad para pararse de forma independiente, amputaciones de piernas/pies o prótesis en la parte inferior del cuerpo.
- Lesiones/cirugías recientes en piernas/tobillos/pies, o mareos actuales con un historial de caídas debido a mareos.
- Usar tacones de 3 pulgadas o más.
- Incapacidad para ajustar correctamente el cinturón de seguridad.

**Exclusiones Específicas de la Condición 5:** Los participantes fueron excluidos adicionalmente de la Condición 5 si tenían dolor de cuello actual, cirugía previa de cuello, problemas crónicos de cuello o movilidad limitada del cuello.

**Aspectos Destacados del Protocolo (Prueba de Romberg Modificada - MRT):**
El MRT evalúa el equilibrio con cinco condiciones de dificultad creciente. Un participante no pasaba una condición si no podía mantener el equilibrio durante el tiempo requerido en dos ensayos.
- **Superficie de Apoyo y Entrada Visual:**
  - **Condición 1:** Suelo descubierto, ojos abiertos
  - **Condición 2:** Suelo descubierto, ojos cerrados
  - **Condición 3:** Espuma densa, ojos abiertos
  - **Condición 4:** Espuma densa, ojos cerrados
  - **Condición 5:** Espuma densa, ojos cerrados, moviendo la cabeza de lado a lado
- **Criterios de aprobación:**
  - **Condiciones 1 y 2:** 15 segundos.
  - **Condiciones 3, 4 y 5:** 20 segundos (la duración real evaluada es de 30 segundos, pero la investigación establece 20 segundos como un umbral de "aprobación").
- **Condiciones de fallo:** Mover los pies, descruzar los brazos del pecho, abrir los ojos (en condiciones con ojos cerrados), tocar la pared o requerir la intervención de un técnico.

**Notas Analíticas (Diferencias con el Ciclo 1999-2004):**
Si compara estos datos con el ciclo de 1999-2004, tenga en cuenta las principales diferencias:
- **Tiempos de Aprobación:** En 1999-2004, los participantes necesitaban 30 segundos para pasar las Condiciones 3 y 4, mientras que este ciclo considera 20 segundos como aprobación. Es posible que necesite recodificar duraciones de 20-29 segundos como "no pasó" para comparaciones directas.
- **Condición 5:** No se evaluó en 1999-2004.
- **Revisión de Variables:** Los nombres de las variables han cambiado (ej., `BAXPFC11` ahora es `BAXPF11`, y `BAXFTC11` ahora es `BAXTC11`). Además, este ciclo informa el *tiempo de duración intentado* en lugar del *tiempo de fallo*.
- **Pesos:** Use los pesos de la muestra de Examen estándar para todos los análisis.

**Variables Clave:**
*   **Identificadores de Encuesta y Estado:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado.
    *   **`Estado Equilibrio`** (`BAXMSTAT`): Estado del examen MRT (1 = Completo, 2 = Parcial, 3 = No realizado, 4 = Inelegible).
    *   **`Estado Romberg`** (`BAX5STAT`): Elegibilidad específicamente para la Condición 5.
    *   **`BAXRXNC` / `BAXRXND`**: Declaraciones de motivos para exámenes Parciales (`BAXRXNC`) o No Realizados (`BAXRXND`).
*   **Preguntas de Evaluación Previa a la Prueba:**
    *   **`Mareos` (`BAQ130`), `Desmayos` (`BAQ121`), `Convulsiones` (`BAQ125`), `Dificultad Caminar` (`BAQ132`), `Caidas` (`BAQ140`), `Fracturas` (`BAQ150`), `Test Densidad` (`BAQ160`), `Med. Osteoporosis` (`BAQ170`), `Diag. Osteoporosis` (`BAQ173`)**: Preguntas de evaluación que abordan la capacidad de pararse, uso de aparatos ortopédicos para las piernas, lesiones, mareos/caídas en el pasado, dolor de cuello, historial de cirugía de cuello y el consentimiento explícito para comenzar la prueba.
*   **Resultados de los Ensayos (Repetido para las Condiciones 1-5, Ensayos 1 y 2):** Convención de nomenclatura de variables: **[Prefijo][Condición #][Ensayo #]**
    *   **`Romberg X Res`** (`BAXPF__`, ej., `BAXPF11`): Aprobó/No aprobó la condición y ensayo específicos.
    *   **`Romberg X Seg`** (`BAXTC__`, ej., `BAXTC11`): Tiempo/duración mantenida durante el ensayo.
    *   **`BAARFC__`** (ej., `BAARFC11`): Motivo por el que se detuvo el ensayo (1 = Movió los pies, 2 = Movió los brazos de la cintura, 3 = Abrió los ojos, 4 = Intervención técnica, 5 = Agarró/tocó la pared).

### 4. Presión Arterial - Oscilométrica (BPXO_L)
**Población Objetivo:** Participantes de 8 años en adelante.
**Publicado por primera vez:** Septiembre 2024

**Elegibilidad y Exclusiones:**
Se **excluyó** a los participantes de la medición de la presión arterial si presentaban condiciones específicas en **ambos brazos** (o condiciones específicas en el brazo afectado):
- Erupciones, vendajes de gasa, yesos, edema, parálisis, tubos, llagas o heridas abiertas, brazos atrofiados o derivaciones A-V.
- A las mujeres que se habían sometido a una biopsia o resección ganglionar axilar, o una mastectomía radical unilateral, no se les midió la presión arterial en el brazo afectado.

**Aspectos Destacados del Protocolo:**
- **Método de Medición:** Se tomaron tres mediciones consecutivas de la presión arterial (sistólica y diastólica) y del pulso con 60 segundos de diferencia.
- **Dispositivo Utilizado:** Un dispositivo electrónico digital para medir la presión arterial en la parte superior del brazo (Omron HEM–907XL).
- **Procedimientos:** 
  - Normalmente se tomaron mediciones estandarizadas en el **brazo derecho** a menos que las condiciones lo prohibieran.
  - Los participantes descansaron tranquilamente sentados durante 5 minutos antes de las mediciones.
  - Primero se midió la circunferencia de la parte superior del brazo para determinar el tamaño adecuado del manguito.

**Reglas de Procesamiento de Datos:**
- La PA sistólica no puede ser mayor de 300 mmHg.
- La PA sistólica debe ser estrictamente mayor que la PA diastólica.
- Si no se registra PA sistólica, no se puede registrar PA diastólica (aunque puede existir una medida sistólica sin una diastólica).

**Notas Analíticas:**
- **Cambio de Metodología:** Después del ciclo 2017-2018, NHANES pasó estrictamente al método de medición oscilométrica (Omron HEM–907XL) y suspendió el método auscultatorio (esfigmomanómetro de mercurio).
- **Pesos:** Los analistas deben usar los pesos de la muestra de Examen estándar para el análisis de datos.

**Variables Clave:**
*   **Identificadores de Encuesta y Medición:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado.
    *   **`Brazo`** (`BPAOARM`): Brazo seleccionado para la medición (L = Izquierdo, R = Derecho).
    *   **`Manguito`** (`BPAOCSZ`): Tamaño del manguito codificado basado en la circunferencia del brazo medio (2 = 17-21.9 cm, 3 = 22-31.9 cm, 4 = 32-41.9 cm, 5 = 42-50 cm).
*   **Lecturas de Presión Arterial (Sistólica y Diastólica):**
    Se proporcionan tres lecturas consecutivas:
    *   **Sistólica (1ª, 2ª, 3ª):** `Sistolica 1` (`BPXOSY1`), `Sistolica 2` (`BPXOSY2`), `Sistolica 3` (`BPXOSY3`)
    *   **Diastólica (1ª, 2ª, 3ª):** `Diastolica 1` (`BPXODI1`), `Diastolica 2` (`BPXODI2`), `Diastolica 3` (`BPXODI3`)
*   **Lecturas de Pulso:**
    Tres lecturas de pulso correspondientes:
    *   **Pulso (1º, 2º, 3º):** `Pulso 1` (`BPXOPLS1`), `Pulso 2` (`BPXOPLS2`), `Pulso 3` (`BPXOPLS3`)

### 5. Medidas Corporales (BMX_L)
**Publicado por primera vez:** Septiembre 2024

**Grupos de Edad Objetivo por Medición:**
No hubo exclusiones médicas/de seguridad para este protocolo. Las mediciones se recopilaron según la edad:
- **Peso:** Todas las edades
- **Circunferencia de la Cabeza:** Nacimiento - 6 meses
- **Longitud Recostado:** Nacimiento - 47 meses
- **Estatura de Pie:** 2+ años
- **Longitud de la Parte Superior de la Pierna:** 8+ años
- **Longitud de la Parte Superior del Brazo y Circunferencia del Brazo Medio:** 2+ meses
- **Circunferencia de la Cintura:** 2+ años
- **Circunferencia de la Cadera:** 12+ años

**Aspectos Destacados del Protocolo y Procedimiento:**
- **Ubicación:** Las medidas fueron recolectadas en el Centro de Examen Móvil (MEC) por técnicos de salud capacitados.
- **Lado del Brazo/Pierna:** Las medidas se tomaron en el lado **derecho** del cuerpo. Si una amputación o condición médica lo impedía, se utilizaba el lado izquierdo. 
- **Amputaciones:** Los datos del peso corporal se establecen como "faltantes" para personas con amputaciones de extremidades debido a riesgos de confidencialidad/divulgación.
- **Embarazo:** Las mujeres embarazadas fueron medidas, pero si una mujer estaba fuera del rango de edad de 20-44 años (el único rango donde se divulga públicamente el estado de embarazo), sus datos de medidas corporales se ocultan para evitar la divulgación.
- **Ropa:** Los técnicos documentaron si la ropa excesiva o los aparatos médicos interferían con las mediciones de peso mediante códigos de comentarios.

**Procesamiento de Datos y Notas Analíticas:**
- **Edición:** Los valores extremos (por encima del percentil 99 o por debajo del percentil 1) se revisaron con respecto a las características del sujeto (edad, sexo, altura, etc.). Se eliminaron los valores irreales. **No hay datos imputados**. 
- **Cálculo de IMC (`IMC` / `BMXBMI`):** Peso en kilogramos dividido por la altura en metros al cuadrado, redondeado a un decimal.
- **Categorías de IMC para niños (`BMDBMIC`):** Calculadas para edades de 2-19 basándose en las tablas de crecimiento del CDC que coinciden con la edad explícitamente en meses (1 = Bajo peso, 2 = Normal, 3 = Sobrepeso, 4 = Obeso). *Nota: la clasificación de peso en niños/adolescentes no es directamente comparable con las definiciones de adultos.*
- **Pesos:** Los analistas deben usar los pesos de la muestra del Examen para analizar estos datos.

**Variables Clave:**
*La mayoría de las mediciones físicas tienen una variable de código de comentario correspondiente que comienza con "BMI" (por ejemplo, `Peso Kg` tiene `BMIWT`) utilizada para indicar si la medida no se pudo obtener, se vio afectada por la ropa o no fue perfectamente recta.*
*   **Identificadores de Encuesta y Estado:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado.
    *   **`Estado Antropo`** (`BMDSTATS`): Código de Estado del Componente (1 = Completo, 2 = Parcial [solo altura/peso], 3 = Otro parcial, 4 = Sin datos de examen).
*   **Medidas Corporales Principales:**
    *   **`Peso Kg`** (`BMXWT`): Peso (kg) y **`BMIWT`**: Comentario
    *   **`Talla Cm`** (`BMXHT`): Estatura de pie (cm) y **`BMIHT`**: Comentario
    *   **`BMXRECUM`**: Longitud Recostado (cm) y **`BMIRECUM`**: Comentario
    *   **`BMXHEAD`**: Circunferencia de la cabeza (cm) y **`BMIHEAD`**: Comentario
*   **Índices Derivados:**
    *   **`IMC`** (`BMXBMI`): Índice de Masa Corporal (kg/m²)
    *   **`BMDBMIC`**: Categoría de IMC para Niños/Jóvenes (edades 2-19)
*   **Medidas de Extremidades y Tronco:**
    *   **`Pierna Cm`** (`BMXLEG`): Longitud de la parte superior de la pierna (cm) y **`BMILEG`**: Comentario
    *   **`Brazo Cm`** (`BMXARML`): Longitud de la parte superior del brazo (cm) y **`BMIARML`**: Comentario
    *   **`Perim. Brazo`** (`BMXARMC`): Circunferencia del brazo (cm) y **`BMIARMC`**: Comentario
    *   **`Cintura Cm`** (`BMXWAIST`): Circunferencia de la cintura (cm) y **`BMIWAIST`**: Comentario
    *   **`Cadera Cm`** (`BMXHIP`): Circunferencia de la cadera (cm) y **`BMIHIP`**: Comentario

### 6. Elastografía Transitoria por Ultrasonido Hepático (LUX_L)
**Población Objetivo:** Participantes de 12 años en adelante.
**Publicado por primera vez:** Septiembre 2024

**Metas y Objetivos:**
Este examen proporciona medidas objetivas para dos manifestaciones importantes de enfermedad hepática:
1. **Fibrosis Hepática (cicatrización):** Medida a través de la rigidez del hígado.
2. **Esteatosis Hepática (grasa en el hígado):** Medida a través del parámetro de atenuación controlada (CAP).

**Elegibilidad y Exclusiones:**
Se **excluyó** a los participantes de este examen si:
1. Embarazo esperado o confirmado (o si no podían proporcionar una muestra de orina).
2. Eran incapaces de recostarse de forma horizontal en la camilla de examen.
3. Tenían un dispositivo médico electrónico implantado (por ejemplo, bomba de insulina, marcapasos).
4. Llevaban un vendaje o tenían lesiones en el lado derecho del abdomen junto a las costillas donde se coloca la sonda.

**Aspectos Destacados del Protocolo:**
- **Dispositivo Utilizado:** FibroScan® modelo 502 V2 Touch (con sondas medianas [M] o extra grandes [XL]).
- **Procedimientos:** Una punta vibratoria envía una onda de corte a través del espacio intercostal hacia el hígado. La velocidad de esta onda se convierte en rigidez del tejido (expresada en kilopascales). El CAP se mide simultáneamente para indicar el contenido de grasa (expresado en dB/m).
- **Objetivo de Control de Calidad:** Los técnicos buscaron capturar 10 mediciones válidas donde la relación entre el rango intercuartílico y la mediana (IQR/M) fuera inferior al 30%.
- **Eliminación de Mediciones:** Para prevenir sesgos, los examinadores solo podían eliminar medidas al principio de una secuencia, sin escoger lecturas individuales a su conveniencia.

**Procesamiento de Datos y Notas Analíticas:**
- **Requisito de Ayuno:** Un examen "Completo" idealmente requiere un tiempo de ayuno de al menos 3 horas. Sin embargo, los datos se incluyen independientemente de la duración del ayuno.
- **Edición de Datos:** Se verificaron los valores extremos, pero la rigidez final, el CAP, el IQRe y los valores del IQRc obtenidos de la máquina **no se alteraron** y **no se imputaron valores**. Los valores atípicos altos pueden reflejar verdaderas condiciones biológicas o dificultades para medir debido a la constitución física (por ejemplo, obesidad o espacios intercostales estrechos).
- **Pesos:** Dependiendo de la naturaleza del análisis, utilice los pesos de la muestra del Examen estándar, a menos que se fusione con la muestra de ayuno matutino (en cuyo caso, use los pesos de ayuno correspondientes).

**Variables Clave:**
*   **Identificadores de Encuesta y Estado:**
    *   **`ID`** (`SEQN`): Número de secuencia del encuestado.
    *   **`Estado Higado`** (`LUAXSTAT`): Estado del examen de elastografía (1 = Completo, 2 = Parcial, 3 = Inelegible, 4 = No realizado).
    *   **`LUARXNC`**: Motivo del examen parcial (ej., ayuno < 3hrs, <10 medidas válidas, IQR/M >30%).
    *   **`LUARXND`** y **`LUARXIN`**: Motivos de un examen no realizado o inelegibilidad del participante.
    *   **`Sonda`** (`LUAPNME`): Tipo de sonda de examen utilizada (M o XL).
*   **Recuentos de Medidas:**
    *   **`Intentos`** (`LUANMTGP`): Recuento de medidas totales intentadas.
    *   **`Med. Validas`** (`LUANMVGP`): Recuento de medidas válidas y completas conservadas.
*   **Resultados de la Elastografía (Fibrosis vs Esteatosis):**
    *   **`Rigidez kPa`** (`LUXSMED`): Mediana de rigidez (E) en kilopascales (kPa). Alta rigidez indica fibrosis.
    *   **`IQR Rigidez`** (`LUXSIQR`): Rango intercuartílico de la rigidez (IQRe).
    *   **`Ratio IQR/M`** (`LUXSIQRM`): Proporción de IQRe / Mediana de la rigidez (utilizado para el umbral de control de calidad).
    *   **`CAP dB/m`** (`LUXCAPM`): Parámetro de Atenuación Controlada Mediana (CAP) en decibelios por metro (dB/m). Evalúa la esteatosis.
    *   **`IQR CAP`** (`LUXCPIQR`): Rango intercuartílico de CAP (IQRc).

### 7. Albúmina y Creatinina - Orina (ALB_CR_L)
**Población Objetivo:** Participantes examinados de 3 años en adelante.
**Publicado por primera vez:** Septiembre 2025

**Descripción del Componente:**
La albúmina es la proteína plasmática más abundante. La eliminación renal de la albúmina sérica se puede observar en casos graves de enfermedad renal y eventos cardiovasculares. La creatinina es un producto de degradación del fosfato de creatina en el músculo. La medición de la creatinina es útil en el diagnóstico y tratamiento de enfermedades renales, y como base de cálculo para otros analitos urinarios.

**Notas Analíticas:**
- **Cambio de Metodología (Albúmina):** Se proporcionan ecuaciones de regresión en la documentación oficial si se necesitan comparaciones cruzadas entre ciclos entre el nuevo método LC-MS/MS y el método de inmunoensayo fluorescente anterior.
- **Límites de Detección:** Para los analitos con mediciones por debajo del límite inferior de detección, se colocó un valor de relleno imputado en el campo de resultados del analito, calculado como LLOD/sqrt(2).

**Variables Clave:**
*   **`Albumina Orina`** (`URXUMA`): Albúmina, orina (ug/mL).
*   **`Albumina SI`** (`URXUMS`): Albúmina, orina (mg/L).
*   **`Com. Albumina`** (`URDUMALC`): Código de comentario de albúmina en orina.
*   **`Creatinina Orina`** (`URXUCR`): Creatinina, orina (mg/dL).
*   **`Creatinina SI`** (`URXCRS`): Creatinina, orina (umol/L).
*   **`Com. Creatinina`** (`URDUCRLC`): Código de comentario de creatinina en orina.
*   **`Ratio Alb/Cre`** (`URDACT`): Proporción de albúmina y creatinina (mg/g).

### 8. Glicoproteína alfa-1-ácida (AGP_L)
**Población Objetivo:** Participantes examinados de 1-5 años de edad y mujeres de 12-49 años de edad.
**Publicado por primera vez:** Septiembre 2024

**Descripción del Componente:**
La glicoproteína alfa-1-ácida (AGP) se sintetiza en el hígado. Es un reactante sensible de fase aguda cuya concentración puede aumentar cuando ocurre una inflamación. Este fue un componente nuevo en el ciclo de NHANES de agosto de 2021 a agosto de 2023.

**Notas Analíticas:**
- **Pesos de Flebotomía:** Debido a que el análisis de los patrones de falta de respuesta para el componente de flebotomía reveló diferencias, se ha incluido un peso de flebotomía adicional (`Peso Sangre` / `WTPH2YR`) para abordar el posible sesgo de falta de respuesta.

**Variables Clave:**
*   **`Peso Sangre`** (`WTPH2YR`): Peso de Flebotomía de 2 años.

### 9. Hemograma Completo con Diferencial de 5 Partes en Sangre Entera (CBC_L)
**Población Objetivo:** Participantes examinados de 1 año y mayores.
**Publicado por primera vez:** Septiembre 2024

**Descripción del Componente:**
El hemograma completo (CBC) con diferencial de 5 partes cuenta los glóbulos rojos (RBC), los glóbulos blancos (WBC) y las plaquetas, mide la hemoglobina; estima el volumen de los glóbulos rojos; y clasifica los WBC en subtipos. 

**Notas Analíticas:**
- **Pesos de Flebotomía:** Utiliza `Peso Sangre` para análisis derivados de analitos en sangre. Los participantes elegibles que no proporcionaron una muestra reciben un peso de "0".

**Variables Clave:**
*   **Glóbulos Blancos y Diferencial:**
    *   **`Blancos`** (`LBXWBCSI`): Recuento de glóbulos blancos (1000 células/uL).
    *   **`% Linfocitos` / `Linfocitos Abs`** (`LBXLYPCT` / `LBDLYMNO`): Porcentaje de linfocitos (%) y número (1000 células/uL).
    *   **`% Monocitos` / `Monocitos Abs`** (`LBXMOPCT` / `LBDMONO`): Porcentaje de monocitos (%) y número (1000 células/uL).
    *   **`% Neutrofilos` / `Neutrofilos Abs`** (`LBXNEPCT` / `LBDNENO`): Porcentaje de neutrófilos segmentados (%) y número (1000 células/uL).
    *   **`% Eosinofilos` / `Eosinofilos Abs`** (`LBXEOPCT` / `LBDEONO`): Porcentaje de eosinófilos (%) y número (1000 células/uL).
    *   **`% Basofilos` / `Basofilos Abs`** (`LBXBAPCT` / `LBDBANO`): Porcentaje de basófilos (%) y número (1000 células/uL).
*   **Glóbulos Rojos:**
    *   **`Rojos`** (`LBXRBCSI`): Recuento de glóbulos rojos (millones de células/uL).
    *   **`Hemoglobina`** (`LBXHGB`): Hemoglobina (g/dL).
    *   **`Hematocrito`** (`LBXHCT`): Hematocrito (%).
    *   **`VCM`** (`LBXMCVSI`): Volumen corpuscular medio (fL).
    *   **`CHCM`** (`LBXMC`): Concentración media de hemoglobina corpuscular (g/dL).
    *   **`HCM`** (`LBXMCHSI`): Hemoglobina corpuscular media (pg).
    *   **`RDW`** (`LBXRDW`): Amplitud de distribución de glóbulos rojos (%).
    *   **`NRBC`** (`LBXNRBC`): Glóbulos rojos nucleados (/100 WBC).
*   **Plaquetas:**
    *   **`Plaquetas`** (`LBXPLTSI`): Recuento de plaquetas (1000 células/uL).
    *   **`VPM`** (`LBXMPSI`): Volumen plaquetario medio (fL).

### 10. Colesterol – Lipoproteína de Alta Densidad (HDL_L)
**Población Objetivo:** Participantes examinados de 6 años en adelante.
**Publicado por primera vez:** Septiembre 2024

**Descripción del Componente:**
Se enfoca exclusivamente en la Lipoproteína de Alta Densidad (HDL-C), fundamental para la evaluación del riesgo cardiovascular.

**Notas Analíticas:**
- **Pesos de Flebotomía:** Utiliza `Peso Sangre` para abordar un posible sesgo por falta de respuesta.
- **Cambio de Metodología:** Se realizaron pruebas de transición para la actualización al Cobas 8000, pero se consideró innecesario hacer ajustes.

**Variables Clave:**
*   **`HDL`** (`LBDHDD`): Colesterol HDL directo (mg/dL).
*   **`HDL SI`** (`LBDHDDSI`): Colesterol HDL directo (mmol/L).

### 11. Proteína C Reactiva de Alta Sensibilidad (HSCRP_L)
**Población Objetivo:** Participantes examinados de 1 año en adelante.
**Publicado por primera vez:** Septiembre 2024

**Descripción del Componente:**
La proteína C reactiva (CRP) es una proteína de fase aguda sintetizada en el hígado, sirviendo como un indicador sensible de inflamación y riesgo de enfermedad cardiovascular.

**Notas Analíticas:**
- **Pesos de Flebotomía:** Utiliza `Peso Sangre` para abordar el posible sesgo de falta de respuesta.
- **Cambio de Metodología:** Se realizaron pruebas de transición debido a una actualización al instrumento Cobas 8000. Existen ecuaciones de regresión en la documentación oficial.

**Variables Clave:**
*   **`Proteina C`** (`LBXHSCRP`): Proteína C reactiva de alta sensibilidad (hs-CRP) (mg/L).
*   **`Com. PCR`** (`LBDHRPLC`): Código de comentario de Proteína C reactiva de alta sensibilidad (hs-CRP).

### 12. Plomo, Cadmio, Mercurio Total, Selenio y Manganeso – Sangre (PBCD_L)
**Población Objetivo:** Participantes examinados de 1 año en adelante.
**Publicado por primera vez:** Septiembre 2024

**Descripción del Componente:**
Evalúa la exposición a metales pesados y oligoelementos utilizando espectrometría de masas (ICP-MS) de muestras de sangre entera.

**Notas Analíticas:**
- **Pesos de Flebotomía:** Utiliza `Peso Sangre` para abordar el posible sesgo de falta de respuesta.

**Variables Clave:**
*   **Plomo:**
    *   **`Plomo` / `Plomo SI`** (`LBXBPB` / `LBDBPBSI`): Plomo en sangre en ug/dL y umol/L.
    *   **`Com. Plomo`** (`LBDBPBLC`): Código de comentario del plomo en sangre.
*   **Cadmio:**
    *   **`Cadmio` / `Cadmio SI`** (`LBXBCD` / `LBDBCDSI`): Cadmio en sangre en ug/L y nmol/L.
    *   **`Com. Cadmio`** (`LBDBCDLC`): Código de comentario del cadmio en sangre.
*   **Mercurio:**
    *   **`Mercurio` / `Mercurio SI`** (`LBXTHG` / `LBDTHGSI`): Mercurio en sangre, total en ug/L y nmol/L.
    *   **`Com. Mercurio`** (`LBDTHGLC`): Código de comentario del mercurio en sangre, total.
*   **Selenio:**
    *   **`Selenio` / `Selenio SI`** (`LBXBSE` / `LBDBSESI`): Selenio en sangre en ug/L y umol/L.
    *   **`Com. Selenio`** (`LBDBSELC`): Código de comentario del selenio en sangre.
*   **Manganeso:**
    *   **`Manganeso` / `Manganeso SI`** (`LBXBMN` / `LBDBMNSI`): Manganeso en sangre en ug/L y nmol/L.
    *   **`Com. Manganeso`** (`LBDBMNLC`): Código de comentario del manganeso en sangre.

### 13. Colesterol - Lipoproteínas de Baja Densidad (LDL) y Triglicéridos (TRIGLY_L)
**Población Objetivo:** Participantes de 12 años en adelante examinados en sesiones matutinas.
**Publicado por primera vez:** Septiembre 2025

**Descripción del Componente:**
Proporciona Triglicéridos medidos directamente y valores derivados de LDL-C.

**Notas Analíticas:**
- **Pesos de Submuestra:** Los analistas deben usar el **Peso MEC de 2 años de la Submuestra de Ayuno (`Peso Ayuno` / `WTSAF2YR`)**. 
- **Cambio de Metodología:** El ensayo con blanco de glicerol fue eliminado. Las ecuaciones de regresión garantizan la comparabilidad entre ciclos.

**Variables Clave:**
*   **Pesos:**
    *   **`Peso Ayuno`** (`WTSAF2YR`): Peso MEC de 2 años de la Submuestra de Ayuno.
*   **Triglicéridos:**
    *   **`Trigliceridos`** (`LBXTLG`): Triglicéridos (mg/dL).
    *   **`Trigli. SI`** (`LBDTRSI`): Triglicéridos (mmol/L).
*   **Colesterol LDL Calculado (Friedewald):**
    *   **`LDL` / `LDL SI`** (`LBDLDL` / `LBDLDLSI`): Colesterol LDL, Friedewald en mg/dL y mmol/L.
*   **Colesterol LDL Calculado (Martin-Hopkins):**
    *   **`LDL Martin` / `LDL Martin SI`** (`LBDLDLM` / `LBDLDMSI`): Colesterol LDL, Martin-Hopkins en mg/dL y mmol/L.
*   **Colesterol LDL Calculado (Ecuación 2 del NIH):**
    *   **`LDL NIH` / `LDL NIH SI`** (`LBDLDLN` / `LBDLDNSI`): Colesterol LDL, Ecuación 2 del NIH en mg/dL y mmol/L.
