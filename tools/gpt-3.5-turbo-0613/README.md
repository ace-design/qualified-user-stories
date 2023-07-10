# Tool Description: GPT-3.5

- URL: [https://github.com/ace-design/gpt-stories/blob/v1.0/README.md](https://github.com/ace-design/gpt-stories/blob/v1.0/README.md)

## Dependencies

- python >= 3.11
- openai = 0.27.8
- timeout-decorator = 0.5.0

## Integration Protocol

Run the tool as described on its webpage. 
It produces one file per user stories, in a specific JSON format.
To transform this format into our unified one, run the `convert.py` script.


## Example

Consider the following story, stored in a file named `input.txt`:

> As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.

We can run the tool on the backlog, producing the following output:

```json
{
  "story": "As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.\n",
  "extraction": {
    "personas": [ "UI designer" ],
    "entities": [ "user testing", "stakeholder UI improvement requests" ],
    "actions":  [ "begin", "validate" ],
    "benefit":  "I can validate stakeholder UI improvement requests"
  },
  "categories": {
    "primary_entities":   [ "user testing" ],
    "secondary_entities": [ "stakeholder UI improvement requests" ],
    "primary_actions":    [ "begin" ],
    "secondary_actions":  [ "validate" ]
  },
  "relations": {
    "relations": [
      { "from": "UI designer", "to": "begin",        "kind": "triggers" },
      { "from": "begin",       "to": "user testing", "kind": "targets" }
    ]
  },
  "cost": {
    "input": 1301,
    "output": 174,
    "time (ns)": 4516597000
  }
}
```

Then, the conversion script normalize the output:

```json
{
    "Text": "#G02# As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.",
    "Persona": [ "UI designer" ],
    "Action": {
        "Primary Action":   [ "begin" ],
        "Secondary Action": [ "validate" ]
    },
    "Entity": {
        "Primary Entity":   [ "user testing" ],
        "Secondary Entity": [ "stakeholder UI improvement requests" ]
    },
    "Benefit": "I can validate stakeholder UI improvement requests",
    "Triggers": [ [ "UI designer", "begin" ] ],
    "Targets":  [ [ "begin", "user testing"] ]
}
```
