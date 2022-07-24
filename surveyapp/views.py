from django.shortcuts import render, redirect
from .models import survey
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def index(request):
    if request.method == 'POST':
        applying = request.POST.getlist('applying')
        applicant = request.POST['applicant']
        Name = request.POST['Name']
        careOf = request.POST.get('careOf', False)
        other = request.POST['other']
        FatherOrHusbandName = request.POST['FatherOrHusbandName']
        gender = request.POST['gender']
        dob = request.POST['dob']
        communicationAddress = request.POST['communicationAddress']
        phone = request.POST['phone']
        whatsappNumber = request.POST['whatsappNumber']
        email = request.POST['email']
        adharNumber = request.POST['adharNumber']
        panNumber = request.POST['panNumber']
        bankLocation = request.POST['bankLocation']
        selfPhoto = request.FILES.get('selfPhoto')
        adhar1 = request.FILES.get('adhar1')
        adhar2 = request.FILES.get('adhar2')
        panCard = request.FILES.get('panCard')
        if careOf == False:
            careOf = other
        data = survey(Applying_For = applying,Applicant=applicant, Name=Name, Care_Of=careOf, Father_Or_Husband_Name=FatherOrHusbandName,
                            Gender=gender,DOB=dob, Communication_Address=communicationAddress, Mobile_Number=phone, Whatsapp_Number=whatsappNumber,
                            Email=email, Adhar_Number=adharNumber, Pan_Number=panNumber,
                      Bank_CSP_Center_Location=bankLocation, Self_photo=selfPhoto, Adhar_Front=adhar1,
                      Adhar_Back=adhar2, Pan_Card=panCard)
        data.save()
        send_mail(
            'Application Form Submission',
            'Hello Sir,Your application has been submitted successfully with application ID:\nKindly save the Application Number for future reference.\nThanks & Regards',
            'from@example.com',
            [email],
            fail_silently=True,
        )
        messages.error(request, "Saved Successfully")
        return redirect('index')
    return render(request, 'index.html')
