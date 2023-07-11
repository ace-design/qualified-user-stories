# Extracting Domain Models from User Stories

## General Information

- Authors:
  - [Sathurshan Arulmohan](arulmohs@mcmaster.ca), McMaster University & McSCert
  - Dr. [Marie-Jean Meurs](meurs.marie-jean@uqam.ca), Université du Québec à Montréal (UQAM) & CIRST
  - Dr. [Sébastien Mosser](mossers@mcmaster.ca), McMaster University & McSCert
- Version: 1.0 (July 2023)

## Content of the repository

- `_raw`:
  - `dalpiaz2018` contains the initial user stories text file from [Dalpiaz et al](https://data.mendeley.com/datasets/7zbk8zsd8y/1).
  - `docanno` contains the raw exportation of the annotated dataset, using Docanno's internal format (JSONL).
- `ground_truth`:
  - Each `json` file represents the associated anotated backlog, annotated by the 1st and 3rd authors.
- `tools`:
  - `visual_narrator`: Concepts extracted using [Visual Narrator](https://github.com/MarcelRobeer/VisualNarrator).
  - `gpt-3.5-turbo-0613`: Concepts extracted using [GPT-3.5](https://platform.openai.com/docs/guides/gpt), between June 22 and June 24 (2023).
  - `crf`: concepts extracted using a tailored Conditional Random Fields approach.

## File Format

### Description 

```json
{
  "PID": "backlog identifier",
  "Text": "original text",
  "Persona": [ "..." ],
  "Action": {
    "Primary Action":   [ "...", ... ],
    "Secondary Action": ["...", ...] 
  },
  "Entity": { 
    "Primary Entity":   [ "...", ... ], 
    "Secondary Entity": [ "...", ...] 
  },
  "Benefit": "...",
  "Triggers": [ [ "Persona", "Action" ], ... ],
  "Targets":  [ [ "Action", "Entity" ],  ... ],
  "Contains": [ [ "Entity", "Entity" ],  ... ]
}
```

### Example

```json
{
    "PID": "#G02#",
    "Text": "#G02# As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.",
    "Persona": ["UI designer"],
    "Action": {
        "Primary Action": ["begin"],
        "Secondary Action": ["validate"]
    },
    "Entity": {
        "Primary Entity": ["user testing"],
        "Secondary Entity": ["stakeholder UI improvement requests"]
    },
    "Benefit": "I can validate stakeholder UI improvement requests",
    "Triggers": [ ["UI designer", "begin"] ],
    "Targets": [
        ["begin", "user testing"],
        ["validate", "stakeholder UI improvement requests"]
    ],
    "Contains": []
}
```

## Publications using this repository:

### Published
1. _Modelling Agile Backlogs as Composable Artefacts to support Developers and Product Owners_. Sébastien Mosser, Vladimir Reihnarz, and Corinne Pulgar. Journal of Object Technology, 2022. ([www](https://archipel.uqam.ca/15421/1/ECMFA_2022_paper_3.pdf))

### Submitted

1. _Extracting Domain Models from Textual Requirements in the Era of Large Language Models_. Sathurshan Arulmohan, Marie-Jean Meurs, and Sébastien Mosser. _Submitted to the 5th Workshop on Artificial Intelligence and Model-driven Engineering, co-located with MODELS'2023_.