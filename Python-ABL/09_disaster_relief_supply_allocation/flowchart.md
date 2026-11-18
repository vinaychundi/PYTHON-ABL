# Flowchart – Case Study 9

The flowchart below is written in Mermaid. GitHub renders the diagram automatically when this Markdown file is opened. A PNG copy is also provided below.

![Flowchart – Case Study 9](./flowchart.png)

## Mermaid source

```mermaid
flowchart TD
 A([Start]) --> B[/Input available stock and area demands/]
 B --> C[Validate area records]
 C --> D[Set priority to 1]
 D --> E[Select areas at current priority]
 E --> F[Allocate minimum of stock and demand]
 F --> G[Calculate unmet demand and update stock]
 G --> H{More areas at this priority?}
 H -- Yes --> F
 H -- No --> I{More priority levels?}
 I -- Yes --> J[Increase priority]
 J --> E
 I -- No --> K[Display allocations and remaining stock]
 K --> L([Stop])
```
