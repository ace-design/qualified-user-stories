# Tool Description: GPT-3.5 extractor

- URL: [https://github.com/MarcelRobeer/VisualNarrator](https://github.com/MarcelRobeer/VisualNarrator)

## Dependencies

- Python >= 3.6 
- spaCy >= 2.1.2 
  - language model: `en_core_web_md`
- NumPy >= 1.16.2
- Pandas >= 0.24.2
- Jinja2 >= 2.10

## Integration Protocol

To ensure reproducibility and avoid python version/dependency hell, we wrapped Visual Narrator into a turn-key docker image: [https://hub.docker.com/r/acedesign/visualnarrator](https://hub.docker.com/r/acedesign/visualnarrator)

```
$ docker run --rm acedesign/visualnarrator -h
```

**Note**: Apple M1/M2 chips require an additional argument: `--platform linux/amd64`

As a consequence, we considered the tool as a blackbox. 
Instead of interfacing with its python API, we ran the tool as an external command (`python run.py -u`), and captured its output. We then parsed the result and store it in our common JSON file format.

## Example

Consider the following story, stored in a file named `input.txt`:

> As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.

We can run Visual Narrator through the docker image as follow (the `output` prefix is used to mount the host file system in the docker container, read input files and produce outputs):

```
docker run --rm -v `pwd`:/usr/src/app/output acedesign/visualnarrator -u output/test.txt
```

Running the command produce the following result:

```txt
<---------- BEGIN U S ---------->
User Story 1 : As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.

 >> INDICATORS
  Role: As a 
    Means: I want to 
    Ends: So that
 >> ROLE
  Functional role: designer ( w/ compound ['UI', 'designer'] )
 >> MEANS
  Main verb: begin  
  Main object: System ( w/ noun phrase [] w/ compound [] )
  Free form: ['can', 'user', 'testing']
    Verbs: ['I']
      Phrasal: [([], '')]
    Nouns: ['user'] 
  Free form: ['I', 'can', 'validate', 'stakeholder', 'UI', 'improvement', 'requests']
    Verbs: ['UI']
      Phrasal: [([], '')]
    Compound nouns: [[improvement, requests]]
    Nouns: ['stakeholder', 'UI', 'improvement', 'requests']  ( Proper: ['UI'])
<----------  END U S  ---------->
```

One can parse the resulting data to create the following JSON:

```json
{
  "Text": "#G02# As a UI designer, I want to begin user testing, so that I can validate stakeholder UI improvement requests.",
  "Persona":  [ "UI designer" ], 
  "Action":   [ "begin" ],
  "Entity":   [ "testing" ],
  "Triggers": [ "UI designer", "begin" ],
  "Targets":  [ "begin", "testing" ]
}
```

This representation can then easily be converted to the unified data format described on the top-level Readme file (actions and entities being primary ones).

