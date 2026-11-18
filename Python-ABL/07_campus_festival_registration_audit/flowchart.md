# Flowchart – Campus Festival Registration and Financial Audit

This flowchart is provided in two viewable forms: the rendered PNG below and the editable Mermaid diagram source.

![Flowchart – Campus Festival Registration and Financial Audit](./flowchart.png)

## Mermaid source

```mermaid
flowchart TD
 A([Start]) --> B[/Input number of registration entries/]
 B --> C[/Input registration ID and payment/]
 C --> D[Normalize ID and store entry]
 D --> E{ID already registered?}
 E -- Yes --> F[Mark duplicate; do not count payment again]
 E -- No --> G[Add ID to unique set and count first payment]
 F --> H{More registrations?}
 G --> H
 H -- Yes --> C
 H -- No --> I[/Input sponsorship and expenses/]
 I --> J[Calculate expected revenue = unique IDs × 300]
 J --> K[Calculate final balance = actual collection + sponsorship - expenses]
 K --> L{Balance positive?}
 L -- Yes --> M[Report SURPLUS]
 L -- No --> N{Balance negative?}
 N -- Yes --> O[Report DEFICIT]
 N -- No --> P[Report BREAK EVEN]
 M --> Q[Display financial audit and duplicate IDs]
 O --> Q
 P --> Q
 Q --> R([Stop])
```
