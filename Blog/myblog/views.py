from django.shortcuts import render
# from .forms import MyForm
from .models import Flipkart
from django.db import connection
import requests
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import csv , datetime
from django.template import RequestContext
# from datetime import date
# Create your views here.

def website(request):
    print("d")
    return render(request , 'index.html')

def my_custom(request):
    data_info = ""
    data1 = ""
    # date = datetime.now
    if request.method == 'POST':
        date_info = request.POST.get('data_date')
        print(data_info)
        data1 = Flipkart.objects.all().filter(date__contains = date_info)
        print(data1)
    context = {
        'data1' : data1
        }
    
    fields = ['MRP', 'Selling_Price', 'Brand', 'Title', 'Type', 'Model_Name', 'Date', 'Product_URL']
    with open('eureka_forbes.csv','w+') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        print("fields created")
        for i in data1:
            csvwriter.writerow(i)
    print(data1)
    with open('eureka_forbes.csv' , 'rb') as myfile:
        response = HttpResponse(myfile.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=eureka_forbes.csv'
    return render_to_response("index1.html", context)

    # fields = ['MRP', 'Selling_Price', 'Brand', 'Title', 'Type', 'Model_Name', 'Date', 'Product_URL']
    # with open('eureka_forbes.csv','w+') as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow(fields)
    #     print("fields created")
    #     for i in data1:
    #         csvwriter.writerow(i)
    # print(data1)
    # print("uu")
    # with open('eureka_forbes.csv' , 'rb') as myfile:
    #     response = HttpResponse(myfile.read(), content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename=eureka_forbes.csv'
    # return response



# def my_custom(request):
#     # if request.method == 'POST':
#     #     form = MyForm(request.POST)
#     #     if form.is_valid():
#     #     #     print('form is valid')
#     #     #     print(form.cleaned_data)     
            
#     #         date = form.cleaned_data.get('date')
#     #         year = date.year
#     #         month = format(date, 'm')
#     #         day = format(date, 'd')
#     # context = RequestContext(request)
#     posts = []
#     # form = MyForm()
#     with connection.cursor() as cursor:
#         if request.method == 'POST':
#             form = MyForm(request.POST)
#             if form.is_valid():            
#                 date = form.cleaned_data.get('date')
#                 year = date.year
#                 month = format(date, 'm')
#                 day = format(date, 'd')
#                 cursor.execute("select * FROM Flipkart where Date ="+day+"/"+month+"/"+year)
#                 all_posts = cursor.fetchall()
#                 for obj in cursor.fetchall():
#                     posts.append({"title": obj[0], "name": obj[1]})
        
#             context = {
#                 'all_posts':all_posts
#             }

#     # fields = ['MRP', 'Selling_Price', 'Brand', 'Title', 'Type', 'Model_Name', 'Date', 'Product_URL']
#     # with open('eureka_forbes.csv','w+') as csvfile:
#     #     csvwriter = csv.writer(csvfile)
#     #     csvwriter.writerow(fields)
#     #     print("fields created")
#     #     for i in all_posts:
#     #         csvwriter.writerow(i)
#     # print(all_posts)
#     # print("uu")
#     # if request.method == 'POST':
#     #     with open('eureka_forbes.csv' , 'rb') as myfile:
#     #         response = HttpResponse(myfile.read(), content_type='text/csv')
#     #         response['Content-Disposition'] = 'attachment; filename=eureka_forbes.csv'
#             # return response

#         # return redirect('myblog/my_custom/')
#     return render(request , 'index1.html' , context)
    
# # def my_data(request):
# #     if request.method == 'POST':
# #         with open('eureka_forbes.csv' , 'rb') as myfile:
# #         response = HttpResponse(myfile.read(), content_type='text/csv')
# #         response['Content-Disposition'] = 'attachment; filename=eureka_forbes.csv'
# #         return response

# #     return redirect('myblog/my_custom/')