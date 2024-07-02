from django.shortcuts import render

#journal list

def journal_list(request):
    return render(request, "journal/journal_list.html")

