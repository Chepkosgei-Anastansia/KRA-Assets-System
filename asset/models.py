from django.db import models


from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Division(models.Model):
    name = models.CharField(max_length=50)
    department=models.ForeignKey(Department, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
class Section(models.Model):
    name = models.CharField(max_length=50)
    division=models.ForeignKey(Division, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
class Grade(models.Model):
     POSITION_OPTIONS=(
        ('DEPUTY COMMISIONNER', '8'),
        ('CHIEF MANAGER','7'),
        ('MANAGER','6'),
        ('ASSISTANT MANAGER','5'),
        ('SUPERVISER','4'),
        ('OFFICER','3'),
        ('SUPPORT II','2'),
        ('SUPPORT I','1'),
    )
     designation = models.CharField(max_length=50, choices=POSITION_OPTIONS)
     def __str__(self):
        return self.designation
    
class User(models.Model):
    personal_number =models.CharField(max_length=50, primary_key=True)
    domain =models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    station=models.ForeignKey(Station, on_delete= models.CASCADE)
    section=models.ForeignKey(Section, on_delete= models.CASCADE)
    role=models.CharField(max_length=50)


    def __str__(self):
        return self.name   



class Staff(models.Model):
    staff_number =models.CharField(max_length=50, primary_key=True)
    staff_name =models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    grade=models.CharField(max_length=50)
    department=models.ForeignKey(Department, on_delete= models.CASCADE)
    division=models.ForeignKey(Division, on_delete= models.CASCADE)
    section=models.ForeignKey(Section, on_delete= models.CASCADE)
    station = models.ForeignKey(Station, on_delete= models.CASCADE)


    def __str__(self):
        return self.staff_number
    

class Asset(models.Model):
    STATUS_OPTIONS=(
        ('Working', 'Working'),
        ('Faulty','Faulty'),
    )

    serial_number = models.CharField(max_length=50, primary_key=True)
    asset_type = models.CharField(max_length=50)
    model_type = models.CharField(max_length=50)
    model_number = models.CharField(max_length=50)
    mac_address=models.CharField(max_length=50)
    os=models.BooleanField(max_length=50,default=False)
    wake_on_lan=models.BooleanField(max_length=50,default=False)
    kav=models.BooleanField(max_length=50, default=False)
    status=models.CharField(max_length=20, choices=STATUS_OPTIONS, blank=False)

class Ticket(models.Model):
    ticket_number = models.CharField(max_length=20, primary_key=True)
    ict_officer = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.ticket_number


class DeployedAsset(models.Model):
     
    MOVEMENT_OPTIONS=(
        ('NEW DEPLOYEMENT', 'NEW DEPLOYEMENT'),
        ('REDEPLOYMENT','REDEPLOYEMENT'),
        ('REDEPLOYMENT','RE-LOCATION'),
        ('CHANGE OF OWNERSHIP','CHANGE OF OWNERSHIP'),
        ('SURRENDER','SURRENDER'),
        ('EXIT WITH','EXIT WITH'),
    )
     
    asset = models.ForeignKey(Asset, on_delete= models.DO_NOTHING)
    workticket = models.ForeignKey(Ticket,on_delete= models.CASCADE)
    previous_owner = models.ForeignKey(User, on_delete= models.DO_NOTHING, related_name='previous_user')
    current_owner = models.ForeignKey(User, on_delete= models.DO_NOTHING, related_name='current_user')
    previous_location = models.CharField(max_length=50)
    current_location = models.CharField(max_length=50)
    movement_form = models.FileField(upload_to="scanned_forms/", default=None)
    movement_type = models.CharField(max_length=30, choices=MOVEMENT_OPTIONS)


    def __str__(self):
        return self.current_location


    



