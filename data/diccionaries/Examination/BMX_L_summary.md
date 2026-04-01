# Dataset Summary: NHANES Body Measures (BMX_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Body Measures
- **Data File:** `BMX_L.xpt`
- **First Published:** September 2024

## Target Age Groups by Measurement
There were no medical/safety exclusions for this protocol. Measurements were collected based on age:
- **Weight:** All ages
- **Head Circumference:** Birth - 6 months
- **Recumbent Length:** Birth - 47 months
- **Standing Height:** 2+ years
- **Upper Leg Length:** 8+ years
- **Upper Arm Length & Mid-upper Arm Circumference:** 2+ months
- **Waist Circumference:** 2+ years
- **Hip Circumference:** 12+ years

## Protocol & Procedure Highlights
- **Location:** Measurements were collected in the Mobile Examination Center (MEC) by trained health technicians.
- **Arm/Leg Side:** Measurements were taken on the **right** side of the body. If an amputation or medical condition prevented this, the left side was used. 
- **Amputations:** Body weight data is set to "missing" for individuals with limb amputations due to confidentiality/disclosure risks.
- **Pregnancy:** Pregnant women were measured, but if a woman was outside the 20-44 age range (the only range where pregnancy status is publicly disclosed), her body measures data is hidden to prevent disclosure.
- **Clothing:** Technicians documented if excessive clothing or medical appliances interfered with weight measurements via comment codes.

## Data Processing & Analytic Notes
- **Editing:** Extreme values (above the 99th or below the 1st percentile) were reviewed against subject characteristics (age, sex, height, etc.). Unrealistic values were deleted. There is **no imputed data**. 
- **BMI Calculation (`BMXBMI`):** Weight in kilograms divided by height in meters squared, rounded to one decimal place.
- **Children's BMI categories (`BMDBMIC`):** Calculated for ages 2-19 based on CDC growth charts matching age explicitly in months (1 = Underweight, 2 = Normal, 3 = Overweight, 4 = Obese). *Note: child/adolescent weight classification is not directly comparable to adult definitions.*
- **Weights:** Analysts should use the Examination sample weights for analyzing this data.

## Key Variables Overview
*Most physical measurements have a corresponding comment code variable starting with "BMI" (e.g., `BMXWT` has `BMIWT`) used to indicate if the measurement could not be obtained, was affected by clothing, or was not perfectly straight.*

### 1. Survey & Status Identifiers
*   **`SEQN`**: Respondent sequence number.
*   **`BMDSTATS`**: Component Status Code (1 = Complete, 2 = Partial [height/weight only], 3 = Other partial, 4 = No exam data).

### 2. Major Body Measurements
*   **`BMXWT`**: Weight (kg) & **`BMIWT`**: Comment
*   **`BMXHT`**: Standing Height (cm) & **`BMIHT`**: Comment
*   **`BMXRECUM`**: Recumbent Length (cm) & **`BMIRECUM`**: Comment
*   **`BMXHEAD`**: Head Circumference (cm) & **`BMIHEAD`**: Comment

### 3. Derived Indices
*   **`BMXBMI`**: Body Mass Index (kg/m²)
*   **`BMDBMIC`**: BMI Category for Children/Youth (aged 2-19)

### 4. Limb & Trunk Measurements
*   **`BMXLEG`**: Upper Leg Length (cm) & **`BMILEG`**: Comment
*   **`BMXARML`**: Upper Arm Length (cm) & **`BMIARML`**: Comment
*   **`BMXARMC`**: Arm Circumference (cm) & **`BMIARMC`**: Comment
*   **`BMXWAIST`**: Waist Circumference (cm) & **`BMIWAIST`**: Comment
*   **`BMXHIP`**: Hip Circumference (cm) & **`BMIHIP`**: Comment
