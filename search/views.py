from django.shortcuts import render
from .models import Restaurant
from .forms import SearchForm
import json
# Create your views here.


# def search_view(request):
#     form = SearchForm()
#     query = request.GET.get('query')
#     results = []
#     if query:
#         results = Restaurant.objects.filter(name__icontains=query)
#     return render(request, 'search/search_results.html', {'form': form, 'results': results, 'query': query})


def home_view(request):
    random_items = Restaurant.objects.order_by('?')[:5]  # Get 5 random items
    # print(Restaurant.objects.items)
    return render(request, 'search/home.html', {'random_items': random_items})


def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Restaurant.objects.filter(items__icontains=query)
        cleaned_items = []
        for result in results:
            item_dict = json.loads(result.items)
            for item, price in item_dict.items():
                if query.lower() in item.lower():
                    cleaned_items.append({
                        'item': item,
                        'price': price.strip(),
                        'location': result.location,
                        'restaurant_name': result.name,
                    })
        for item_data in cleaned_items:
            print(f"Item: {item_data['item']}, Price: {item_data['price']}, Location: {item_data['location']}, Restaurant: {item_data['restaurant_name']}")
    else:
        query = ''
        results = []
        cleaned_items = []
    return render(request, 'search/search_results.html', {'form': form, 'results': results, 'query': query, 'cleaned_items': cleaned_items})
