import paralleldots

paralleldots.set_api_key('xh38DdxTrAVfjsAbK290ANbjqS9BGkDAmtBEBQDrQE8')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
