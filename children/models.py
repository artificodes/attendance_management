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
from django.core.exceptions import ValidationError
from members import models as mmodels
import math



class General(models.Model):

    phone_number_1 = models.CharField(max_length=13, default ='', blank=True, )
    phone_number_1_handler = models.CharField(max_length=100, default ='', blank=True, )
    phone_number_2 = models.CharField(max_length=13, default ='', blank=True, )
    phone_number_2_handler = models.CharField(max_length=100, default ='', blank=True, )
    email_1 = models.CharField(max_length=100, default ='', blank=True, )
    email_1_handler = models.CharField(max_length=100, default ='', blank=True, )
    email_2 = models.CharField(max_length=100, default ='', blank=True, )
    email_2_handler = models.CharField(max_length=100, default ='', blank=True, )
    def __str__(self):
        return 'Children Administrators'
    class Meta:
        verbose_name ='Setting'

    def clean(self):
        """
        Throw ValidationError if you try to save more than one model instance
        See: http://stackoverflow.com/a/6436008
        """
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError(
                "Can only create 1 instance of %s." % model.__name__)



class LraMembersChildren(models.Model):
    child_id = models.AutoField(primary_key=True)
    c_surname = models.CharField(max_length=50, blank=True, null=True)
    c_firstname = models.CharField(max_length=50, blank=True, null=True)
    c_middlename = models.CharField(max_length=50, blank=True, null=True)
    c_gender = models.CharField(max_length=1, blank=True, null=True)
    c_date_of_birth = models.DateField(default=now,blank=True,editable=True)
    member_id = models.IntegerField(blank=True, null=True)
    c_phone = models.CharField(max_length=50, blank=True, null=True)
    c_email = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    del_flg = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    created_by = models.IntegerField(blank=True, null=True)
    last_modified_date = models.DateField(blank=True, null=True)
    last_modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lra_members_children'
        unique_together = (('c_surname', 'c_firstname', 'parent_id', 'del_flg'),)

    def __str__(self):
        return self.c_firstname +' ' + self.c_surname

class Dependant(models.Model):
    member = models.ForeignKey(mmodels.Member,on_delete=models.CASCADE,default='',related_name='member')
    parent = models.ForeignKey(mmodels.Member,on_delete=models.CASCADE,default='',related_name='Dependent')
    bio_data = models.ForeignKey(LraMembersChildren,on_delete=models.CASCADE,default='')
    parentid = models.CharField(default='',max_length=100,blank=True)
    date_of_birth = models.DateField(default=now,blank=True,editable=True)
    care=models.TextField(max_length=500,default='',blank=True)
    special_care = models.BooleanField(default=False,blank=True)
    available = models.BooleanField(default=True,blank=True)
    dependantid = models.CharField(default='',max_length=100,blank = True)
    date_time_added = models.DateTimeField(auto_now=True)
    groupid = models.CharField(default='',max_length=100,blank = True)
    classid = models.CharField(default='',max_length=100,blank=True)
    classname= models.CharField(default='',max_length=100,blank=True)
    groupname = models.CharField(default='',max_length=100,blank=True)
    agef = models.FloatField(default=0,blank=True,)
    age = models.IntegerField(default=0,blank=True,)
    photo = models.ImageField(default='',blank=True)
    def __str__(self):
        return self.bio_data.c_firstname + ' ' +self.bio_data.c_surname

    def save(self,*args, **kwargs):


        classroomfound = False
        try:
            dateofbirth = datetime.datetime(self.bio_data.c_date_of_birth.year,self.bio_data.c_date_of_birth.month,self.bio_data.c_date_of_birth.day)
            self.agef = ((datetime.datetime.timestamp(datetime.datetime.now()) - datetime.datetime.timestamp(dateofbirth))/31556952)
            self.age = datetime.datetime.now().year - dateofbirth.year
        except AttributeError:
            pass

        if self.groupid != '' and self.classid !='':
            try:
                group = Group.objects.get(groupid = self.groupid)
                group.pupils.add(self)
                self.groupname=group.name
            except ObjectDoesNotExist:
                pass
            try:
                classroom = ClassRoom.objects.get(classid = self.classid)
                classroom.pupils.add(self)
                self.classname =classroom.name
            except ObjectDoesNotExist:
                pass
            self.parentid = self.parent.memberid      
            super(Dependant,self).save(*args, **kwargs)

        else:

            self.groupid=''
            self.groupname=''
            self.classid=''
            self.classname=''
        

            super(Dependant,self).save(*args, **kwargs)

            groups = Group.objects.all()
            for group in groups:
                for pupil in group.pupils.all():
                    if self == pupil:
                        group.pupils.remove(self)
            try:
                group = Group.objects.get(age = self.age)
                group.pupils.add(self)
                self.groupname = group.name
                self.groupid = group.groupid
                groupclassrooms = list(group.classrooms.all())

                classrooms = []
                for index in range(len(groupclassrooms)):
                    classrooms.append([])
                    classrooms[index].append(groupclassrooms[index].arrangement_index)
                    classrooms[index].append(groupclassrooms[index])
                for classroom in groupclassrooms:
                    classrooms[index].append(classroom)
                
                classrooms.sort(key=lambda x: x[0])
                classroomfound = True
                for classroom in classrooms:
                    classroom = classroom[1]
                    if classroom.full:
                        pass
                    else:
                        self.classid = classroom.classid
                        self.classname = classroom.name
                        break
            except ObjectDoesNotExist:
                pass
            
            if classroomfound:
                classroom.pupils.add(self)




class Guardian(models.Model):
    member =models.ForeignKey(mmodels.LraMembersBiodata,on_delete=models.CASCADE,default='')
    active = models.BooleanField(default=True)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.firstname +' ' +self.member.surname


class Parent(models.Model):
    member = models.ForeignKey(mmodels.Member,on_delete=models.CASCADE,default='')
    parent_2 = models.ManyToManyField(mmodels.Member,default='',related_name='parent_2')
    dependants = models.ManyToManyField(Dependant,default='',blank=True,related_name='Dependants')
    date_time_added = models.DateTimeField(auto_now=True)
    guardians = models.ManyToManyField(Guardian,default='',blank=True,related_name='Guardians')


    def __str__(self):
        return self.member.full_name

    def save(self,*args,**kwargs):
        super(Parent,self).save(*args,**kwargs)
        
        try:
            try:
                parent2 = Parent.objects.get(member = self.parent_2.all()[0])
                parent2.member.familyid=self.member.familyid
                parent2.member.save()
                for dependant in self.dependants.all():
                    if dependant in parent2.dependants.all():
                        pass
                    else:
                        parent2.dependants.add(dependant)

                parent2.parent_2.clear()
                parent2.parent_2.add(self.member)
                for dependant in parent2.dependants.all():
                    if dependant in self.dependants.all():
                        pass
                    else:
                        self.dependants.add(dependant)
            except IndexError:
                self.parent_2.add(self.member)
            for dependant in self.dependants.all():
                dependant.member.familyid=self.member.familyid
                dependant.member.save()

            
        except ObjectDoesNotExist:
            pass



class ClassRoomRegistration(models.Model):
    registrations = models.ManyToManyField(mmodels.Registration,default='',blank=True)
    full = models.BooleanField(default=False)
    eventid=models.CharField(max_length=20,default='',blank=True)
    hostedeventid=models.CharField(max_length=20,default='',blank=True)
    arrangementid=models.CharField(max_length=20,default='',blank=True)
    dayid=models.CharField(max_length=20,default='',blank=True)
    day = models.BooleanField(default=False)
    classid = models.CharField(max_length=20,default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        hostedevent = mmodels.HostedEvent.objects.get(eventid=self.eventid,hostedeventid=self.hostedeventid)
        return self.classid  + ' ' + str(self.registrations.count()) + ' ' + str(hostedevent.start_date_time.date())

    def save(self,*args,**kwargs):
        # classroomcapacity = ClassRoom.objects.get(classid=self.classid).capacity
        # if self.registrations.count() == classroomcapacity:
        #     self.full=True
        super(ClassRoomRegistration,self).save(*args,**kwargs)

class ClassRoom(models.Model):
    name = models.CharField(max_length=100,default='Class room name',blank=False)
    registrations = models.ManyToManyField(ClassRoomRegistration,default='',blank=True)
    initials= models.CharField(max_length=20,default='',blank=True)
    capacity = models.IntegerField(default=0)
    arrangement_index = models.IntegerField(default=0,verbose_name='Position for arrangement')
    classid=models.CharField(max_length=20,default='',blank=True)
    pupils = models.ManyToManyField(Dependant,default='',blank=True)
    full = models.BooleanField(default=False)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
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

        super(ClassRoom,self).save(*args,**kwargs)
        for pupil in self.pupils.all():
            pupil.save()
        if self.pupils.count() == self.capacity:
            self.full = True
        else:
            self.full = False
        super(ClassRoom,self).save()


class Group(models.Model):
    name = models.CharField(max_length=100,default='Group name',blank=False)
    pupils = models.ManyToManyField(Dependant,default='',blank=True)
    age = models.IntegerField(default=0,blank=True,verbose_name='Age')
    classrooms = models.ManyToManyField(ClassRoom,default='',blank=True)
    initials= models.CharField(max_length=20,default='',blank=True)
    groupid=models.CharField(max_length=20,default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name + str(self.age)

    def save(self,*args,**kwargs):

        initials = self.name[0]
        for char in range(1,len(self.name)):
            if char+1==len(self.name):
                break
            elif self.name[char] ==  ' ':
                initials+=self.name[char+1]
        self.initials = initials.upper()

        self.groupid = self.initials+str(self.age)

        super(Group,self).save(*args,**kwargs)
        for pupil in self.pupils.all():
            pupil.save()

        for classroom in self.classrooms.all():
            classroom.classid=self.groupid+classroom.initials
            classroom.save()

class Teacher(models.Model):
    member = models.ForeignKey(mmodels.Member,on_delete=models.CASCADE,default='')
    classroom = models.ForeignKey(ClassRoom,default='',on_delete=models.CASCADE,)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.full_name

    def save(self,*args,**kwargs):
        self.member.user.is_staff = True
         
        self.member.user.save()
        super(Teacher,self).save(*args,**kwargs)

class Administrator(models.Model):
    member = models.ForeignKey(mmodels.Member,on_delete=models.CASCADE,default='')
    # phone_number = models.CharField(max_length=100, default ='', blank=True, )
    # email = models.EmailField(max_length=100, default ='', blank=True, )
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    can_receive_emails = models.BooleanField(default=False,verbose_name='Receive child status emails')
    can_receive_calls = models.BooleanField(default=False,verbose_name='Receive child status calls')
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member.full_name


    def save(self):
        if self.is_staff:
            self.member.user.is_staff = True
        else:
            self.member.user.is_staff = False
        if self.is_superuser:
            self.member.user.is_superuser = True
        else:
            self.member.user.is_superuser = False            
        self.member.user.save()
        super(Administrator,self).save()


# class EventSpecialOffer(models.Model):
#     name = models.CharField(max_length=20,default='Class name',blank=False)
#     price = models.IntegerField(default=0,blank=False)
#     quantity = models.IntegerField(default=0,blank=False)
#     subscribers = models.ManyToManyField(Dependant,default='')
#     percent= models.IntegerField(default=0)
#     def __str__(self):
#         return self.name

#     def save(self,*args,**kwargs):
#         super(EventSpecialOffer,self).save(*args,**kwargs)
#         self.percent =round(100 * self.subscribers.count() /self.quantity)
#         super(EventSpecialOffer,self).save(*args,**kwargs)



# class EventImage(models.Model):
#     name = models.CharField(max_length=20,default='image name')
#     image= models.ImageField(blank=False, default ='',)
#     date_time_added = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name



# class EventDay(models.Model):
#     title = models.CharField(max_length=100, default='Day Title')
#     short_description = models.CharField(max_length=1000, default='short description',blank = True)
#     full_description = HTMLField(default='full Description')
#     start_date_time = models.DateTimeField(default=now)
#     end_date_time = models.DateTimeField(default=now)
#     eventid = models.CharField(max_length=225,default='',blank =True,)
#     start_time_timestamp = models.IntegerField(default=0,blank=True)
#     attendance_limit = models.IntegerField(default=0,blank=True)
#     hostedeventid = models.CharField(max_length=225,default='',blank =True,)
#     attendees = models.ManyToManyField(mmodels.Registration,default='',blank=True,)
#     registrations = models.ManyToManyField(mmodels.Registration,default='',blank=True,related_name='event_day_registrations')
#     thumbnail= models.ImageField(default ='')
#     parent_image = models.BooleanField(default=False)
#     dayid= models.CharField(max_length=225,default='',blank =True,)
#     day = models.IntegerField(default=0,blank=False)
#     full = models.BooleanField(default=False)
#     arrange = models.BooleanField(default=False,blank=True)
#     arrangement_update_needed = models.BooleanField(default=False,blank=True)
#     classroomregistraions = models.ManyToManyField(ClassRoomRegistration,default='',blank=True)
#     special_offer = models.BooleanField(default=False,blank=True)
#     error = models.BooleanField(default=False,blank=True)
#     special_offers = models.ManyToManyField(EventSpecialOffer,default='',blank=True)
#     def __str__(self):
#         return self.title

#     def save(self,*args,**kwargs):
#         attendance_limit = 0
#         if self.dayid =='':
#             self.dayid = self.hostedeventid+str(HostedEvent.objects.filter(hostedeventid=self.hostedeventid).count())+str(round(random()*1234567890))
#         self.start_time_timestamp =self.start_date_time.timestamp()

#         super(EventDay,self).save(*args,**kwargs)

#     # def delete(self,*args,**kwargs):
#     #     for ticket in self.tickets.all():
#     #         ticket.delete()
#     #     for arrangment in self.arrangements.all():
#     #         arrangment.delete()
#     #     super(EventDay,self).delete(*args,**kwargs)

# class HostedEvent(models.Model):
#     content = models.CharField(max_length=20,default='event',editable=False,auto_created=True)
#     initials = models.CharField(max_length=20,default='',blank=True)
#     title = models.CharField(max_length=100, default='Hosted Event Title')
#     short_description = models.CharField(max_length=1000, default='short description',blank = True)
#     start_date_time = models.DateTimeField(default=now)
#     end_date_time = models.DateTimeField(default=now)
#     thumbnail= models.ImageField(default ='',blank=True)
#     images=models.ManyToManyField(EventImage, blank=True, default ='',)
#     video_link = models.CharField(max_length=100, default ='', blank=True)
#     full_description = HTMLField()
#     date_time_added = models.DateTimeField(auto_now=True)
#     eventid = models.CharField(max_length=225,default='',blank =True,)
#     hostedeventid = models.CharField(max_length=225,default='',blank =True,)
#     start_time_timestamp = models.IntegerField(default=0,blank=True)
#     payment_required = models.BooleanField(default=False)
#     registrations = models.ManyToManyField(mmodels.Registration,default='',blank=True,related_name='registration')
#     attendance_limit = models.IntegerField(default=0,blank=True)
#     one_time_ticketing = models.BooleanField(default=False,blank=True)
#     special_offer = models.BooleanField(default=False,blank=True)
#     special_offers = models.ManyToManyField(EventSpecialOffer,default='',blank=True)
#     one_time_arrangement = models.BooleanField(default=False,blank=True)
#     arrangement_update_needed = models.BooleanField(default=False,blank=True)
#     one_day = models.BooleanField(default=False,blank=True)
#     classroomregistrations = models.ManyToManyField(ClassRoomRegistration,default='',blank=True)
#     verification_steps = models.CharField(max_length=2,default='0',choices=(('0','0'),('1','1'),('2','2')))
#     days = models.ManyToManyField(EventDay,default='',blank=True)
#     ended = models.BooleanField(default=False,blank=True)
#     editable = models.BooleanField(default=True,blank=True)
#     publishable = models.BooleanField(default=True,blank=True)
#     published = models.BooleanField(default=False,blank=True)

#     def __str__(self):
#         return self.title
        
#     def save(self,*args,**kwargs):
#         if self.initials:
#             pass
#         else:
#             initials = self.title[0]
#             for char in range(1,len(self.title)):
#                 if char+1==len(self.title):
#                     break
#                 elif self.title[char] ==  ' ':
#                     initials+=self.title[char+1]
#             self.initials = initials
#         if self.hostedeventid =='':
#             self.hostedeventid= str(round(random() *1234567890))[0:5]+str(Event.objects.all().count()+1)
#         self.start_time_timestamp =self.start_date_time.timestamp()
#         attendance_limit = 0
#         super(HostedEvent,self).save(*args,**kwargs)
        
        
 
# class Event(models.Model):
#     content = models.CharField(max_length=20,default='event',editable=False,auto_created=True)
#     initials = models.CharField(max_length=20,default='',blank=True)
#     title = models.CharField(max_length=100, default='Event Title')
#     short_description = models.CharField(max_length=1000, default='short description',blank = True)
#     full_description = HTMLField()
#     thumbnail= models.ImageField(default ='')
#     date_time_added = models.DateTimeField(auto_now=True)
#     eventid = models.CharField(max_length=225,default='',blank =True,)
#     hosted_events = models.ManyToManyField(HostedEvent,default='',blank=True,)
#     reoccur = models.BooleanField(default=False,blank= True)
#     reoccurance_frequency = models.CharField(max_length=20, default='',blank=True, choices=(('daily','Daily'),('weekly','Weekly'),('monthly','Monthly'),('yearly','Yearly')))
#     def __str__(self):
#         return self.title
        
#     def save(self,*args,**kwargs):
#         if self.initials:
#             pass
#         else:
#             initials = self.title[0]
#             for char in range(1,len(self.title)):
#                 if char+1==len(self.title):
#                     break
#                 elif self.title[char] ==  ' ':
#                     initials+=self.title[char+1]
#             self.initials = initials
#         if self.eventid =='':
#             self.eventid=self.initials+ str(round(random() *1234567890))[0:5]+str(Event.objects.all().count()+1)
#         super(Event,self).save(*args,**kwargs)
        
               

class Announcement(models.Model):
    content = models.CharField(max_length=20,default='announcement',editable=False,auto_created=True)
    title = models.CharField(max_length=100, default='Event Title')
    short_description = models.CharField(max_length=1000, default='short description',blank = True)
    contentid = models.CharField(max_length=225,default='',blank =True,)
    # thumbnail= models.ImageField(blank=False, default ='',)
    video_link = models.CharField(max_length=100, default ='', blank=True, )
    full_description = HTMLField()
    date_time_added = models.DateTimeField(auto_now=True)
    read = models.ManyToManyField(Parent,default='',blank=True,)
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if self.announcementid =='':
            self.announcementid= str(round(random() *1234567890))[0:5]+str(Announcement.objects.all().count()+1)
        super(Announcement,self).save(*args,**kwargs)



class Video(models.Model):
    content = models.CharField(max_length=20,default='video',editable=False,auto_created=True)
    title = models.CharField(max_length=100, default='video Title')
    short_description = models.CharField(max_length=1000, default='short description',blank = True)
    video_id = models.CharField(max_length=100, default ='', blank=True, )
    date_time_added = models.DateTimeField(auto_now=True)
    read = models.ManyToManyField(Parent,default='',blank=True,)

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
    short_description = models.CharField(max_length=1000, default='short description',blank = True)
    thumbnail= models.ImageField(blank=False, default ='',)
    images=models.ManyToManyField(ArticleImage, blank=True, default ='',)
    video_link = models.CharField(max_length=100, default ='', blank=True, )
    contentid = models.CharField(max_length=225,default='',blank =True,)
    full_description = HTMLField()
    read = models.ManyToManyField(Parent,default='',blank=True)
    date_time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if self.articleid =='':
            self.articleid= str(round(random() *1234567890))[0:5]+str(Article.objects.all().count()+1)
        super(Article,self).save(*args,**kwargs)