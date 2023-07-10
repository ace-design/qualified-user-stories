'''
ChatGPT saves each story annotation  in a JSON format that does not match with the other 
NLP tools. This script will extract all information from a chatgpt dataset folder and merge 
each story annotation into one JSON file with the correct formating. 
'''

import argparse
import os
import json

def main():
    folderPath, savingName = command()
    dataset, stories = extractData(folderPath)
    saveResults(dataset, stories, savingName)
def command():
    '''
    gets info from the commandline input

    Returns:
    args.folder_path (str): path to the directory with all the story annotations
    args.saving_name (str): the name of the JSON file to save the results 

    Raises:
        directory does not exists: raises exception
    '''
    parser = argparse.ArgumentParser(description = "This program will structure ChatGPT to the generalized JSON format")
    parser.add_argument("folder_path", type = str, help = "folder path to all the annotations")
    parser.add_argument("saving_name", type = str, help = "name to save the JSON file")
    
    args = parser.parse_args()

    if (not os.path.isdir(args.folder_path)):
        print ("Directory does not exists")
        raise 
    else:
        return args.folder_path, args.saving_name

def extractData(folderPath):
    '''
    Extracts the data from all the files in the folder path and saves into a dictionary

    Parameters: 
    folderPath (str): the path to the folder with all the ChatGPT story annotations for a dataset

    Returns:
    dataset (dict): annotations of each story by ChatGPT
    '''
    folder = os.listdir(folderPath)
    dataset = []
    stories = []

    for fileName in folder:
        file = open(folderPath + "\\" + fileName)
        data = json.load(file) 

        #Collect the data
        extractedData = {}
        story = data["story"].strip(" \t\n")
        story = story.replace('\\\'', "\'")
        story = story.replace('\\\"', "\"")
        extractedData["Text"] = story
        stories.append(story)
        extractedData["Persona"] = data["extraction"]["personas"]
        extractedData["Action"] = {} 
        extractedData["Action"]["Primary Action"] = data["categories"]["primary_actions"]
        extractedData["Action"]["Secondary Action"] = data["categories"]["secondary_actions"]  
        extractedData["Entity"] = {}
        extractedData["Entity"]["Primary Entity"] = data["categories"]["primary_entities"]
        extractedData["Entity"]["Secondary Entity"] = data["categories"]["secondary_entities"] 
        extractedData["Benefit"] = data["extraction"]["benefit"]
        extractedData["Triggers"] = []
        extractedData["Targets"] = []
        for relationInfo in data["relations"]["relations"]:
            if "kind" in relationInfo:
                relationType = relationInfo["kind"]
                relationStart = relationInfo["from"]
                relationEnd = relationInfo["to"]
                relation = [relationStart, relationEnd]
                if relationType == "triggers":
                    extractedData["Triggers"].append(relation)
                elif relationType == "targets":
                    extractedData["Targets"].append(relation)

        dataset.append(extractedData)

    return dataset, stories

def saveResults(dataset, stories, savingName):
    '''
    Saves the data extractions into a file 

    Parameters: 
    dataset (dict): annotations of each story by ChatGPT
    stories (list): all the stories that ChatGPT annotated
    savingName (str): the name of the file to save the dataset
    '''
    
    json.dumps(dataset)
    resultsSavingPath = "nlp\\nlp_outputs\\individual_backlog\\nlp_outputs_original\\chatgpt\\" + savingName + ".json"
    with open(resultsSavingPath,"w", encoding="utf-8") as file:
        json.dump(dataset, file, ensure_ascii=False, indent = 4) 

    storiesSavingPath = "inputs\individual_backlog\chatgpt_stories\\" + savingName + ".txt"
    file = open(storiesSavingPath, "w", encoding="utf-8")
    for story in stories:
        file.writelines(story + "\n")

if __name__ == "__main__":
    main()  