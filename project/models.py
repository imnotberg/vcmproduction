import hashlib, random, sys
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.db import models
from . import constants


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
        team_members = Client.objects.filter(organization=self)
        return team_members
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
        return [a for a in self.awards] + [p for p in self.promotion] + [c for c in self.message]

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

    def get_object(self,queryset=None):
        obj = super(PostDetailView, self).get_object()
        if not obj.owner == self.request.user:
            print('you shall not pass')
        return obj


    def __str__(self):
        return f"{self.organization.name} {self.project_name} {self.date.year}"

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
    if instance.folder_id is None:
        gd = GoogleDriveApi()
        instance.folder_id = gd.createFolder(instance.project_name)
        instance.save()

class Award(models.Model):
    awards = models.ForeignKey(Awards, on_delete=models.CASCADE)
    award_number = models.PositiveSmallIntegerField()
    award_name = models.CharField(max_length=200000)
    award_description = models.TextField(blank=True,null=True)
    award_winner = models.CharField(max_length=2000)
    award_project = models.CharField(max_length=2000,null=True,blank=True)
    award_comments = models.TextField()
    award_assets = models.URLField(null=True, blank=True, default='#')
    script = models.URLField(null=True, blank=True, default='#')
    draft = models.URLField(null=True, blank=True, default='#')
    final_draft = models.URLField(null=True, blank=True, default='#')
    edit_comments = JSONField(null=True,blank=True)
    folder_id = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.awards.organization.name} {self.awards.project_name} {str(self.award_number)} {self.award_name}"

    def get_absolute_url(self):
        return reverse('project:award_detail',
                       kwargs={'pk': self.pk, 'org_id': self.awards.organization.id, 'awards_id': self.awards.id})


@receiver(post_save, sender=Award)
def update_award(sender, instance, **kwargs):
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
