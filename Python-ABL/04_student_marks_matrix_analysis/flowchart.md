# Flowchart – Student Marks Matrix Analysis

The flowchart below is written in Mermaid. GitHub renders the diagram automatically when this Markdown file is opened. A PNG copy is also provided below.

![Flowchart – Student Marks Matrix Analysis](./flowchart.png)

## Mermaid source

```mermaid
flowchart TD
 A([Start]) --> B[/Input number of students and subjects/]
 B --> C[/Input subject names and student names/]
 C --> D[Build marks matrix and validate each mark]
 D --> E[Calculate each student's total and average]
 E --> F{At least one student?}
 F -- Yes --> G[Find and display top performer]
 F -- No --> H[Skip top performer calculation]
 G --> I[Calculate subject averages]
 H --> I
 I --> J{More subjects?}
 J -- Yes --> K[Display subject average]
 K --> L{Average below 50?}
 L -- Yes --> M[Flag low-average subject]
 L -- No --> N[Continue]
 M --> O{More subjects?}
 N --> O
 O -- Yes --> I
 O -- No --> P[Display student and subject analysis]
 P --> Q([Stop])
```
