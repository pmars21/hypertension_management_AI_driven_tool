# Dataset Summary: NHANES Physical Activity (PAQ_L)

## General Information
- **Survey Name:** National Health and Nutrition Examination Survey (NHANES)
- **Data Cycle:** August 2021 - August 2023
- **Component:** Physical Activity
- **Data File:** `PAQ_L.xpt`
- **First Published:** September 2024
- **Target Population:** Participants aged 18 years and older.

## Protocol Highlights
- **Administration:** Questionnaire administered in-home or by telephone using the Computer-Assisted Personal Interview (CAPI) system.
- **Language & Proxy:** Conducted in English or Spanish (interpreters available). A proxy was allowed if the participant could not answer for themselves.
- **Scope:** The questionnaire focuses on two main intensity levels of leisure-time physical activity (LTPA) — Moderate and Vigorous — as well as sedentary behaviors.

## Data Processing & Analytic Notes
- **Outliers:** Individuals reporting an average of 24 hours or more per day of activity had their data set to "missing." The dataset may still contain very high activity values, and analysts are encouraged to carefully inspect data for plausibility.
- **Sedentary Behavior Trend Changes (`PAD680`):** In the 2011-2012 cycle, an additional probe was added to the sedentary behavior question to query times less than 8 hours. Analysts comparing historical survey cycles should account for this methodological shift.
- **Sample Weights:** 
  - If analyzing the PAQ data alone, use the **Interview sample weights**. 
  - If merging PAQ data with any examination data from the Mobile Examination Center (MEC), use the **MEC sample weights**.

## Key Variables Overview

### 1. Identifiers
*   **`SEQN`**: Respondent sequence number.

### 2. Moderate Leisure-Time Physical Activity (LTPA)
*Causes moderate increases in breathing or heart rate.*
*   **`PAD790Q`**: Frequency of moderate LTPA (number of times).
*   **`PAD790U`**: Unit for the moderate LTPA frequency (D = Day, W = Week, M = Month, Y = Year).
*   **`PAD800`**: Duration in minutes of each moderate LTPA session (maximum allowed record is < 24 hours).

### 3. Vigorous Leisure-Time Physical Activity (LTPA)
*Causes large increases in breathing or heart rate.*
*   **`PAD810Q`**: Frequency of vigorous LTPA (number of times).
*   **`PAD810U`**: Unit for the vigorous LTPA frequency (D = Day, W = Week, M = Month, Y = Year).
*   **`PAD820`**: Duration in minutes of each vigorous LTPA session (maximum allowed record is < 24 hours).

### 4. Sedentary Activity
*   **`PAD680`**: Minutes spent sitting/sedentary on a typical day (e.g., at a desk, traveling, reading, watching TV). This measure strictly **excludes** time spent sleeping.
