import os
entries = os.listdir(os.getcwd())
for entry in entries:
    if (not entry == "saved.txt") and  not (entry == "NameFinder.py") :
        with open(entry,'r',encoding="utf-8") as file:
            
        
            
            contents = file.readlines()
            search_word = ""             # Inserisci la stringa da ricercare

            for line in contents:
                if search_word in line:
                    with open("saved.txt",'a',encoding="utf-8") as filesave:
                        filesave.write(line+ "--- ")

       