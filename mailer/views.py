import email.message
from io import StringIO, BytesIO

from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import NewsletterForm, ReceiptForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def sendNewsletter(request):

    if request.method == 'POST':

        form = NewsletterForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = cd["subject"]
            message = cd['message']

            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])


    else:
        form = NewsletterForm()

    return render(request, 'mailer/newsletter.html', {'form': form})

def createPdf(request):
    x = 100
    y = 100
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=300)
    p.drawString(x, y, "HELLOWORLD")
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def getData(email, dishes, prices):
    content = "Paragon dla" + email + "\n Wystawiony przez:\n" \
              "Restauracja A\n ul. Wyspianskiego 27\n 50-370 Wroclaw \n\n " \
              "Zamowienie: \n";

    total = 0.0

    for i in range(len(dishes)):
        content += dishes[i] + " " + str(prices[i]) + " zł\n"
        total += prices[i]
    content += "Razem: " + str(total) + " zł\n"
    return content


def sendReceipt(request):

    if request.method == 'POST':

        form = ReceiptForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject = "Paragon za zamówienie"
            message = "Dziękujemy za złożone zamówienie. W załączniku znajdą państwo paragon."

            email = EmailMessage(subject, message,
             settings.DEFAULT_FROM_EMAIL, [cd['recipient']])


            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)

            t = p.beginText()
            t.setFont('Helvetica-Bold', 10)
            t.setCharSpace(3)
            t.setTextOrigin(50, 700)
            t.textLines(getData(cd['recipient'], ["Danie_X"], [15]))
            p.drawText(t)

            p.showPage()
            p.save()
            pdf = buffer.getvalue()
            buffer.close()
            email.attach("Paragon.pdf", pdf, 'application/pdf')
            email.send()


    else:
        form = ReceiptForm()

    return render(request, 'mailer/receipt.html', {'form': form})