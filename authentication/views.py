from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ItemForm,CommentForm
from .models import Item,Comment


def home(request):
          return render(request,'home.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/')
            
    return render(request, 'login.html')
                        
def register_page(request):
          if request.method=='POST':
                first_name=request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                username=request.POST.get('username')
                password=request.POST.get('password')

                user=User.objects.filter(username=username)
                if user.exists():
                        messages.info(request,'Username Already Taken!!!')
                        return redirect('/register/')
                user=User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username
                )
                user.set_password(password)
                user.save()
                messages.info(request,'Account Created Successfully')
                return redirect('/register/')
          return render(request,'register.html')


def list(request):
        items=Item.objects.all()
        return render(request,'list.html',{'items':items})

from django.contrib.auth.decorators import login_required

@login_required
def createitem(request):
    if request.method == 'POST':
        print("User:", request.user)
        print("Authenticated:", request.user.is_authenticated)

        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            print("Saving item with user:", item.user)  
            item.save()
            return redirect('/')
        else:
            print("Form errors:", form.errors)
    else:
        form = ItemForm()
    return render(request, 'createitem.html', {'form': form})


@login_required
def update(request,pk):
        item = get_object_or_404(Item, pk=pk)
        if request.method=='POST':
                form=ItemForm(request.POST, instance=item)
                if form.is_valid():
                        form.save()
                        return redirect('/')
        else:
                form=ItemForm(instance=item)
        return render(request,'update.html',{'form':form})

@login_required
def delete(request,pk):
        item=get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('/')

@login_required
def Logout(request):
        logout(request)
        return render(request,'login.html')

@login_required
def profile(request):
        items=Item.objects.filter(user=request.user)  
        comments = Comment.objects.all().order_by('-id') 
        return render(request,'profile.html',{'items':items, 'comments': comments})

@login_required
def addcomment(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.user = request.user  
            comment.save()
            return redirect('/list/')
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form, 'item': item})
