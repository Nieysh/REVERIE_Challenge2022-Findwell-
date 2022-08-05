import json

ours_file = '../datasets/REVERIE/exprs_map/finetune/dagger-vitbase-seed.0/preds/submit_test_dynamic.json'

with open(ours_file) as f:
    ours = json.load(f)

ours_new = []

for item in ours:
    new_item = {}
    new_item["instr_id"] = item["instr_id"]
    if item["pred_objid"] != None:
        new_item["predObjId"] = int(item["pred_objid"])
    else:
        new_item["predObjId"] = -1
    path_list = sum(item["trajectory"],[])
    path_new_list = []
    for vp in path_list:
        path_new_list.append([vp])
    new_item["trajectory"] = path_new_list
    print(path_new_list)
    ours_new.append(new_item)

json.dump(ours_new,open("../datasets/REVERIE/exprs_map/finetune/dagger-vitbase-seed.0/preds/submit_test.json", 'w'), indent=4)


