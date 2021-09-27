####################################################
#
# Description: Automatic filter queries
#              generation for cecm.usp.br
# Depencencies: unidecode, json, os
# Author: Rafael Badain @ University of São Paulo
#
####################################################

# imports
import os
import json
import unidecode

# search queries
focus_queries = {'concentracoes': []}
specialization_queries = {'especializacoes': []}
# search results
focus_results = {}
specialization_results = {}

# iterates through every scholar .json and catalogs respectives 'focus' and 'specialization'
for cohord in os.listdir("./estudantes"):
    for file in os.listdir(f"./estudantes/{cohord}"):
        if file.endswith(".json") and cohord not in file:
            #print(cohord, file)
            with open(f'./estudantes/{cohord}/{file}', encoding='utf-8') as scholar:
                scholar_dict = json.load(scholar)
                
                if 'concentracao' in scholar_dict:
                    # merge unique query values
                    focus_queries['concentracoes'] = list(set(focus_queries['concentracoes'] + scholar_dict['concentracao']))
                    # groups name results
                    for focus in scholar_dict['concentracao']:
                        if focus not in focus_results: 
                            focus_results[focus] = { scholar_dict['turma']: [ scholar_dict['nome'] ] }
                        elif scholar_dict['turma'] not in focus_results[focus]:
                            focus_results[focus][scholar_dict['turma']] = [ scholar_dict['nome'] ]
                        elif scholar_dict['nome'] not in focus_results[focus][scholar_dict['turma']]:
                            focus_results[focus][scholar_dict['turma']].append(scholar_dict['nome'])

                if 'especializacao' in scholar_dict:
                    # merge unique query values
                    specialization_queries['especializacoes'] = list(set(specialization_queries['especializacoes'] + scholar_dict['especializacao']))
                    # groups name results
                    for specialization in scholar_dict['especializacao']:
                        if specialization not in specialization_results: 
                            specialization_results[specialization] = { scholar_dict['turma']: [ scholar_dict['nome'] ] }
                        elif scholar_dict['turma'] not in specialization_results[specialization]:
                            specialization_results[specialization][scholar_dict['turma']] = [ scholar_dict['nome'] ]
                        elif scholar_dict['nome'] not in specialization_results[specialization][scholar_dict['turma']]:
                            specialization_results[specialization][scholar_dict['turma']].append(scholar_dict['nome'])

# saves to file
focus_queries['concentracoes'].sort()
specialization_queries['especializacoes'].sort()

with open('./filtros/concentracao/concentracao.json', mode="w", encoding="utf-8") as focus_out:
    json.dump(focus_queries, focus_out)

for focus in focus_results:
    with open(f'./filtros/concentracao/results/{unidecode.unidecode(focus.replace(" ", "-").lower())}.json', mode="w", encoding="utf-8") as results:
        json.dump(focus_results[focus], results)

with open('./filtros/especializacao/especializacao.json', mode="w", encoding="utf-8") as specialization_out:
    json.dump(specialization_queries, specialization_out)

for specialization in specialization_results:
    with open(f'./filtros/especializacao/results/{unidecode.unidecode(specialization.replace(" ", "-").lower())}.json', mode="w", encoding="utf-8") as results:
        json.dump(specialization_results[specialization], results)

