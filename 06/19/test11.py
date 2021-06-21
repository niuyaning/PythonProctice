#在函数中修改列表
def print_models(unprinted_designs,complate_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"{current_design}")
        complate_models.append(current_design)

def show_complated_models(complate_models):
    for complate_model in complate_models:
        print(complate_model)

unprinted_designs = ['phone case','robot pendant','dode']
complate_models = []

print_models(unprinted_designs,complate_models)
show_complated_models(complate_models)
