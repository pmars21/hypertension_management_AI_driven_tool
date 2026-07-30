# Hypertension Management AI-Driven Tool

## Descripción del proyecto

Este proyecto implementa un flujo de trabajo completo de ciencia de datos centrado en la estimación del riesgo de hipertensión a partir de los datos de la NHANES (Encuesta Nacional de Examen de Salud y Nutrición). El proyecto combina la preparación de datos, el análisis exploratorio, la ingeniería de características, la selección de características, el entrenamiento de modelos y la puntuación de probabilidad en un proceso reproducible de estilo investigativo centrado en los factores clínicos y de estilo de vida relacionados con la presión arterial.

El proyecto utiliza múltiples componentes de NHANES (módulos demográficos, de exploración, de laboratorio y dietéticos) y los fusiona en un conjunto de datos analítico unificado. Las fuentes de datos sin procesar se organizan en la carpeta `/data`, incluyendo diccionarios, subconjuntos fusionados, divisiones de entrenamiento y prueba, y archivos de apoyo. Un script de utilidad (`/data/xpt/convert_xpt_to_csv.py`) permite convertir archivos XPT de NHANES a formato CSV, lo que facilita su incorporación al flujo de trabajo del cuaderno.

El preprocesamiento de los datos se realiza en gran medida a través de cuadernos de trabajo. Las tareas clave de preprocesamiento incluyen el tratamiento de valores nulos, la imputación mediante estrategias iterativas basadas en árboles al estilo de MissForest (`missForest_imp_tfm.ipynb`) y la preparación de archivos de entrenamiento y prueba, como `train_imputado.csv` y `test_imputado.csv`. El repositorio también incluye varios cuadernos exploratorios para el análisis por dominio (`/analisis_mergedSets`) y experimentos de agrupamiento (`/clustering`) con el fin de comprender mejor la estructura, la separabilidad y el comportamiento de las características antes de la modelización supervisada.

Para la modelización predictiva, el proyecto aplica una selección de características basada en algoritmos genéticos (GA) utilizando pyWinEA 

# Resumen del Dataset: NHANES Merged Dataset (merged_all.csv)

## Información General

- **Nombre de la Encuesta:** National Health and Nutrition Examination Survey (NHANES)
- **Ciclo de Datos:** Agosto 2021 - Agosto 2023 (principalmente)
- **Componente:** Dataset multi-componente consolidado
- **Archivo de Datos:** `merged_all.csv`
- **Población Objetivo:** Varía según el componente (generalmente participantes de 1 a 80+ años, con restricciones específicas de edad para componentes como presión arterial, equilibrio y elastografía).

## Alcance y Metodología

Este dataset es un archivo consolidado que combina múltiples componentes de NHANES en un único archivo plano. Utiliza el número de secuencia del encuestado (`id_participante` (SEQN)) para vincular datos demográficos, de exploración, laboratorio y cuestionarios de cada participante.

**Componentes incluidos según las variables:**

- Demografía (`DEMO_L`)
- Medidas Corporales (`BMX_L`)
- Presión Arterial (`BPXO_L`)
- Equilibrio (`BAX_L`)
- Elastografía Hepática por Ultrasonido Transitorio (`LUX_L`)
- Suplementos Dietéticos (`DSQTOT_L`)
- Datos de Laboratorio (Hemograma Completo, Lípidos, Metales Pesados, Albúmina/Creatinina en Orina)

**Notas Analíticas:**

Dado que este dataset combina múltiples componentes (Demografía, Exámenes MEC, Dieta y Submuestras de Laboratorio), los analistas deben seleccionar cuidadosamente la variable de peso apropiada (por ejemplo, `peso_entrevista_2a` (WTINT2YR), `peso_examen_mec_2a` (WTMEC2YR), `peso_dieta_dia1` (WTDRD1), `peso_flebotomia_2a` (WTPH2YR), `peso_muestra_ayuno_2a` (WTSAF2YR)) según las variables y subpoblaciones que se analicen. Muchas columnas contienen valores faltantes (`NaN`) derivados de exclusiones intencionales (por ejemplo, mujeres embarazadas en elastografía) o restricciones del protocolo basadas en la edad.

---

## Descripción de las Variables Clave

### 1. Identificadores, Demografía y Pesos (DEMO_L)

**Población Objetivo:** Todos los participantes de la muestra NHANES Ago 2021 - Ago 2023.
**Primera Publicación:** Septiembre 2024
**Valores Faltantes:** Codificados como *.*

**Contexto de la Encuesta y Notas Analíticas (Impacto COVID-19):**

La recolección de datos se reanudó en agosto de 2021 tras su suspensión en marzo de 2020. No se realizó sobremuestreo por raza/origen hispano ni por ingresos (a diferencia de ciclos anteriores), aunque sí se añadió sobremuestreo por grupo de edad. Existe una brecha de 15 meses entre este ciclo y el anterior, por lo que se recomienda extremar la cautela al combinar datos con ciclos previos o realizar análisis de tendencias. Algunas variables han sido truncadas por razones de confidencialidad (estado civil, embarazo, edad 80+, tamaños de hogar superiores a 7).

#### Identificadores y Administración de la Encuesta

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado (identificador único) |
| `ciclo_datos` | (SDDSRVYR) | Ciclo de publicación de datos (`12` = ciclo Ago 2021 - Ago 2023) |
| `estado_entrevista` | (RIDSTATR) | Estado de entrevista/examen (1 = Solo entrevistado; 2 = Entrevistado y examinado en MEC) |
| `periodo_examen` | (RIDEXMON) | Periodo semestral en que se realizó el examen |

#### Demografía

| Variable | Variable Original | Descripción |
|---|---|---|
| `genero` | (RIAGENDR) | Género (Masculino=1, Femenino=2) |
| `edad_anios` | (RIDAGEYR) | Edad en años al momento del cribado (truncada a 80 años) |
| `edad_meses` | (RIDAGEMN / RIDEXAGM) | Edad en meses (para niños pequeños/jóvenes) |
| `raza_etnia` | (RIDRETH1 / RIDRETH3) | Raza/origen hispano (Mexicano-Americano, Otro Hispano, Blanco No Hispano, Negro No Hispano, Asiático No Hispano, Otro/Multirracial) |
| `nivel_educacion` | (DMDEDUC2) | Nivel de educación para adultos de 20+ años |
| `estado_civil` | (DMDMARTZ) | Estado civil |
| `servicio_militar` | (DMQMILIZ) | Sirvió en las Fuerzas Armadas de EE.UU. |

#### Lugar de Nacimiento y Residencia

| Variable | Variable Original | Descripción |
|---|---|---|
| `pais_nacimiento` | (DMDBORN4) | País de nacimiento (Nacido en EE.UU. vs. Nacido en otro país) |
| `tiempo_residencia_us` | (DMDYRUSR) | Tiempo viviendo en EE.UU. (categórico) |

#### Hogar e Ingresos

| Variable | Variable Original | Descripción |
|---|---|---|
| `tamano_hogar` | (DMDHHSIZ) | Número total de personas en el hogar (truncado en 7 o más) |
| `ratio_ingresos_pobreza` | (INDFMPIR) | Relación entre ingresos familiares y umbral de pobreza (truncado en 5.00) |
| `genero_ref_hogar` | (DMDHRGND) | Género de la persona de referencia del hogar |
| `edad_ref_hogar` | (DMDHRAGZ) | Edad de la persona de referencia del hogar |
| `educacion_ref_hogar` | (DMDHREDZ) | Educación de la persona de referencia del hogar |
| `estado_civil_ref_hogar` | (DMDHRMAZ) | Estado civil de la persona de referencia del hogar |

#### Estado Médico / Físico

| Variable | Variable Original | Descripción |
|---|---|---|
| `estado_embarazo` | (RIDEXPRG) | Estado de embarazo en el momento del examen (publicado solo para mujeres de 20-44 años) |

#### Pesos Muestrales y Estimación de Varianza

| Variable | Variable Original | Descripción |
|---|---|---|
| `peso_entrevista_2a` | (WTINT2YR) | Peso de entrevista de 2 años para la muestra completa |
| `peso_examen_mec_2a` | (WTMEC2YR) | Peso de examen MEC de 2 años para la muestra completa |
| `estrato_varianza` | (SDMVSTRA) | Pseudo-estrato de varianza enmascarado |
| `psu_varianza` | (SDMVPSU) | Pseudo-PSU de varianza enmascarado |

---

### 2. Suplementos Dietéticos (DSQTOT_L)

**Población Objetivo:** Todos los participantes de la encuesta.
**Primera Publicación:** Febrero 2025

**Alcance y Contenido:**

Este componente captura el uso en los últimos 30 días de: suplementos dietéticos (con y sin receta: vitaminas, minerales, plantas medicinales) y antiácidos sin receta que contengan calcio y/o magnesio.

El archivo `DSQTOT_L` resume la **ingesta diaria media total** de 34 nutrientes por participante procedentes de todos sus suplementos y antiácidos combinados.

**Notas del Protocolo e Impacto COVID-19:**

La recogida de datos se realizó mediante entrevista telefónica (CATI) tras la primera encuesta dietética de 24 horas. Los participantes leyeron las etiquetas de los envases al entrevistador por teléfono. Se eliminaron las preguntas sobre duración del uso y motivo de consumo del suplemento.

**Procesamiento de Datos y Pesos Muestrales:**

Los suplementos reportados fueron emparejados por nutricionistas del NCHS con la base de datos NHANES-DSD. Dado que esta encuesta se realizó simultáneamente al recuerdo dietético del Día 1, los analistas **deben usar el peso muestral del Día 1 de dieta (`peso_dieta_dia1` (WTDRD1))**. No deben usarse los pesos estándar MEC ni de entrevista.

#### Variables de Peso e Identificadores

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado |
| `peso_dieta_dia1` | (WTDRD1) | Peso muestral del día 1 de dieta |

#### Uso General y Recuentos

| Variable | Variable Original | Descripción |
|---|---|---|
| `toma_suplementos` | (DSD010) | ¿Toma algún suplemento dietético? (1 = Sí, 2 = No) |
| `toma_antiacidos` | (DSD010AN) | ¿Toma algún antiácido? (1 = Sí, 2 = No) |
| `cant_suplementos` | (DSDCOUNT) | Número total de suplementos dietéticos tomados |
| `cant_antiacidos` | (DSDANCNT) | Número total de antiácidos tomados |

#### Ingesta Diaria Media Agregada de Nutrientes

Las variables con prefijo `sup_` representan la ingesta media diaria total procedente de todos los suplementos/antiácidos del individuo.

| Variable | Variable Original | Descripción |
|---|---|---|
| `sup_energia_kcal` | (DSQTKCAL) | Energía (kcal) |
| `sup_proteina` | (DSQTPROT) | Proteína (g) |
| `sup_carbohidratos` | (DSQTCARB) | Carbohidratos (g) |
| `sup_azucar` | (DSQTSUGR) | Azúcar (g) |
| `sup_fibra` | (DSQTFIBE) | Fibra (g) |
| `sup_grasas_totales` | (DSQTTFAT) | Grasas totales (g) |
| `sup_grasas_saturadas` | (DSQTSFAT) | Grasas saturadas (g) |
| `sup_vitamina_c` | (DSQTVC) | Vitamina C (mg) |
| `sup_vitamina_d` | (DSQTVD) | Vitamina D (mcg) |
| `sup_vitamina_b12` | (DSQTVB12) | Vitamina B12 (mcg) |
| `sup_acido_folico` | (DSQTFA) | Ácido fólico (mcg) |
| `sup_calcio` | (DSQTCALC) | Calcio (mg) |
| `sup_hierro` | (DSQTIRON) | Hierro (mg) |
| `sup_magnesio` | (DSQTMAGN) | Magnesio (mg) |
| `sup_zinc` | (DSQTZINC) | Zinc (mg) |
| `sup_cafeina` | (DSQTCAFF) | Cafeína (mg) |
| `sup_luteina` | (DSQTLZ) | Luteína/zeaxantina (mcg) |

*(Consultar el Apéndice 2 de la documentación oficial para la lista completa de los 34 nutrientes calculados.)*

---

### 3. Prueba de Equilibrio (BAX_L)

**Población Objetivo:** Participantes de 20 a 69 años.
**Primera Publicación:** Octubre 2024

**Elegibilidad y Exclusiones:**

Los participantes fueron **excluidos** si: estaban embarazadas o superaban los 315 libras, tenían discapacidad visual grave, no podían mantenerse de pie de forma independiente, tenían amputaciones o prótesis en extremidades inferiores, habían sufrido lesiones o cirugías recientes en piernas/tobillos/pies, presentaban mareos con historial de caídas, llevaban tacones de más de 3 pulgadas, o no podían ajustarse correctamente el cinturón de seguridad. Para la Condición 5, también se excluía a quienes tenían dolor cervical, cirugía previa de cuello o problemas cervicales crónicos.

**Protocolo: Test de Romberg Modificado (TRM)**

El TRM evalúa el equilibrio en cinco condiciones de dificultad creciente. Un participante falla una condición si no mantiene el equilibrio el tiempo requerido en dos intentos.

| Condición | Superficie | Visión |
|---|---|---|
| Condición 1 | Suelo firme | Ojos abiertos |
| Condición 2 | Suelo firme | Ojos cerrados |
| Condición 3 | Foam denso | Ojos abiertos |
| Condición 4 | Foam denso | Ojos cerrados |
| Condición 5 | Foam denso | Ojos cerrados + movimiento lateral de cabeza |

Criterio de superación: 15 segundos para las Condiciones 1 y 2; 20 segundos para las Condiciones 3, 4 y 5.

#### Identificadores y Estado del Examen

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado |
| `estado_examen_balance` | (BAXMSTAT) | Estado del examen TRM (1 = Completo, 2 = Parcial, 3 = No realizado, 4 = No elegible) |
| `elegibilidad_balance_cond5` | (BAX5STAT) | Elegibilidad específica para la Condición 5 |
| `razon_balance_parcial` | (BAXRXNC) | Razón del examen parcial |
| `razon_balance_no_realizado` | (BAXRXND) | Razón del examen no realizado |

#### Preguntas de Cribado Previas al Test

| Variable | Variable Original | Descripción |
|---|---|---|
| `filtro_balance_110` a `filtro_balance_173` | (BAQ110 a BAQ173) | Preguntas de cribado sobre capacidad de mantenerse de pie, aparatos ortopédicos, lesiones, mareos, historial de caídas, dolor cervical y consentimiento |

#### Resultados por Ensayo (Condiciones 1-5, Intentos 1 y 2)

Convención de nombres: **[prefijo][nº condición][nº intento]**

| Variable (ejemplo) | Variable Original (ejemplo) | Descripción |
|---|---|---|
| `aprueba_cond1_int1` | (BAXPF11) | Superado/No superado para la condición e intento específicos |
| `tiempo_seg_cond1_int1` | (BAXTC11) | Duración mantenida durante el ensayo (segundos) |
| `razon_paro_cond1_int1` | (BAARFC11) | Razón de finalización del ensayo (1 = Pies movidos, 2 = Brazos separados, 3 = Ojos abiertos, 4 = Intervención del técnico, 5 = Agarró/tocó la pared) |

---

### 4. Presión Arterial Oscilométrica (BPXO_L)

**Población Objetivo:** Participantes de 8 años en adelante.
**Primera Publicación:** Septiembre 2024

**Elegibilidad y Exclusiones:**

Los participantes fueron excluidos si presentaban en ambos brazos condiciones como erupciones, vendajes, escayolas, edema, parálisis, llagas abiertas o fístulas A-V. Las mujeres con biopsia axilar o mastectomía radical unilateral no fueron medidas en el brazo afectado.

**Protocolo:**

Se tomaron tres mediciones consecutivas de presión arterial (sistólica y diastólica) y pulso con 60 segundos de separación, usando el dispositivo Omron HEM-907XL. Habitualmente en el **brazo derecho**, tras 5 minutos de reposo sentado.

#### Identificadores y Datos de Medición

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado |
| `brazo_medicion_pa` | (BPAOARM) | Brazo seleccionado para la medición (I = Izquierdo, D = Derecho) |
| `tamano_manguito_pa` | (BPAOCSZ) | Tamaño del manguito según circunferencia del brazo (2 = 17-21,9 cm; 3 = 22-31,9 cm; 4 = 32-41,9 cm; 5 = 42-50 cm) |

#### Lecturas de Presión Arterial

| Variable | Variable Original | Descripción |
|---|---|---|
| `pa_sistolica_1` | (BPXOSY1) | Presión sistólica, 1.ª medición (mmHg) |
| `pa_sistolica_2` | (BPXOSY2) | Presión sistólica, 2.ª medición (mmHg) |
| `pa_sistolica_3` | (BPXOSY3) | Presión sistólica, 3.ª medición (mmHg) |
| `pa_diastolica_1` | (BPXODI1) | Presión diastólica, 1.ª medición (mmHg) |
| `pa_diastolica_2` | (BPXODI2) | Presión diastólica, 2.ª medición (mmHg) |
| `pa_diastolica_3` | (BPXODI3) | Presión diastólica, 3.ª medición (mmHg) |
| `pulso_1` | (BPXOPLS1) | Pulso, 1.ª medición (lpm) |
| `pulso_2` | (BPXOPLS2) | Pulso, 2.ª medición (lpm) |
| `pulso_3` | (BPXOPLS3) | Pulso, 3.ª medición (lpm) |

---

### 5. Medidas Corporales (BMX_L)

**Primera Publicación:** Septiembre 2024

**Grupos de Edad por Medición:**

| Medición | Rango de edad |
|---|---|
| Peso | Todas las edades |
| Circunferencia cefálica | Nacimiento - 6 meses |
| Longitud en decúbito | Nacimiento - 47 meses |
| Talla de pie | 2+ años |
| Longitud del muslo | 8+ años |
| Longitud del brazo y circunferencia braquial | 2+ meses |
| Circunferencia de cintura | 2+ años |
| Circunferencia de cadera | 12+ años |

**Notas:** No existen exclusiones médicas/de seguridad. Las medidas corporales de personas con amputaciones de extremidades se declaran como faltantes por razones de confidencialidad. El IMC (`imc` (BMXBMI)) se calcula como peso (kg) / altura² (m²). No hay datos imputados.

#### Identificadores y Estado

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado |
| `estado_medidas_corp` | (BMDSTATS) | Código de estado del componente (1 = Completo, 2 = Parcial [solo talla/peso], 3 = Otro parcial, 4 = Sin datos) |

#### Mediciones Corporales Principales

| Variable | Variable Original | Descripción |
|---|---|---|
| `peso_kg` | (BMXWT) | Peso (kg) |
| `nota_peso` | (BMIWT) | Código de comentario sobre el peso |
| `altura_cm` | (BMXHT) | Talla de pie (cm) |
| `nota_altura` | (BMIHT) | Código de comentario sobre la talla |
| `longitud_recostado_cm` | (BMXRECUM) | Longitud en decúbito (cm) |
| `nota_longitud` | (BMIRECUM) | Código de comentario sobre la longitud |
| `circunferencia_cabeza_cm` | (BMXHEAD) | Circunferencia cefálica (cm) |
| `nota_cabeza` | (BMIHEAD) | Código de comentario sobre la cabeza |

#### Índices Derivados

| Variable | Variable Original | Descripción |
|---|---|---|
| `imc` | (BMXBMI) | Índice de Masa Corporal (kg/m²) |
| `categoria_imc_infantil` | (BMDBMIC) | Categoría de IMC para niños/jóvenes de 2-19 años (1 = Bajo peso, 2 = Normal, 3 = Sobrepeso, 4 = Obeso) |

#### Medidas de Extremidades y Tronco

| Variable | Variable Original | Descripción |
|---|---|---|
| `largo_pierna_superior_cm` | (BMXLEG) | Longitud del muslo (cm) |
| `nota_pierna` | (BMILEG) | Código de comentario sobre la pierna |
| `largo_brazo_superior_cm` | (BMXARML) | Longitud del brazo superior (cm) |
| `nota_largo_brazo` | (BMIARML) | Código de comentario sobre el largo del brazo |
| `circunferencia_brazo_cm` | (BMXARMC) | Circunferencia braquial (cm) |
| `nota_circunferencia_brazo` | (BMIARMC) | Código de comentario sobre la circunferencia del brazo |
| `circunferencia_cintura_cm` | (BMXWAIST) | Circunferencia de cintura (cm) |
| `nota_cintura` | (BMIWAIST) | Código de comentario sobre la cintura |
| `circunferencia_cadera_cm` | (BMXHIP) | Circunferencia de cadera (cm) |
| `nota_cadera` | (BMIHIP) | Código de comentario sobre la cadera |

---

### 6. Elastografía Hepática por Ultrasonido Transitorio (LUX_L)

**Población Objetivo:** Participantes de 12 años en adelante.
**Primera Publicación:** Septiembre 2024

**Objetivos:**

Proporciona medidas objetivas de dos manifestaciones importantes de enfermedad hepática:

1. **Fibrosis hepática (cicatrización):** Medida mediante la rigidez hepática.
2. **Esteatosis hepática (grasa en el hígado):** Medida mediante el parámetro de atenuación controlada (CAP).

**Elegibilidad y Exclusiones:**

Fueron excluidos los participantes que: estaban embarazadas o no podían aportar muestra de orina, no podían tumbarse en la camilla, llevaban dispositivos electrónicos implantados (marcapasos, bomba de insulina) o tenían vendajes/lesiones en el lado derecho del abdomen.

**Protocolo:**

Dispositivo FibroScan® modelo 502 V2 Touch (sondas M o XL). Se buscan 10 mediciones válidas con un ratio IQR/mediana < 30%. La rigidez se expresa en kilopascales (kPa) y el CAP en dB/m.

#### Identificadores y Estado

| Variable | Variable Original | Descripción |
|---|---|---|
| `id_participante` | (SEQN) | Número de secuencia del encuestado |
| `estado_elastografia` | (LUAXSTAT) | Estado del examen (1 = Completo, 2 = Parcial, 3 = No elegible, 4 = No realizado) |
| `razon_elasto_parcial` | (LUARXNC) | Razón del examen parcial |
| `razon_elasto_no_realizado` | (LUARXND) | Razón del examen no realizado |
| `ineligibilidad_elasto` | (LUARXIN) | Razón de inelegibilidad |
| `tipo_sonda_elasto` | (LUAPNME) | Tipo de sonda utilizada (M o XL) |
| `intentos_totales_elasto` | (LUANMTGP) | Número total de mediciones intentadas |
| `medidas_validas_elasto` | (LUANMVGP) | Número de mediciones válidas retenidas |

#### Resultados de Elastografía

| Variable | Variable Original | Descripción |
|---|---|---|
| `rigidez_mediana_kpa` | (LUXSMED) | Rigidez mediana (E) en kPa — valores altos indican fibrosis |
| `rigidez_iqr` | (LUXSIQR) | Rango intercuartílico de la rigidez (IQRe) |
| `ratio_iqr_mediana` | (LUXSIQRM) | Ratio IQRe / Mediana de rigidez (control de calidad) |
| `cap_mediana_db_m` | (LUXCAPM) | Parámetro de atenuación controlada mediano en dB/m — evalúa esteatosis |
| `cap_iqr` | (LUXCPIQR) | Rango intercuartílico del CAP (IQRc) |

---

### 7. Analíticas de Laboratorio

#### 7.1 Albúmina y Creatinina en Orina (ALB_CR_L)

**Población Objetivo:** Participantes examinados de 3 años en adelante.
**Primera Publicación:** Septiembre 2025

La albúmina es la proteína plasmática más abundante; su eliminación renal puede observarse en enfermedad renal grave y eventos cardiovasculares. La creatinina es un producto de degradación de la fosfocreatina muscular, útil en el diagnóstico y tratamiento de enfermedades renales.

| Variable | Variable Original | Descripción |
|---|---|---|
| `albumina_orina_ug_ml` | (URXUMA) | Albúmina en orina (ug/mL) |
| `albumina_orina_mg_l` | (URXUMS) | Albúmina en orina (mg/L) |
| `nota_albumina_orina` | (URDUMALC) | Código de comentario sobre la albúmina en orina |
| `creatinina_orina_mg_dl` | (URXUCR) | Creatinina en orina (mg/dL) |
| `creatinina_orina_umol_l` | (URXCRS) | Creatinina en orina (umol/L) |
| `nota_creatinina_orina` | (URDUCRLC) | Código de comentario sobre la creatinina en orina |
| `ratio_albumina_creatinina` | (URDACT) | Cociente albúmina/creatinina (mg/g) |

#### 7.2 Alfa-1-Glicoproteína Ácida / Pesos de Flebotomía (AGP_L)

**Población Objetivo:** Participantes examinados de 1-5 años y mujeres de 12-49 años.
**Primera Publicación:** Septiembre 2024

La alfa-1-glicoproteína ácida (AGP) es sintetizada en el hígado y actúa como reactante de fase aguda sensible, cuya concentración aumenta con la inflamación. Este fue un componente nuevo en el ciclo NHANES Ago 2021 - Ago 2023.

| Variable | Variable Original | Descripción |
|---|---|---|
| `peso_flebotomia_2a` | (WTPH2YR) | Peso de flebotomía de 2 años (para analíticas sanguíneas) |

#### 7.3 Hemograma Completo con Diferencial de 5 Partes (CBC_L)

**Población Objetivo:** Participantes examinados de 1 año en adelante.
**Primera Publicación:** Septiembre 2024

El hemograma completo con diferencial cuenta glóbulos rojos (GR), glóbulos blancos (GB) y plaquetas; mide la hemoglobina; estima el volumen celular; y clasifica los GB en subtipos.

**Glóbulos Blancos y Diferencial:**

| Variable | Variable Original | Descripción |
|---|---|---|
| `leucocitos_totales` | (LBXWBCSI) | Recuento de leucocitos (1000 células/uL) |
| `linfocitos_pct` | (LBXLYPCT) | Porcentaje de linfocitos (%) |
| `linfocitos_abs` | (LBDLYMNO) | Recuento absoluto de linfocitos (1000 células/uL) |
| `monocitos_pct` | (LBXMOPCT) | Porcentaje de monocitos (%) |
| `monocitos_abs` | (LBDMONO) | Recuento absoluto de monocitos (1000 células/uL) |
| `neutrofilos_pct` | (LBXNEPCT) | Porcentaje de neutrófilos segmentados (%) |
| `neutrofilos_abs` | (LBDNENO) | Recuento absoluto de neutrófilos (1000 células/uL) |
| `eosinofilos_pct` | (LBXEOPCT) | Porcentaje de eosinófilos (%) |
| `eosinofilos_abs` | (LBDEONO) | Recuento absoluto de eosinófilos (1000 células/uL) |
| `basofilos_pct` | (LBXBAPCT) | Porcentaje de basófilos (%) |
| `basofilos_abs` | (LBDBANO) | Recuento absoluto de basófilos (1000 células/uL) |

**Glóbulos Rojos:**

| Variable | Variable Original | Descripción |
|---|---|---|
| `eritrocitos_totales` | (LBXRBCSI) | Recuento de eritrocitos (millones de células/uL) |
| `hemoglobina_g_dl` | (LBXHGB) | Hemoglobina (g/dL) |
| `hematocrito_pct` | (LBXHCT) | Hematocrito (%) |
| `volumen_corpuscular_medio` | (LBXMCVSI) | Volumen corpuscular medio (fL) |
| `conc_hemoglobina_media` | (LBXMC) | Concentración de hemoglobina corpuscular media (g/dL) |
| `hemoglobina_corpuscular_media` | (LBXMCHSI) | Hemoglobina corpuscular media (pg) |
| `ancho_distribucion_eritrocitos` | (LBXRDW) | Amplitud de distribución eritrocitaria (%) |
| `eritrocitos_nucleados` | (LBXNRBC) | Eritrocitos nucleados (/100 GB) |

**Plaquetas:**

| Variable | Variable Original | Descripción |
|---|---|---|
| `plaquetas_totales` | (LBXPLTSI) | Recuento de plaquetas (1000 células/uL) |
| `volumen_plaquetario_medio` | (LBXMPSI) | Volumen plaquetario medio (fL) |

#### 7.4 Colesterol HDL (HDL_L)

**Población Objetivo:** Participantes examinados de 6 años en adelante.
**Primera Publicación:** Septiembre 2024

| Variable | Variable Original | Descripción |
|---|---|---|
| `hdl_mg_dl` | (LBDHDD) | Colesterol HDL directo (mg/dL) |
| `hdl_mmol_l` | (LBDHDDSI) | Colesterol HDL directo (mmol/L) |

#### 7.5 Proteína C-Reactiva de Alta Sensibilidad (HSCRP_L)

**Población Objetivo:** Participantes examinados de 1 año en adelante.
**Primera Publicación:** Septiembre 2024

La PCR es una proteína de fase aguda sintetizada en el hígado, indicadora sensible de inflamación y riesgo cardiovascular.

| Variable | Variable Original | Descripción |
|---|---|---|
| `proteina_c_reactiva_mg_l` | (LBXHSCRP) | Proteína C-reactiva de alta sensibilidad (mg/L) |
| `nota_proteina_c_reactiva` | (LBDHRPLC) | Código de comentario sobre la PCR |

#### 7.6 Metales Pesados en Sangre: Plomo, Cadmio, Mercurio, Selenio y Manganeso (PBCD_L)

**Población Objetivo:** Participantes examinados de 1 año en adelante.
**Primera Publicación:** Septiembre 2024

Evalúa la exposición a metales pesados y oligoelementos mediante espectrometría de masas con plasma acoplado inductivamente (ICP-MS).

| Variable | Variable Original | Descripción |
|---|---|---|
| `plomo_sangre_ug_dl` | (LBXBPB) | Plomo en sangre (ug/dL) |
| `plomo_sangre_umol_l` | (LBDBPBSI) | Plomo en sangre (umol/L) |
| `nota_plomo` | (LBDBPBLC) | Código de comentario sobre el plomo |
| `cadmio_sangre_ug_l` | (LBXBCD) | Cadmio en sangre (ug/L) |
| `cadmio_sangre_nmol_l` | (LBDBCDSI) | Cadmio en sangre (nmol/L) |
| `nota_cadmio` | (LBDBCDLC) | Código de comentario sobre el cadmio |
| `mercurio_sangre_ug_l` | (LBXTHG) | Mercurio total en sangre (ug/L) |
| `mercurio_sangre_nmol_l` | (LBDTHGSI) | Mercurio total en sangre (nmol/L) |
| `nota_mercurio` | (LBDTHGLC) | Código de comentario sobre el mercurio |
| `selenio_sangre_ug_l` | (LBXBSE) | Selenio en sangre (ug/L) |
| `selenio_sangre_umol_l` | (LBDBSESI) | Selenio en sangre (umol/L) |
| `nota_selenio` | (LBDBSELC) | Código de comentario sobre el selenio |
| `manganeso_sangre_ug_l` | (LBXBMN) | Manganeso en sangre (ug/L) |
| `manganeso_sangre_nmol_l` | (LBDBMNSI) | Manganeso en sangre (nmol/L) |
| `nota_manganeso` | (LBDBMNLC) | Código de comentario sobre el manganeso |

#### 7.7 Colesterol LDL y Triglicéridos (TRIGLY_L)

**Población Objetivo:** Participantes de 12 años en adelante examinados en sesiones matinales.
**Primera Publicación:** Septiembre 2025

**Nota analítica clave:** Los analistas deben usar el **peso muestral de ayuno de 2 años (`peso_muestra_ayuno_2a` (WTSAF2YR))**, ya que esta submuestra requiere un ayuno previo.

| Variable | Variable Original | Descripción |
|---|---|---|
| `peso_muestra_ayuno_2a` | (WTSAF2YR) | Peso muestral de la submuestra en ayunas de 2 años |
| `trigliceridos_mg_dl` | (LBXTLG) | Triglicéridos (mg/dL) |
| `trigliceridos_mmol_l` | (LBDTRSI) | Triglicéridos (mmol/L) |
| `ldl_friedewald_mg_dl` | (LBDLDL) | Colesterol LDL calculado, método Friedewald (mg/dL) |
| `ldl_friedewald_mmol_l` | (LBDLDLSI) | Colesterol LDL calculado, método Friedewald (mmol/L) |
| `ldl_martin_mg_dl` | (LBDLDLM) | Colesterol LDL calculado, método Martin-Hopkins (mg/dL) |
| `ldl_martin_mmol_l` | (LBDLDMSI) | Colesterol LDL calculado, método Martin-Hopkins (mmol/L) |
| `ldl_nih_mg_dl` | (LBDLDLN) | Colesterol LDL calculado, ecuación NIH 2 (mg/dL) |
| `ldl_nih_mmol_l` | (LBDLDNSI) | Colesterol LDL calculado, ecuación NIH 2 (mmol/L) |
