from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Companies


def companies_list(request):
    companies = Companies.objects.all()
    return render(request, "companies/companies_list.html", {"companies": companies})

def company_detail(request, company_id):
    company = get_object_or_404(Companies, id=company_id)
    return render(request, "companies/company_detail.html", {"company": company})