import json
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from myapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword
from django.shortcuts import render, redirect
from myapp.models import User, Destinations, Holidayreserve
from myapp.forms import DestinationForm, Holidayreserveform, ContactForm


# Create your views here.
def login(request):
    return render(request, 'login.html')


def landingpage(request):
        return render(request, 'landingpage.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def rsv1(request):
    return render(request, 'reservation1.html')


def rsv2(request):
    return render(request, 'reservation2.html')


def rsv3(request):
    return render(request, 'reservation3.html')


# nyd to mean new year details
def nyd(request):
    return render(request, 'newyeardeals.html')


def success(request):
    return render(request, 'success.html')


# vln to mean valentine details
def vln(request):
    return render(request, 'valentinedeals.html')


def est(request):
    return render(request, 'easterdeals.html')


def lbd(request):
    return render(request, 'labordeals.html')


def mad(request):
    return render(request, 'madarakadeals.html')


def hud(request):
    return render(request, 'hudumadaydeals.html')


def jam(request):
    return render(request, 'Jamhuri.html')


def mash(request):
    return render(request, 'mashujaa.html')


def xmas(request):
    return render(request, 'christmas.html')


# hdl to mean holiday details
# holiday-detailsmhk to mean holiday-details of mountain hike category
# holiday-detailssb to mean holiday-details of sandy beaches category
# holiday-detailswld to mean holiday-details of wild category
def hdl1(request):
    return render(request, 'holiday-detailsmhk1.html')


def hdl2(request):
    return render(request, 'holiday-detailsmhk2.html')


def hdl3(request):
    return render(request, 'holiday-detailsmhk3.html')


def hdl4(request):
    return render(request, 'holiday-detailssb1.html')


def hdl5(request):
    return render(request, 'holiday-detailssb2.html')


def hdl6(request):
    return render(request, 'holiday-detailssb3.html')


def hdl7(request):
    return render(request, 'holiday-detailswld1.html')


def hdl8(request):
    return render(request, 'holiday-detailswld2.html')


def hdl9(request):
    return render(request, 'holiday-detailswld3.html')


def book(request):
    return render(request, 'Reservation.html')


def kesafaris(request):
    return render(request, 'Kenyasafaris.html')


def tzsafaris(request):
    return render(request, 'Tzsafaris.html')


def Ugsafaris(request):
    return render(request, 'Ugsafaris.html')


def Rwsafaris(request):
    return render(request, 'Rwandasafaris.html')


# def pay(request):
#     return render(request, 'pay.html')
#
# def success(request, booking_id):
#     booking = Holidayreserve.objects.get(pk=booking_id)
#     return render(request, 'success.html')


def proposal(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/proposal')
    else:
        form = DestinationForm()
        return render(request, 'proposals.html', {'form': form})


def delete(request, id):
    destination = Destinations.objects.get(id=id)
    destination.delete()
    return redirect('/show')


def edit(request, id):
    destination = Destinations.objects.get(id=id)
    return render(request, 'edit.html', {'destination': destination})


def show(request):
    destinations = Destinations.objects.all()
    return render(request, 'show.html', {'destinations': destinations})


def token(request):
    consumer_key = 'yW35kAbwReh5gtEsfdFpoJ9erzlznpCe'
    consumer_secret = '2eLxwvqPTaA9mNNM'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Wunderkind Co.",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)


def payment_page(request):
    if request.method == 'POST':
        form = Holidayreserveform(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.total_amount = booking.calculate_total_amount()
            booking.save()
            return render(request, 'paymentpage.html', {'booking': booking})
        else:
            form = Holidayreserveform()

        return render(request, 'holiday-detailsmhk1.html', {'form': form})


def holiday_reserve(request):
    if request.method == 'POST':
        form = Holidayreserveform(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('success')
        else:
            form = Holidayreserveform()

        return render(request, 'holiday-detailsmhk1.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

<<<<<<< HEAD
=======
# def like_image(request, image_id):
#     image = get_object_or_404(Image, pk=image_id)
#     if request.user in image.likes.all():
#         image.likes.remove(request.user)
#     else:
#         image.likes.add(request.user)
#     return redirect('image_detail', image_id=image.id)

>>>>>>> 6fc92ba (My Bootcamp-SP project)
#
# def translate_view(request):
#     if request.method == 'POST':
#         text_to_translate =
<<<<<<< HEAD
=======

# def image_detail(request, image_id):
#     image = get_object_or_404(Image, pk=image_id)
#     comments = image.comments.all()
#     comment_form = CommentForm()
#
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.image = image
#             new_comment.user = request.user
#             new_comment.save()
#             return redirect('image_detail', image_id=image.id)
#
#     return render(request, 'image_detail.html', {'image': image, 'comments': comments, 'comment_form': comment_form})
>>>>>>> 6fc92ba (My Bootcamp-SP project)
