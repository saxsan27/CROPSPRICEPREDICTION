from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import Context, RequestContext
import pickle
@ensure_csrf_cookie
def inputs(request):
    return render_to_response('input.html',context_instance=RequestContext(request))
def result(result):
    m=request.POST.get('Crop')
    k=pickle.load(open(m+'.sav','rb'))
    a=request.POST.get('maxtemperature')
    b=request.POST.get('mintemperature')
    c=request.POST.get('DPrice')
    d=request.POST.get('GDP')
    e=request.POST.get('msp')
    if m=='Rice':
        l=k.predict([[request.POST.get('maxtemperature'),request.POST.get('mintemperature'),request.POST.get('DPrice'),d,e,request.POST.get('quantity'),request.POST.get('ExPrice')]])
        res=l
    elif m=='Maize':
        l=k.predict([[request.POST.get('maxtemperature'),request.POST.get('mintemperature'),request.POST.get('DPrice'),d,e,request.POST.get('quantity'),request.POST.get('ExPrice')]])
        res=l
    elif m=='Jowar':
        l=k.predict([[request.POST.get('maxtemperature'),request.POST.get('mintemperature'),request.POST.get('DPrice'),d,e]])
        res=l
    else:
        l=k.predict([[request.POST.get('maxtemperature'),request.POST.get('mintemperature'),request.POST.get('DPrice'),d,e]])
        res=l
    c={'res':res}
    return render_to_response('result.html',c,ontext_instance=RequestContext(request))
        
        
                    
