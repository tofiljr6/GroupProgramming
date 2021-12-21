from django.shortcuts import render
import os
from fpdf import FPDF
import subprocess
from .forms import UploadFileForm
from django.http import HttpResponseRedirect

# Create your views here.
def homeprinter(request):
    return render(request, 'printer/printer.html')

def printorder(request):
    # print("Hello world")
    #
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    c = 0
    c = title(pdf, "Glodna 4, 50-123", "Wroclaw", "Restauracja pod zlotym kernelem vol.2", c)
    c = clientsname(pdf, "Jan", "Kowalski", 24, c)
    c = addproduct(pdf, "Schabowy z ziemiaczkami", "3", "21.90", c)
    pdf.output("/Volumes/SamsungT5/GroupProgramming2/printer/static/test2.pdf")

    print("Before 2")
    os.system('lpr /Volumes/SamsungT5/GroupProgramming2/printer/static/test2.pdf')
    print("After 2")
    os.system("ls /Volumes/SamsungT5/GroupProgramming2/printer/static")
    # subprocess.Popen(['lpr', '/Volumes/SamsungT5/GroupProgramming2/printer/static/test.pdf'])
    # print(os.getcwd())

    return render(request, 'printer/printer2.html')

# pdf generate
def title(pdf, adress, city, company, c):
    pdf.cell(0, 10, txt=company, ln=c + 1)
    pdf.cell(0, 10, txt=city, ln=c + 2)
    pdf.cell(0, 10, txt=adress, ln=c + 3)
    return c


def clientsname(pdf, name, surname, id, c):
    pdf.cell(0, 10, txt=name, ln=c + 1, align="R")
    pdf.cell(0, 10, txt=surname, ln=c + 2, align="R")
    pdf.cell(0, 10, txt="RACHUNEK", ln=c + 3, align="C")
    return c


def addproduct(pdf, name, count, price, c):
    icount = float(count)
    iprice = float(price)
    isum = round(icount * iprice, 2)
    string_result = str(icount) + " x " + str(iprice) + " = " + str(isum)

    pdf.cell(0, 10, txt=name, ln=1, align="L")
    pdf.cell(0, 10, txt=string_result, ln=1, align="R")

    return c


def sumproduct(pdf, count):
    result = "Do zaplaty " + count
    pdf.cell(0, 10, txt=result, ln=1, align="R")

