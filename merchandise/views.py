from django.shortcuts import render,HttpResponse
from .models import Product, Video, GamingProduct
import math

# Create your views here.
def homepage(request):
    shop_prod = Product.objects.all()[:4]
    vid = Video.objects.all()[:3]
    prods={"shop_prod":shop_prod,"vid":vid}
    return render(request,'home.html',prods)

def shoppage(request):
    shop_prod = Product.objects.all()
    # print(shop_prod[0].prod_cost,"        hello")
    products={'shop_prod':shop_prod}
    return render(request,'shop.html',products)

def videopage(request):
    vid = Video.objects.all()
    # print(vid[0].Vid_title)
    vids={'Vids':vid,'containers':range(0,math.ceil(len(vid)/4))}
    return render(request,'videos.html',vids)


def gamingsetuppage(request):
    gprods = GamingProduct.objects.all()
    allprod=[]
    for gprod in gprods:
        prod=[]
        
        store=gprod.gprod_store.split(",")
        link=gprod.gprod_link.split(",")
        for i in range(0,len(store)):
            dictionary={}
            dictionary["store"]=store[i]
            dictionary["link"]=link[i]
            prod.append(dictionary)
        # print(prod)
        allprod.append([gprod,prod])
    gproduct={'Gprods':allprod}
    return render(request,'gamingsetup.html',gproduct)

def customPcBuild(request):
    gprods = GamingProduct.objects.all()
    allprod=[]
    for gprod in gprods:
        prod=[]
        
        store=gprod.gprod_store.split(",")
        link=gprod.gprod_link.split(",")
        for i in range(0,len(store)):
            dictionary={}
            dictionary["store"]=store[i]
            dictionary["link"]=link[i]
            prod.append(dictionary)
        # print(prod)
        allprod.append([gprod,prod])
    gproduct={'Gprods':allprod}
    return render(request,'customPcBuild.html',gproduct)

def racingSimulator(request):
    gprods = GamingProduct.objects.all()
    allprod=[]
    for gprod in gprods:
        prod=[]
        
        store=gprod.gprod_store.split(",")
        link=gprod.gprod_link.split(",")
        for i in range(0,len(store)):
            dictionary={}
            dictionary["store"]=store[i]
            dictionary["link"]=link[i]
            prod.append(dictionary)
        # print(prod)
        allprod.append([gprod,prod])
    gproduct={'Gprods':allprod}
    return render(request,'racingSimulator.html',gproduct)

def accessories(request):
    gprods = GamingProduct.objects.all()
    allprod=[]
    for gprod in gprods:
        prod=[]
        
        store=gprod.gprod_store.split(",")
        link=gprod.gprod_link.split(",")
        for i in range(0,len(store)):
            dictionary={}
            dictionary["store"]=store[i]
            dictionary["link"]=link[i]
            prod.append(dictionary)
        # print(prod)
        allprod.append([gprod,prod])
    gproduct={'Gprods':allprod}
    return render(request,'accessories.html',gproduct)



    