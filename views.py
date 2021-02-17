
def getbranch(data, obj):
    leaves = []
    if 'branches' in data:
        for branch in data['branches']:
            internal_leaves = []
            if 'branches' in branch:
                for ibranch in branch:
                    getbranch(ibranch)

            if 'leaves' in branch:
                for leave in branch['leaves']:
                    internal_leaves.append(leave)
            res_all[branch['id']] = internal_leaves
            leaves.extend(internal_leaves)
    else:
        if 'leaves' in data:
            for leave in data['leaves']:
                leaves.append(leave)

    res_all[data['id']] = leaves
    res_all[obj['id']] = leaves

    return leaves



def assignment(request):
    data = [
        {
            "id": "1",
            "name": "node1",
            "branches": [
                {
                    "id": "2",
                    "name": "node2",
                    "branches": [
                        {
                            "id": "3",
                            "name": "node3",
                            "leaves": [
                                "leaf1",
                                "leaf2"
                            ]
                        }, {
                            "id": "4",
                            "name": "node4",
                            "leaves": [
                                "leaf3",
                                "leaf4"
                            ]
                        }
                    ]
                }
            ]
        }, {
            "id": "5",
            "name": "node5",
            "branches": [
                {
                    "id": "6",
                    "name": "node6",
                    "leaves": [
                        "leaf5"
                    ]
                }
            ]
        }
    ]
    data_result = []

    for obj in data:
        if 'branches' in obj:

            for branch in obj['branches']:
                result = getbranch(branch, obj)
                data_result.extend(result)


    resultobj = {
        'result': data_result,
        'global' : res_all,
    }
    return JsonResponse(resultobj, safe=False, status=200)
