import hashlib, random, sys
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from . import constants
from O365 import Account
from picklefield.fields import PickledObjectField
import pandas as pd 
from pandas import DataFrame as df


# Create your models here.
from .googleDriveApi import GoogleDriveApi


class Organization(models.Model):
    name = models.CharField(max_length=200)
    logo = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('project:organization_detail',kwargs={'pk':self.pk})
    @property
    def team(self):

        team_members = [t.user for t in Client.objects.filter(organization=self)] + [x for x in User.objects.filter(is_staff=True)]      

        #print(t.email for t in team_members)
        return team_members
    @property
    def team_email(self):
        team_members = [t.user for t in Client.objects.filter(organization=self)] + [x for x in User.objects.filter(is_staff=True)]        
        email_list = [t.email for t in list(team_members)]
        return email_list
    @property
    def videos(self):
        videos = Award.objects.filter(awards__organization=self)
        return videos
    @property
    def awards(self):
        return Awards.objects.filter(organization=self)

    @property
    def promotion(self):
        return Promotion.objects.filter(organization=self)
    @property
    def message(self):
        return Message.objects.filter(organization=self)
    @property
    def projects(self):
        return [a for a in self.awards if a.active==True] + [p for p in self.promotion] + [c for c in self.message]

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_first = models.CharField(max_length=200)
    contact_last = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=200, blank=True, null=True)
    contact_email = models.EmailField()
    contact_role = models.CharField(max_length=200,blank=True,null=True,default='')
    partner_logo = models.URLField(max_length=2000, null=True, blank=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.user.username


    def get_absolute_url(self):
        return reverse('project:partner_projects', kwargs={'pk': self.pk})

    @property
    def awards(self):
        return Project.objects.filter(client=self)

    @property
    def promotion(self):
        return Promotion.objects.filter(client=self)
    @property
    def message(self):
        return Message.objects.filter(client=self)

    @property
    def projects(self):
        return [x for x in self.awards] + [y for y in self.promotion] + [z for z in self.message]
    @property
    def list_of_videos(self):

        return [x for x in Video.objects.filter(project__client=self)] + [y for y in self.message] + [z for z in self.promotion]




class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    date = models.DateField()
    number_of_awards = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.client} {self.project_name} {self.date.year}"

    def get_absolute_url(self):
        return reverse('project:project_overview', kwargs={'partner_id': self.client.id, 'project_id': self.pk})

    @property
    def project_videos(self):
        return self.number_of_awards

    @property
    def type(self):
        return 'awards'


class Video(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    award_number = models.PositiveSmallIntegerField()
    award_name = models.CharField(max_length=200000)
    award_description = models.TextField()
    award_winner = models.CharField(max_length=2000)
    award_comments = models.TextField()
    award_assets = models.URLField(null=True, blank=True, default='#')
    script = models.URLField(null=True, blank=True, default='#')
    draft = models.URLField(null=True, blank=True, default='#')
    final_draft = models.URLField(null=True, blank=True, default='#')

    def __str__(self):
        return f"{self.project.client.user.username} {self.project.project_name} {str(self.award_number)} {self.award_name}"

    def get_absolute_url(self):
        return reverse('project:video_detail',
                       kwargs={'pk': self.pk, 'partner_id': self.project.client.id, 'project_id': self.project.id})

    @property
    def project_videos(self):
        return Project.objects.filter(client__id=self.project.id).count()


class Promotion(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=500)
    logo = models.URLField(blank=True, null=True)
    theme = models.TextField(blank=True, null=True)
    attendees = models.PositiveSmallIntegerField(blank=True, null=True)
    exhibitors = models.PositiveSmallIntegerField(blank=True, null=True)
    venue = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    target_audience = models.CharField(max_length=200, blank=True, null=True)
    feature_1 = models.TextField(blank=True, null=True)
    feature_2 = models.TextField(blank=True, null=True)
    feature_3 = models.TextField(blank=True, null=True)
    feature_4 = models.TextField(null=True,blank=True)
    feature_5 = models.TextField(null=True,blank=True)
    assets = models.URLField(null=True,blank=True)
    guests = models.CharField(max_length=200, null=True,blank=True)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.client.user.username} {self.name}- {self.date}"

    @property
    def type(self):
        return 'promotion'

    def get_absolute_url(self):
        return reverse('project:promotion_detail', kwargs={'partner_id': self.client.id, 'pk': self.pk})

    @property
    def project_videos(self):
        return 1


class Message(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=2000, default="Client Message")
    date = models.DateField(null=True, blank=True)
    draft_script = models.URLField(null=True, blank=True)
    script = models.URLField(null=True, blank=True)
    assets = models.URLField(null=True, blank=True)
    draft = models.URLField(null=True, blank=True)
    final = models.URLField(null=True, blank=True)
    notes = JSONField(default=dict)
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"Message {self.organization.name}"
    @property
    def type(self):
        return 'message'

    def get_absolute_url(self):
        return reverse('project:message_detail', kwargs={'partner_id': self.client.id, 'pk': self.pk})
class Awards(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    date = models.DateField()
    folder_id = models.CharField(max_length=100, null=True, blank=True)
    number_of_awards = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)

    def get_object(self,queryset=None):
        obj = super(PostDetailView, self).get_object()
        if not obj.owner == self.request.user:
            print('you shall not pass')
        return obj

    def project_comments(self):
        all_comments = pd.concat([pd.concat([df([[x.award_number,x.award_name,x.award_project]],columns=['NUMBER','AWARD','PROJECT']),x.edit_comments],axis=1) for x in self.awards_list])
        return all_comments
    def __str__(self):
        return f"{self.organization.name} {self.project_name} {self.date.year}"

    def created_message(self):
        team_email = self.organization.team_email
        emaillist = list(set([team_email[0],team_email[1],team_email[2]]))
        subject = f"New Awards Project created for {self.organization.name}"
        html_content = '<h4>Thank you for adding 'f"{self.project_name}"' to the production portal. You can view all updates to this project and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.organization.id}/awards/{self.id}"'">'f"{self.project_name}"'</a></h4>'        
        text_content = f"Thank you for adding {self.project_name} to the production portal. You can view the progress and make changes to the project at http://www.virtuous-circle/org/{self.organization.id}/awards/{self.pk}"
        
        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content
        message.to.add([emaillist])
        message.send()
        
        
    def get_absolute_url(self):
        return reverse('project:awards_detail', kwargs={'org_id': self.organization.id, 'pk': self.pk})
    @property
    def awards_list(self):
        return Award.objects.filter(awards=self).order_by('award_number','award_name')
    @property
    def project_videos(self):
        return self.number_of_awards

    @property
    def type(self):
        return 'awards'


@receiver(post_save, sender=Awards)
def update_awards(sender, instance, **kwargs):    
    #instance.created_message()       
    if instance.folder_id is None:
        print('here three times 246')
        gd = GoogleDriveApi()
        instance.folder_id = gd.createFolder(instance.project_name)
        instance.save()


class Award(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE)
    award_number = models.PositiveSmallIntegerField(null=True)
    award_name = models.CharField(max_length=200000)
    award_description = models.TextField(blank=True,null=True)
    award_winner = models.CharField(max_length=2000)
    award_project = models.CharField(max_length=2000,null=True,blank=True)
    award_comments = models.TextField()
    award_assets = models.URLField(null=True, blank=True, default='#')
    script = models.URLField(null=True, blank=True, default='#')
    draft = models.URLField(null=True, blank=True, default='#')
    final_draft = models.URLField(null=True, blank=True, default='#')
    edit_comments = PickledObjectField(null=True)
    folder_id = models.CharField(max_length=100, null=True, blank=True)
    __original_script = None
    __original_draft = None
    __original_final = None
    complete =  models.BooleanField(default=False)

    def __str__(self):
        return f"{self.awards.organization.name} {self.awards.project_name} {str(self.award_number)} {self.award_name}"
    

    def get_absolute_url(self):
        return reverse('project:award_detail',
                       kwargs={'pk': self.pk, 'org_id': self.awards.organization.id, 'awards_id': self.awards.id})
    def updated_draft(self):
        team_email = self.awards.organization.team_email
        print(team_email)
        subject = f"Updated Draft added for video: {self.awards.project_name} {self.award_name}"
        html_content = '<h4>We have updated a draft for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly."
        text_content = 'We have updated a draft for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly." 
        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content        
        message.to.add([team_email])
        message.send()
    
    def updated_final(self):
        team_email = self.awards.organization.team_email        
        subject = f"Updated Final added for video: {self.awards.project_name} {self.award_name}"
        html_content = '<h4>We have updated a final-draft for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly."
        text_content = 'We have updated a final-draft draft for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly." 
        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content        
        message.to.add([team_email])
        message.send()

    def comment_added(self):        
        subject = f"Updated Comment: {self.awards.project_name} {self.award_name}"
        html_content = '<h4>Updated Comment 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly."
        text_content = 'We have updated a draft for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly." 
        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content        
        message.to.add(['aaron.weisberg@virtuouscirclemedia.com'])
        message.send()


    def updated_script(self):
        team_email = self.awards.organization.team_email
        #emaillist = list(set(team_email[0],team_email[1],team_email[3]))
        subject = f"Updated Script added for video: {self.awards.project_name} {self.award_name}"
        html_content = '<h4>We have updated a script for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly." 
        text_content = 'We have updated a script for video: 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'f"Please be sure to comment or email us directly." 

        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content        
        message.to.add([team_email])
        message.send()

    def created_message(self):
        team_email = self.awards.organization.team_email
        emaillist = list(set([team_email[0],team_email[1],team_email[2]]))
        subject = f"New Award added to {self.awards.project_name}"
        html_content = '<h4>Thank you for adding 'f"{self.award_name}"' to the production portal. You can view all updates to this video and make any changes here: <a href="http://www.virtuous-circle.com/'f"org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"'">'f"{self.award_name}"'</a></h4>'        
        text_content = f"Thank you for adding {self.award_name} to the production portal. You can view the progress and make changes to the project at http://www.virtuous-circle/org/{self.awards.organization.id}/awards/{self.awards.id}/award/{self.id}"
        credentials=(settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        account = Account(credentials)
        message = account.new_message()
        message.subject = subject
        message.body = html_content        
        message.to.add([emaillist])
        message.send()       
       


@receiver(post_save, sender=Award)
def update_award(sender, instance, **kwargs):
    #instance.created_message()    
    if instance.folder_id is None:
        gd = GoogleDriveApi()
        folder_id = gd.createFolder(instance.award_name, instance.awards.folder_id)
        instance.folder_id = folder_id
        instance.save()

class Comment(models.Model):
    PROCESS_STEPS = (
            ('Script Rough Draft','rough_script'),
            ('Script Final Draft','final_script'),
            ('Video Rough Draft','video_rough'),
            ('Video Final Draft', 'final_video'),
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
    process_comment = models.CharField(max_length=200,choices=PROCESS_STEPS,null=True)
    info = JSONField()


    def send_comment(self):
        print('sending comment!')
        credentials = (settings.EMAIL_CLIENT,settings.EMAIL_SECRET)
        subject = 'New Comment'
        body = f"From: {self.user.username}"
        body += '\n'f"Message: {self.comment}"
        body += '\n'f"{self.info}"
        account = Account(credentials)
        message= account.new_message()
        message.body = body
        message.to.add([User.objects.get(pk=1).email])
        message.subject = 'New comment'
        message.send()



class File(models.Model):
    award = models.ForeignKey(Award,on_delete=models.CASCADE,blank=True,null=True)
    file_name = models.CharField(max_length=2000,null=True,blank=True)
    on_drive = models.BooleanField(default=False,null=True,blank=True)
    file = models.FileField(upload_to='project/%Y/%m/%d',blank=True,null=True)
    def __str__(self):
        return f"{self.award} {self.file_name}"
    @property
    def filename(self):
        name = self.file.name.split("/")[-1].replace('_',' ').replace('-',' ')
        return name
    def get_absolute_url(self):
     return reverse('project:index')

@receiver(pre_save,sender=Award)
def video_update(sender,instance,**kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        print('new file')
    else:
        if not obj.draft == instance.draft and instance.draft !='#' and instance.draft is not None:
            obj.updated_draft()
        if not obj.script == instance.script and instance.script != '#' and instance.script is not None:
            obj.updated_script()
        if not obj.final_draft == instance.final_draft and instance.final_draft !='#' and instance.final_draft is not None:
            obj.updated_final()
        

@receiver(post_save, sender=File)
def upload_file(sender, instance, **kwargs):
    import mimetypes
    gd = GoogleDriveApi()
    gd.uploadFile(instance.filename, instance.file.url, instance.award.folder_id,mimetypes.guess_type(instance.filename)[0])
    #uploadFile(self, name, file_path, mimetype, folder_name=None):

@receiver(post_save,sender=Comment)
def comment_added(sender,instance,**kwargs):
    print('post save biz')
    instance.send_comment()


    
    
'''
@receiver(post_save, sender=File)
def upload_file(sender, instance, **kwargs):
    if instance.on_drive is False:
        gd = GoogleDriveApi()
        #folder_id = gd.createFolder(instance.file_name, instance.award.folder_id)
        instance.folder_id = folder_id
        instance.save()


def uploadFile(self, name, file_path, mimetype, folder_name=None):
        file_metadata = {'name': name}
        if folder_name:
            folder_id = self.createFolder(folder_name)
            file_metadata = {'name': name, 'parents': [folder_id]}
        media = MediaFileUpload(file_path, mimetype=mimetype)
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
'''

