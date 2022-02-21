def validateParams(requestdata, checkdetail):
    output_obj = {}
    for i in checkdetail:
        output_obj[i] = requestdata.get(i)

    return output_obj