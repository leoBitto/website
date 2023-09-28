from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Gallery_image, Contact, Opening_hour
from .forms import GalleryImageForm, ContactForm, OpeningHourForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages


# this is the part of the website accessible only to admin
@login_required
def dashboard(request):
    
    # Recupera tutte le istanze dei modelli
    gallery_images = Gallery_image.objects.all()
    contacts = Contact.objects.all()
    opening_hours = Opening_hour.objects.all()

    context = {
        'gallery_images': gallery_images,
        'contacts': contacts,
        'opening_hours': opening_hours,
    }

    return render(request, 'website/dashboard.html', context)


def gallery_page(request):
    gallery_images = Gallery_image.objects.all()
    form = GalleryImageForm()

    context = {
        'gallery_images': gallery_images,
        'form': form,
    }

    return render(request, 'website/gallery_page.html', context)
    

def add_gallery_image(request):
    print(request.POST)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Immagine aggiunta con successo.')
            return redirect('website:gallery_page')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    else:
        form = GalleryImageForm()

    return render(request, 'website/gallery_page.html', {'form': form})


def delete_gallery_image(request, image_id):
    # Trova l'immagine nel database
    image = get_object_or_404(Gallery_image, id=image_id)

    # Elimina l'immagine
    image.delete()
    messages.success(request, 'Immagine eliminata con successo.')
    return redirect('website:dashboard')



def contact_page(request):
    contacts = Contact.objects.all()
    form = ContactForm()
    context = {
        'contacts': contacts,
        'form':form,
    }

    return render(request, 'website/contact_page.html', context)

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contatto aggiunto con successo.')
            return redirect('website:contact_page')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    else:
        form = ContactForm()

    return render(request, 'website/contact_page.html', {'form': form})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Contatto eliminato con successo.')
    return redirect('website:dashboard')



def opening_hours_page(request):
    opening_hours = Opening_hour.objects.all()
    form = OpeningHourForm()
    context = {
        'opening_hours': opening_hours,
        'form':form,
    }

    return render(request, 'website/opening_hours_page.html', context)

def add_opening_hour(request):
    if request.method == 'POST':
        form = OpeningHourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orario aggiunto con successo.')
            return redirect('website:opening_hours_page')
        else:
            messages.error(request, 'Si è verificato un errore. Si prega di correggere il modulo.')
    else:
        form = OpeningHourForm()

    return render(request, 'website/opening_hours_page.html', {'form': form})

def delete_opening_hour(request, opening_hour_id):
    hours = get_object_or_404(Opening_hour, pk=opening_hour_id)
    hours.delete()
    messages.success(request, 'Orario eliminato con successo.')
    return redirect('website:dashboard')



# this is part of the website accessible to everyone
def base(request):
    
    context = {}

    return render(request, 'website/landing.html', context)