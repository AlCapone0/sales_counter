from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Companies, RSPORTcouter


def companies_list(request):
    companies = Companies.objects.all()
    return render(request, "companies/companies_list.html", {"companies": companies})

def company_detail(request, company_id):
    company = get_object_or_404(Companies, id=company_id)
    result = RSPORTcouter.objects.values()  # return ValuesQuerySet object
    comport = [entry for entry in result] # converts ValuesQuerySet into Python list

    return render(request, "companies/company_detail.html", {"company": company, "comport": comport})

#def result_filter(request, pk):
 #   result = RSPORTcouter.objects.values()
  #      if pk == 1:
   #     pass
  #  return render(request, "companies/company_detail.html", {"company": company, "comport": comport})