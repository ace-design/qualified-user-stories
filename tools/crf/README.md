# Tool Description: CRF

- URL: [https://github.com/ace-design/nlp-stories/tree/main/nlp/nlp_tools/crf](https://github.com/ace-design/nlp-stories/tree/main/nlp/nlp_tools/crf)

## Dependencies

- python >= 3.10
- pytest = "*"
- jsonlines = "*"
- seaborn = "*"
- pandas = "*"
- stanza = "*"
- pip = "*"
- install = "*"
- ace-sklearn-crfsuite = "*"

## Integration Protocol

Run the tool as described on its webpage. 


## Training/Testing

We used a 80/20 partition to cut the dataset into traning and validation datasets. As such, the results in this directory does not include the stories used for training.

Backlog G16 was also ommited, as when intersected with the other tools outputs it does not contain enough data to support a 80/20 partition.

