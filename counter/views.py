from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Companies, RSPORTcouter


def companies_list(request):
    companies = Companies.objects.all()
    return render(request, "companies/companies_list.html", {"companies": companies})

def company_detail(request, company_id):
    company = get_object_or_404(Companies, id=company_id)

    result = RSPORTcouter.objects.values()  # return ValuesQuerySet object
    comport = [entry for entry in result]  # converts ValuesQuerySet into Python list
    #return list_result
   # comport = list_result

    return render(request, "companies/company_detail.html", {"company": company, "comport": comport})