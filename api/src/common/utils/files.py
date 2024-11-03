import os

def list_files(path):
    if not os.path.exists(path):
        return []
    
    if os.path.isfile(path):
        return [os.path.realpath(path)]
    
    files = []
    
    for file in os.listdir(path):
        dir_files = list_files(os.path.join(path, file))
        files.extend(dir_files)
        
    return files
        
        

