from django.shortcuts import render
from requests import post
from .models import recipe_data
from recipeList.settings import BASE_DIR
# Create your views here.

def index(request):
    recipes = recipe_data.objects.all()
    return render(request, 'index.html', {'recipes':recipes, 'BASE_DIR':BASE_DIR})
 

def admin1(request):
    if request.method == 'POST':
        recipe = recipe_data()
        recipe.recipe_name = request.POST.get("recipe_name", False)
        recipe.recipe_desc = request.POST.get("recipe_desc", False)
        recipe.recipe_photo = request.FILES.get("recipe_photo", False)
        recipe.save()

    return render(request, 'upload.html')