from django_countries.fields import CountryField
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import (
    get_available_image_extensions,
    FileExtensionValidator,
)
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import datetime
from django.shortcuts import get_object_or_404
from django.views.generic.edit import BaseDeleteView
from random import random
from tinymce.models import HTMLField
import os
import base64
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# from users import models as cmodels
from general import models as gmodels
from django.utils.timezone import now




class LraMembersBiodata(models.Model):
    member_id = models.AutoField(primary_key=True)
    lra_membership_id = models.CharField(max_length=100, blank=True, default='', null=True)
    title = models.CharField(max_length=45, blank=True, default='', null=True)
    surname = models.CharField(max_length=50, blank=True, default='', null=True)
    firstname = models.CharField(max_length=50, blank=True, default='', null=True)
    middlename = models.CharField(max_length=50, blank=True, default='', null=True)
    maidenname = models.CharField(max_length=50, blank=True, default='', null=True)
    gender = models.CharField(max_length=1, blank=True, default='', null=True)
    marital_status = models.CharField(max_length=45, blank=True, default='', null=True)
    date_of_birth = models.DateField(blank=True,  auto_now=True)
    born_in_nigeria = models.IntegerField(default =0,blank=True)
    place_of_birth = models.CharField(max_length=45, blank=True, default='', null=True)
    home_town = models.CharField(max_length=45, blank=True, default='', null=True)
    address1 = models.CharField(max_length=200, blank=True, default='', null=True)
    address2 = models.CharField(max_length=200, blank=True, default='', null=True)
    country = models.CharField(max_length=45, blank=True, default='', null=True)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    lga = models.CharField(max_length=20, blank=True, default='', null=True)
    zip = models.CharField(max_length=20, blank=True, default='', null=True)
    nearest_b_stop = models.CharField(max_length=100, blank=True, default='', null=True)
    mobile1 = models.CharField(max_length=50, blank=True, default='', null=True)
    mobile2 = models.CharField(max_length=45, blank=True, default='', null=True)
    email = models.CharField(max_length=50, blank=True, default='', null=True)
    email2 = models.CharField(max_length=45, blank=True, default='', null=True)
    nationality = models.CharField(max_length=45, blank=True, default='', null=True)
    skype_id = models.CharField(max_length=20, blank=True, default='', null=True)
    unit_id = models.IntegerField(default =0,blank=True)
    position_in_dept = models.CharField(max_length=50, blank=True, default='', null=True)
    department_id = models.IntegerField(default =0,blank=True)
    department_status = models.CharField(max_length=2, blank=True, default='', null=True)
    cih_id = models.IntegerField(default =0,blank=True)
    chartered_flg = models.IntegerField(default =0,blank=True)
    affinity_group_id = models.IntegerField(blank=True, default=0, null=True)
    workforce_flg = models.IntegerField(default =0,blank=True)
    workforce_id = models.CharField(max_length=45,default='')
    mountain_id = models.IntegerField(default =0,blank=True)
    lra_govt_structure = models.CharField(max_length=100, blank=True, default='', null=True)
    date_of_spiritual_birth = models.DateField(blank=True,  auto_now=True)
    date_joined_lra = models.DateField(blank=True,  auto_now=True)
    edu_qual = models.CharField(max_length=100, blank=True, default='', null=True)
    prof_qual = models.CharField(max_length=100, blank=True, default='', null=True)
    employment_status = models.CharField(max_length=5, blank=True, default='', null=True)
    position = models.CharField(max_length=100, blank=True, default='', null=True)
    place_of_work = models.CharField(max_length=100, blank=True, default='', null=True)
    employer_address = models.CharField(max_length=100, blank=True, default='', null=True)
    employer_address2 = models.CharField(max_length=100, blank=True, default='', null=True)
    employer_telephone = models.CharField(max_length=100, blank=True, default='', null=True)
    employer_country = models.CharField(max_length=45, blank=True, default='', null=True)
    employer_state = models.IntegerField(blank=True, default='', null=True)
    employer_lga = models.IntegerField(blank=True, default='', null=True)
    industry_sector = models.CharField(max_length=100, blank=True, default='', null=True)
    sub_sector_code = models.CharField(max_length=45,default='')
    sports = models.CharField(max_length=200, blank=True, default='', null=True)
    other_sports = models.CharField(max_length=100, blank=True, default='', null=True)
    social_causes = models.CharField(max_length=200, blank=True, default='', null=True)
    entrep_interest = models.CharField(max_length=200, blank=True, default='', null=True)
    interest_sector = models.CharField(max_length=200, blank=True, default='', null=True)
    del_flg = models.CharField(max_length=1,default='')
    status = models.CharField(max_length=1,default='')
    created_on = models.DateTimeField(blank=True,  auto_now=True)
    created_by = models.IntegerField(default =0,blank=True)
    last_modified_date = models.DateTimeField(blank=True,  auto_now=True)
    last_modified_by = models.IntegerField(default =0,blank=True)
    last_session_id = models.CharField(max_length=100, blank=True, default='', null=True)
    row_id = models.IntegerField(blank=True, default='', null=True)
    source = models.CharField(max_length=45, blank=True, default='', null=True)
    upload_flg = models.IntegerField(blank=True, default='', null=True)
    cooperative = models.IntegerField(default =0,blank=True)
    advisory = models.IntegerField(default =0,blank=True)
    training = models.IntegerField(default =0,blank=True)
    profile_image_path = models.CharField(max_length=100, blank=True, default='', null=True)
    chartered_verified_flg = models.IntegerField(default =0,blank=True)
    first_timer = models.CharField(max_length=1, blank=True, default='', null=True)

    class Meta:
        managed = False
        db_table = 'lra_members_biodata'

    def __str__(self):
        return str(self.firstname) + " " +str(self.surname)


class Member(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    bio_data= models.ForeignKey(LraMembersBiodata,on_delete=models.CASCADE,default='')
    lra_membership_id = models.CharField(max_length=100, blank=True, default='', null=True)
    full_name = models.TextField(max_length=100,default='',blank=True)
    dependant=models.BooleanField(default=False)
    has_dependants=models.BooleanField(default=False)
    photo = models.ImageField(upload_to="media/members/", blank=True)
    memberid = models.CharField(max_length=50, blank=True, default='',unique=True)
    familyid = models.CharField(max_length=50, blank=True, default='')
    signup_date = models.DateField(default=now)
    profile_edit_date = models.DateField(auto_now=True)
    email_confirmed = models.BooleanField(default=True)
    date_time_added = models.DateTimeField(default=now)
    secret_question = models.TextField(max_length=100,blank=True, default='',)
    secret_answer = models.TextField(max_length=100,blank=True, default='',)
    previous_email = models.CharField(max_length=100,blank=True, default='',)
    last_token = models.CharField(max_length=20,blank=True, default='',)
    profile_updated = models.BooleanField(default=False)
    suspension_count = models.IntegerField(default=0)
    briefly_suspended = models.BooleanField(default=False)
    time_suspended = models.DateTimeField(auto_now_add=False,default=now, blank=True)
    time_suspended_timestamp = models.IntegerField(default=0,blank=True)
    private_number= models.TextField(default='',blank=False,)

    def __str__(self):
        return self.full_name
       

    def save(self,*args, **kwargs):

        if self.suspension_count>2:
            self.briefly_suspended = True
            self.time_suspended =  datetime.datetime.now()
            self.time_suspended_timestamp = datetime.datetime.now().timestamp()
        secret_question=''
        for char in self.secret_question:
            if char ==  '?':
                continue
            else:
                secret_question = secret_question +char
        self.secret_question = secret_question+'?'
        if self.full_name =='':
            self.full_name = self.user.first_name +' ' +self.user.last_name
        if self.memberid =='':
            nums = '0123456789'
            tempnums = ''
            lalph = 'abcdefghijklmnopqrstuvwxyz'
            templalph=''
            ualph = lalph.upper()
            tempualph = ''

            for num in range(0,len(nums)):
                tempnums +=nums[round((random()-0.5)*len(nums))]
            for num in range(0,len(lalph)):
                templalph +=lalph[round((random()-0.5)*len(lalph))]
            for num in range(0,len(ualph)):
                tempualph +=ualph[round((random()-0.5)*len(ualph))]
            firstletter= self.user.first_name[0].upper()
            lastletter =self.user.last_name[0].upper()
            temporary_userid = tempnums[0:3] + templalph[0:3]+tempualph[0:3]+firstletter+lastletter
            userid= []
            for char in temporary_userid:
                userid.insert(round(random()*5),char)
            userid = ''.join(userid)
            self.memberid=userid
        super(Member,self).save(*args,**kwargs)



class CenterCategoryImage(models.Model):
    name = models.CharField(max_length=20,default='image name')
    image= models.ImageField(blank=False, default ='',)
    date_time_added = models.DateTimeField(auto_now=True)


class EventCenterCategory(models.Model):
    name = models.CharField(max_length=200,default='Event name',blank = False)
    price = models.IntegerField(default=0,blank=False)
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    full_description = HTMLField()
    capacity = models.IntegerField(default=0,blank=False)
    images = models.ManyToManyField(CenterCategoryImage,default='')
    def __str__(self):
        return self.name


class EventSpecialOffer(models.Model):
    name = models.CharField(max_length=20,default='Class name',blank=False)
    price = models.IntegerField(default=0,blank=False)
    quantity = models.IntegerField(default=0,blank=False)
    subscribers = models.ManyToManyField(Member,default='')
    percent= models.IntegerField(default=0)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(EventSpecialOffer,self).save(*args,**kwargs)
        self.percent =round(100 * self.subscribers.count() /self.quantity)
        super(EventSpecialOffer,self).save(*args,**kwargs)



class EventImage(models.Model):
    name = models.CharField(max_length=20,default='image name')
    image= models.ImageField(blank=False, default ='',)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    attendee = models.ForeignKey(Member,default=3,on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=20, default='',blank=True)
    special_offers = models.ManyToManyField(EventSpecialOffer,default='',blank=True)
    status = models.CharField(max_length =100, choices=(('accredited','Accredited'),('pickedup','pickedup')), default='',blank=False)
    accredited = models.BooleanField(default=False)
    pickedup = models.BooleanField(default=False)
    dropped = models.BooleanField(default=False)
    drop_date_time = models.DateTimeField(auto_now=True)
    pickup_date_time = models.DateTimeField(auto_now=True)
    trackingid = models.CharField(max_length=20,default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)
    classid = models.CharField(max_length=20,default='',blank=True)
    verified = models.BooleanField(default=False)
    authorized = models.BooleanField(default=False)
    secured_search =models.BooleanField(default=False)
    hostedeventid=models.CharField(max_length=20,default='',blank=False)
    eventid=models.CharField(max_length=20,default='',blank=False)
    payment_reference = models.CharField(max_length=500, default='',blank=True)
    registrationid = models.CharField(max_length=20,default='',blank=False)
    dayid=models.CharField(max_length=20,default='',blank=False)
    ticketid=models.CharField(max_length=20,default='',blank=False)
    arrangementid=models.CharField(max_length=20,default='',blank=False)
    day = models.BooleanField(default=False)
    brought_in_by = models.CharField(max_length=20,default='',blank=True)
    picked_by = models.CharField(max_length=20,default='',blank=True)
    accredited_by = models.CharField(max_length=20,default='',blank=True)
    checked_out_by = models.CharField(max_length=20,default='',blank=True)
    registered_by =models.CharField(max_length=20,default='',blank=True)
    def __str__(self):
        return self.attendee.full_name




class Arrangement(models.Model):
    name = models.CharField(max_length=20,default='Arrangement name',blank=False)
    registrations = models.ManyToManyField(Registration,default='',blank=True)
    arrangement_index = models.IntegerField(default=0,verbose_name='Arrangement order')
    sections = models.IntegerField(default=0,blank=True)
    tables_per_section = models.IntegerField(default=0,blank=True)
    chairs_per_table = models.IntegerField(default=0,blank=True) 
    initials= models.CharField(max_length=20,default='',blank=True)
    percent = models.IntegerField(default=0,blank=True)
    available_chairs = models.IntegerField(default=0,blank=True)
    full = models.BooleanField(default=False)
    attendance_limit = models.IntegerField(default=0)
    eventid=models.CharField(max_length=20,default='',blank=True)
    hostedeventid=models.CharField(max_length=20,default='',blank=False)
    arrangementid=models.CharField(max_length=20,default='',blank=True)
    dayid=models.CharField(max_length=20,default='',blank=False)
    day = models.BooleanField(default=False)
    


    def __str__(self):
        return self.name

    def save(self):
        super(Arrangement,self).save()
        self.full = False
        if self.sections == 0:
            self.sections =1
        if self.tables_per_section ==0:
            self.tables_per_section =1
        self.attendance_limit =(self.sections * self.tables_per_section * self.chairs_per_table)
        self.available_chairs =  self.attendance_limit - self.registrations.count()
        if self.available_chairs <=0:
            self.full=True
        if self.registrations.count()==0:
            pass
        else:
            if(self.attendance_limit==0):
                pass
            else:
                self.percent =round(100 * self.registrations.count() /(self.attendance_limit))
                if self.sections<=0 and self.tables_per_section > 0 and self.chairs_per_table >0:
                    self.available_chairs = (self.tables_per_section * self.chairs_per_table) - self.registrations.count()
                elif self.sections<=0 and self.tables_per_section <=0 and self.chairs_per_table >0:
                    self.available_chairs =  self.chairs_per_table - self.registrations.count()
                elif self.sections>0 and self.tables_per_section >0 and self.chairs_per_table >0:
                    self.available_chairs =  (self.sections * self.tables_per_section * self.chairs_per_table) - self.registrations.count()
        if self.initials:
                pass
        else:
            initials = self.name[0]
            for char in range(1,len(self.name)):
                if char+1==len(self.name):
                    break
                elif self.name[char] ==  ' ':
                    initials+=self.name[char+1]
            self.initials = initials
        if self.arrangementid =='':
            self.arrangementid = self.hostedeventid+str(HostedEvent.objects.filter(hostedeventid=self.hostedeventid).count())+str(round(random()*1234567890))
        super(Arrangement,self).save()



class EventTicket(models.Model):
    name = models.CharField(max_length=20,default='Ticket name',blank=False)
    price = models.IntegerField(default=0,blank=False)
    attendance_limit = models.IntegerField(default=0,blank=False)
    registrations = models.ManyToManyField(Registration,default='',blank=True)
    sections = models.IntegerField(default=0,blank=True)
    tables_per_section = models.IntegerField(default=0,blank=True)
    chairs_per_table = models.IntegerField(default=0,blank=True) 
    available_quota = models.IntegerField(default=0,blank=True)
    hostedeventid=models.CharField(max_length=20,default='',blank=False)
    free = models.BooleanField(default=False)
    ticketid=models.CharField(max_length=20,default='',blank=True)
    eventid=models.CharField(max_length=20,default='',blank=True)
    initials= models.CharField(max_length=20,default='',blank=True)
    percent = models.IntegerField(default=0,blank=True)
    available_chairs = models.IntegerField(default=0,blank=True)
    full = models.BooleanField(default=False)
    dayid=models.CharField(max_length=20,default='',blank=False)
    day = models.BooleanField(default=False)
    arrangeable = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(EventTicket,self).save(*args,**kwargs)
        if self.price<=0:
            self.free = True
        if self.sections<=0 and self.tables_per_section > 0 and self.chairs_per_table >0:
            self.attendance_limit = (self.tables_per_section * self.chairs_per_table)
        elif self.sections<=0 and self.tables_per_section <=0 and self.chairs_per_table >0:
            self.attendance_limit=self.chairs_per_table
        elif self.sections>0 and self.tables_per_section >0 and self.chairs_per_table >0:
            self.attendance_limit =(self.sections * self.tables_per_section * self.chairs_per_table)
        self.available_chairs =  self.attendance_limit - self.registrations.count()
        if self.available_chairs <=0:
            self.full=True
        if self.registrations.count()==0:
            pass
        else:
            if(self.attendance_limit==0):
                pass
            else:
                self.percent =round(100 * self.registrations.count() /(self.attendance_limit))
                if self.sections<=0 and self.tables_per_section > 0 and self.chairs_per_table >0:
                    self.available_chairs = (self.tables_per_section * self.chairs_per_table) - self.registrations.count()
                elif self.sections<=0 and self.tables_per_section <=0 and self.chairs_per_table >0:
                    self.available_chairs =  self.chairs_per_table - self.registrations.count()
                elif self.sections>0 and self.tables_per_section >0 and self.chairs_per_table >0:
                    self.available_chairs =  (self.sections * self.tables_per_section * self.chairs_per_table) - self.registrations.count()
        if self.initials:
                pass
        else:
            initials = self.name[0]
            for char in range(1,len(self.name)):
                if char+1==len(self.name):
                    break
                elif self.name[char] ==  ' ':
                    initials+=self.name[char+1]
            self.initials = initials
        if self.ticketid =='':
            self.ticketid = self.hostedeventid+str(HostedEvent.objects.filter(hostedeventid=self.hostedeventid).count())+str(round(random()*1234567890))
        super(EventTicket,self).save(*args,**kwargs)



class EventDay(models.Model):
    title = models.CharField(max_length=100, default='Day Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    full_description = HTMLField(default='full Description')
    start_date_time = models.DateTimeField(default=now)
    end_date_time = models.DateTimeField(default=now)
    eventid = models.CharField(max_length=100,default='',blank =True,)
    start_time_timestamp = models.IntegerField(default=0,blank=True)
    attendance_limit = models.IntegerField(default=0,blank=True)
    hostedeventid = models.CharField(max_length=100,default='',blank =True,)
    attendees = models.ManyToManyField(Registration,blank=True, default='',)
    registrations = models.ManyToManyField(Registration,blank=True, default='',related_name='event_day_registrations')
    thumbnail= models.ImageField(default ='')
    parent_image = models.BooleanField(default=False)
    dayid= models.CharField(max_length=100,default='',blank =True,)
    day = models.IntegerField(default=0,blank=False)
    full = models.BooleanField(default=False)
    arrange = models.BooleanField(default=False,blank=True)
    arrangement_update_needed = models.BooleanField(default=False,blank=True)
    ticket_required = models.BooleanField(default=False,blank=True)
    tickets = models.ManyToManyField(EventTicket,default='',blank=True)
    arrangements = models.ManyToManyField(Arrangement,default='',blank=True)
    special_offer = models.BooleanField(default=False,blank=True)
    error = models.BooleanField(default=False,blank=True)
    special_offers = models.ManyToManyField(EventSpecialOffer,default='',blank=True)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        attendance_limit = 0
        if self.dayid =='':
            self.dayid = self.hostedeventid+str(HostedEvent.objects.filter(hostedeventid=self.hostedeventid).count())+str(round(random()*1234567890))
        self.start_time_timestamp =self.start_date_time.timestamp()
        if self.ticket_required:
            try:
                for ticket in self.tickets.all():
                    attendance_limit =attendance_limit + ticket.attendance_limit
                self.attendance_limit = attendance_limit
            except ValueError:
                pass
        elif self.arrange:
            try:
                for arrangement in self.arrangements.all():
                    attendance_limit =attendance_limit + arrangement.attendance_limit
                self.attendance_limit = attendance_limit
            except ValueError:
                pass
        super(EventDay,self).save(*args,**kwargs)

    # def delete(self,*args,**kwargs):
    #     for ticket in self.tickets.all():
    #         ticket.delete()
    #     for arrangment in self.arrangements.all():
    #         arrangment.delete()
    #     super(EventDay,self).delete(*args,**kwargs)

class HostedEvent(models.Model):
    content = models.CharField(max_length=20,default='event',editable=False,auto_created=True)
    initials = models.CharField(max_length=20,default='',blank=True)
    title = models.CharField(max_length=100, default='Hosted Event Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    start_date_time = models.DateTimeField(default=now)
    end_date_time = models.DateTimeField(default=now)
    thumbnail= models.ImageField(default ='',blank=True)
    images=models.ManyToManyField(EventImage, blank=True, default='',)
    video_link = models.CharField(max_length=100, default ='', blank=True)
    full_description = HTMLField()
    open_to = models.CharField(max_length =100, choices=(('children','Children'), ('adults','Adults')),default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)
    eventid = models.CharField(max_length=100,default='',blank =True,)
    hostedeventid = models.CharField(max_length=100,default='',blank =True,)
    start_time_timestamp = models.IntegerField(default=0,blank=True)
    payment_required = models.BooleanField(default=False)
    registrations = models.ManyToManyField(Registration,blank=True, default='',related_name='registration')
    attendance_limit = models.IntegerField(default=0,blank=True)
    one_time_ticketing = models.BooleanField(default=False,blank=True)
    special_offer = models.BooleanField(default=False,blank=True)
    special_offers = models.ManyToManyField(EventSpecialOffer,default='',blank=True)
    one_time_arrangement = models.BooleanField(default=False,blank=True)
    arrangement_update_needed = models.BooleanField(default=False,blank=True)
    one_day = models.BooleanField(default=True,blank=True)
    tickets = models.ManyToManyField(EventTicket,default='',blank=True)
    arrangements = models.ManyToManyField(Arrangement,default='',blank=True)
    verification_steps = models.CharField(max_length=2,default='0',choices=(('0','0'),('1','1'),('2','2')))
    days = models.ManyToManyField(EventDay,default='',blank=True)
    ended = models.BooleanField(default=False,blank=True)
    editable = models.BooleanField(default=True,blank=True)
    publishable = models.BooleanField(default=True,blank=True)
    published = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.title + ' '+ str(self.start_date_time.date())
        
    def save(self,*args,**kwargs):
        if self.initials:
            pass
        else:
            initials = self.title[0]
            for char in range(1,len(self.title)):
                if char+1==len(self.title):
                    break
                elif self.title[char] ==  ' ':
                    initials+=self.title[char+1]
            self.initials = initials
        if self.hostedeventid =='':
            self.hostedeventid= str(round(random() *1234567890))[0:5]+str(Event.objects.all().count()+1)
        self.start_time_timestamp =self.start_date_time.timestamp()
        attendance_limit = 0
        try:
            for ticket in self.tickets.all():
                attendance_limit =attendance_limit + ticket.attendance_limit
            self.attendance_limit = attendance_limit
        except ValueError:
            pass
        try:
            for arrangement in self.arrangements.all():
                attendance_limit =attendance_limit + arrangement.attendance_limit
            self.attendance_limit = attendance_limit
        except ValueError:
            pass
        super(HostedEvent,self).save(*args,**kwargs)
        
        
 
class Event(models.Model):
    content = models.CharField(max_length=20,default='event',editable=False,auto_created=True)
    initials = models.CharField(max_length=20,default='',blank=True)
    # host = models.ForeignKey(Member,on_delete=models.CASCADE,default='',blank=True)
    title = models.CharField(max_length=100, default='Event Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    full_description = HTMLField()
    thumbnail= models.ImageField(default ='')
    date_time_added = models.DateTimeField(auto_now=True)
    eventid = models.CharField(max_length=100,default='',blank =True,)
    hosted_events = models.ManyToManyField(HostedEvent,blank=True, default='',)
    reoccur = models.BooleanField(default=False,blank= True)
    reoccurance_frequency = models.CharField(max_length=20, blank=True, default='', choices=(('daily','Daily'),('weekly','Weekly'),('monthly','Monthly'),('yearly','Yearly')))
    def __str__(self):
        return self.title
        
    def save(self,*args,**kwargs):
        if self.initials:
            pass
        else:
            initials = self.title[0]
            for char in range(1,len(self.title)):
                if char+1==len(self.title):
                    break
                elif self.title[char] ==  ' ':
                    initials+=self.title[char+1]
            self.initials = initials
        if self.eventid =='':
            self.eventid=self.initials+ str(round(random() *1234567890))[0:5]+str(Event.objects.all().count()+1)
        super(Event,self).save(*args,**kwargs)
        
               



class Announcement(models.Model):
    content = models.CharField(max_length=20,default='announcement',editable=False,auto_created=True)
    title = models.CharField(max_length=100, default='Event Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    contentid = models.CharField(max_length=100,default='',blank =True,)
    # thumbnail= models.ImageField(blank=False, default ='',)
    video_link = models.CharField(max_length=100, default ='', blank=True )
    full_description = HTMLField()
    date_time_added = models.DateTimeField(auto_now=True)
    read = models.ManyToManyField(Member,blank=True, default='',)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if self.announcementid =='':
            self.announcementid= str(round(random() *1234567890))[0:5]+str(Announcement.objects.all().count()+1)
        super(Announcement,self).save(*args,**kwargs)



class Video(models.Model):
    content = models.CharField(max_length=20,default='video',editable=False,auto_created=True)
    title = models.CharField(max_length=100, default='video Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    video_id = models.CharField(max_length=100, default ='', blank=True )
    date_time_added = models.DateTimeField(auto_now=True)
    read = models.ManyToManyField(Member,blank=True, default='',)

    def __str__(self):
        return self.title
    
    def save(self):
        # if 'https://' in self.link:
        #     pass

        # else:
        #     self.link = 'https://'+self.link
        super(Video, self).save()






class ArticleImage(models.Model):
    image= models.ImageField(blank=False, default ='',)

    def __str__(self):
        return self.event.title


class Article(models.Model):
    content = models.CharField(max_length=20,default='article',editable=False,auto_created=True)
    title = models.CharField(max_length=100, default='Article Title')
    short_description = models.CharField(max_length=100, default='short description',blank = True)
    thumbnail= models.ImageField(blank=False, default ='',)
    images=models.ManyToManyField(ArticleImage, blank=True, default='',)
    video_link = models.CharField(max_length=100, default ='', blank=True )
    contentid = models.CharField(max_length=100,default='',blank =True,)
    full_description = HTMLField()
    read = models.ManyToManyField(Member,default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if self.articleid =='':
            self.articleid= str(round(random() *1234567890))[0:5]+str(Article.objects.all().count()+1)
        super(Article,self).save(*args,**kwargs)