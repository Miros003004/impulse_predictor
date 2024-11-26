from django.shortcuts import render
from django.http import HttpResponse
import pickle
from rdkit.Chem import AllChem, MolFromSmiles

def get_fingerprint(smiles: str) -> list:
    try:
        mol = MolFromSmiles(smiles)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 3, nBits=1024)
        return list(fp)

    except:
        pass

# Create your views here.
with open('model_1.sav', 'rb') as file:
    model = pickle.load(file)

def index(request):
    template_name = 'homepage/index.html'

    url = request.build_absolute_uri()
    if 'value-1' in url:
        composition = request.GET.get('value-1')
        expantion_coeff = request.GET.get('value-2')


        try:
            result = model.predict([get_fingerprint(composition) + [expantion_coeff]])[0]
            result = round(result, 2)
        except:
            result='В Ваших данных ошибка, попробуйте ещё раз.'
    
    else:
        result = '...'

    context = {'result': result}
    
    # return HttpResponse('hello')
    return render(request, template_name, context)