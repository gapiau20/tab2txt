'''
Utils to get the text configuration from diverse file formats
'''
import yaml

def parseYML(filepath:str):
    '''
    returns a dictionary from yaml metadata description in form

    variable name
        iscategorical (0 or 1)
        imp (the value corresponding to nan)
    '''
    with open(filepath, 'r') as f:
        data = yaml.full_load(f)
    return data