from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django import forms
from django.views.generic.list import ListView
from datetime import datetime
from formtools.wizard.views import SessionWizardView
from rest_framework import viewsets
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .serializers import *
# from pandas import DataFrame as df
# import pandas as pd
from .forms import *
from .models import *
from . import constants
import json
import mimetypes
import logging
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




# Create your views here.


def index(request):
    try:
        client = Client.objects.get(user=request.user)
        organization = client.organization
        return redirect(organization)
    except:
        return redirect('/login/')


def register(request):
    context = {'form': CreateUserForm, }
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            u = form.save(commit=False)
            profile = Client(user=u)
            u.save()
            profile.save()
            login(request, u)
            return redirect('project:index')

    return render(request, 'project/register.html', context)


@method_decorator(login_required, name='dispatch')
class PartnerProjectList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(id=self.kwargs['pk'])
        context['project_list'] = Project.objects.filter(client=client)
        context['project_count'] = Project.objects.filter(client=client).count()
        context['partner'] = client

        return context


@method_decorator(login_required, name='dispatch')
class ProjectOverview(ListView):
    model = Video
    template_name = 'project/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['project_id'])
        client = Client.objects.get(id=self.kwargs['partner_id'])
        video_list = Video.objects.filter(project=project)
        context['project'] = project
        context['partner'] = client
        context['video_list'] = video_list

        return context


@method_decorator(login_required, name='dispatch')
class VideoDetailView(DetailView):
    model = Video

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = Video.objects.get(id=self.kwargs['pk'])
        partner = Client.objects.get(id=self.kwargs['partner_id'])
        project = Project.objects.get(id=self.kwargs['project_id'])
        context['video'], context['project'], context['partner'] = video, partner, project
        return context


@method_decorator(login_required, name='dispatch')
class VideoCreateView(CreateView):
    model = Video
    fields = ['award_number', 'award_name', 'award_description', 'award_winner', 'award_comments']

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['project'] = Project.objects.get(id=self.kwargs['project_id'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(pk=self.kwargs['project_id'])
        context['project'] = project
        return context

    def form_valid(self, form):
        data = self.get_initial()
        instance = form.save(commit=False)
        instance.project = data['project']
        instance.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProjectCreateView(CreateView):    
    model = Project   
    form_class = ProjectForm


    # fields = ['project_name','date','number_of_awards']

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['partner'] = Client.objects.get(id=self.kwargs['partner_id'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        partner = Client.objects.get(pk=self.kwargs['partner_id'])
        context['partner'] = partner
        return context

    def form_valid(self, form):
        data = self.get_initial()
        instance = form.save(commit=False)
        instance.client = data['partner']
        instance.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class VideoUpdateView(UpdateView):
    model = Video
    fields = ['award_number', 'award_name', 'award_description', 'award_winner', 'award_comments']


@method_decorator(login_required, name='dispatch')
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm


# fields = ['project_name','date','number_of_awards']
@method_decorator(login_required, name='dispatch')
class PromotionFormView(SessionWizardView):
    template_name = 'project/promotion_form.html'
    # form_list = [PromotionForm1,PromotionForm2,PromotionForm3,PromotionForm4,PromotionForm5]
    form_list = [PromotionForm2, PromotionForm3, PromotionForm4, PromotionForm5, PromotionForm6, PromotionForm7]

    def get_form_initial(self, step):
        client = Client.objects.get(user=self.request.user)
        initial_dict = {'0': {'organization': client.user.username, 'email': client.user.email, }, '1': {}, '2': {},
                        '3': {}, '4': {}, '5': {}, }
        return self.initial_dict.get(step, {})

    def done(self, form_list, **kwargs):
        fd = [form.cleaned_data for form in form_list]
        form_data = {k: v for list_item in fd for (k, v) in list_item.items()}
        client = Client.objects.get(user=self.request.user)
        p = Promotion(client=Client.objects.get(user=self.request.user), name=form_data['name'],
                      venue=form_data['venue'], date=form_data['date'], city=form_data['city'],
                      state=form_data['state'], theme=form_data['theme'], logo=form_data['logo'],
                      target_audience=''.join([str(x) for x in form_data['target_audience']]),
                      attendees=form_data['attendees'], exhibitors=form_data['exhibitors'],
                      feature_1=form_data['feature_1'], feature_4=form_data['feature_4'],
                      feature_2=form_data['feature_2'], feature_3=form_data['feature_3'],
                      feature_5=form_data['feature_5'], guests=form_data['guests'], assets=form_data['assets'])
        
        p.save()
        return HttpResponseRedirect(reverse('project:promotion_detail', kwargs={'partner_id': client.pk, 'pk': p.pk}))

    # return render(h.request, 'project/done.html', {'form_data': [form.cleaned_data for form in form_list],})
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class PromotionDetailView(DetailView):
    model = Promotion

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        client = Client.objects.get(user=self.kwargs['partner_id'])
        context['client'] = client
        return context
@method_decorator(login_required, name='dispatch')
class OrganizationDetailView(DetailView):
    model = Organization

    def get_object(self,queryset=None):
        obj = super(OrganizationDetailView, self).get_object()

        if Client.objects.get(user=self.request.user).organization != obj and self.request.user.id != 1:
            obj = Client.objects.get(user=self.request.user).organization     
            return obj
        return obj

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['pk']=='1':            
            context['projects'] = [x for x in Awards.objects.filter(active=True)] + [y for y in Promotion.objects.all()] + [z for z in Message.objects.all()]            
        return context




@login_required
def get_project(request, project_type, project_id):
    if project_type == 'awards':
        return redirect(Awards.objects.get(pk=project_id))
    elif project_type == 'promotion':
        return redirect(Promotion.objects.get(pk=project_id))
    elif project_type == 'message':
        return redirect(Message.objects.get(pk=project_id))


@method_decorator(login_required, name='dispatch')
class AwardFormView(SessionWizardView):
    template_name = 'project/award_form.html'
    form_list = [AwardForm1, AwardForm2, AwardForm3, AwardForm4]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization = Organization.objects.get(pk=self.kwargs['org_id'])        
        context['org'] = organization
        context['project'] = Awards.objects.get(pk=self.kwargs['awards_id'])
        return context
    def get(self, request, *args, **kwargs):
        awards_id = kwargs['awards_id']
        project = Awards.objects.get(pk=awards_id)

        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        fd = [form.cleaned_data for form in form_list]
        form_data = {k: v for list_item in fd for (k, v) in list_item.items()}
        awards_id = kwargs['awards_id']
        awards = Awards.objects.get(id=awards_id)
        organization = awards.organization
        v = Award(awards=awards, award_number=form_data['award_number'], award_name=form_data['award_name'],
                  award_description=form_data['award_description'], award_winner=form_data['award_winner'],
                  award_comments=form_data['award_comments'], award_project=form_data['award_project'])
        v.save()
        v.created_message()
        return HttpResponseRedirect(reverse('project:award_detail',
                                            kwargs={'org_id': organization.id, 'awards_id': awards_id,
                                                    'pk': v.pk}))


@login_required
def message_create(request, org_id):
    if request.method == 'POST':
        form = MessageCreateForm(request.POST)
        if form.is_valid():
            notes = {'reps': form.cleaned_data['representatives'], 'theme': form.cleaned_data['theme'],
                     'message': form.cleaned_data['message'], }

            jnotes = json.dumps(notes)
            organization = Organization.objects.get(pk=org_id)
            message = Message(organization=organization, name=form.cleaned_data['name'], date=form.cleaned_data['date'])
            message.notes = json.loads(jnotes)
            message.organization = organization
            message.save()

            return HttpResponseRedirect(
                reverse('project:message_detail', kwargs={'org_id': org_id, 'pk': message.pk}))
    else:
        form = MessageCreateForm()
        organization = Organization.objects.get(pk=org_id)

    return render(request, 'project/message_create.html', {'form': form, 'org': organization,})


@method_decorator(login_required, name='dispatch')
class MessageDetailView(DetailView):
    model = Message
@method_decorator(login_required,name='dispatch')
class AwardsUpdateView(UpdateView):
    model = Awards 
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization = Organization.objects.get(pk=self.kwargs['org_id'])        
        context['organization'] = organization
        return context
    def form_valid(self, form):        
        context = self.get_context_data()
        
        instance = form.save(commit=False)
        instance.organization = context['organization']
        instance.created_message()
        instance.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class AwardsCreateView(CreateView):    
    model = Awards   
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        organization = Organization.objects.get(pk=self.kwargs['org_id'])        
        context['organization'] = organization
        return context
    def form_valid(self, form):        
        context = self.get_context_data()
        
        instance = form.save(commit=False)
        instance.organization = context['organization']
        instance.created_message()
        instance.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class AwardsDetailView(DetailView):
    model = Awards
    template_name = 'project/awards_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  


        return context
@method_decorator(login_required, name='dispatch')
class AwardDetailView(DetailView):
    model = Award
    template_name = 'project/award_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['form']=CommentForm
        context['upload_form'] = FileForm
        print(context['upload_form'])   

        return context
@method_decorator(login_required, name='dispatch')
class AwardUpdateView(UpdateView):
    model = Award
    template_name = 'project/award_update_form.html'
    fields = ['award_number', 'award_name', 'award_description', 'award_winner', 'award_project','award_comments']
    widgets = {
        'award_winner':forms.Textarea
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)       
        context['org'] = Organization.objects.get(pk=self.kwargs['org_id'])
        context['project'] = Awards.objects.get(pk=self.kwargs['awards_id'])
        context['award'] = Award.objects.get(pk=self.kwargs['pk'])
        return context

class FileUpload(CreateView):
    model = File
    form_class = FileForm
    def form_valid(self,form):
        obj = form.save(commit=False)
        print('obje',obj)
        if self.request.FILES:
            for f in self.request.FILES.getlist('file'):
                obj = self.model.objects.create(file=f)
                print('obj',obj)
        return super(FileUpload,self).form_valid(form)


def model_form_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():            
            form.save()

    else:
        form = FileForm()
    return render(request, 'project/model_form_upload.html', {
        'form': form})
def upload_file(request,org_id,awards_id,award_id):
    if request.method == 'POST':
        award = Award.objects.get(pk=award_id)
        for _file in request.FILES.getlist('file'):
            request.FILES['file'] = _file
            form = FileForm(request.POST,request.FILES)
            if form.is_valid():
                _new = form.save(commit=False)
                _new.award = award
                _new.save()
        return redirect(Award.objects.get(pk=award_id))
def test_upload(request,org_id,awards_id,award_id):
    if request.method == 'POST':
        award = Award.objects.get(pk=award_id)
        #form = FileForm(request.POST,request.FILES)
        for _file in request.FILES.getlist('file'):
            request.FILES['file'] = _file
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                _new = form.save(commit=False)
                _new.award = award
                _new.save()
                
        '''
        if form.is_valid:            
            instance = File(file=request.FILES['file'],award=award)
            print(instance.award,'IIIIII')
            instance.save()
        '''
            
    else:
        form = FileForm()
    return render(request,'project/test_upload.html',{'form':form,})
def comment_view(request,org_id,awards_id,award_id):
    if request.method == 'POST':
        user = request.user
        form = CommentForm(request.POST)
        award = Award.objects.get(pk=award_id)
        if form.is_valid():
            add = {request.POST['block']:request.POST['comment'],}
            if award.edit_comments is not None:
                old = award.edit_comments
                new = old.update(add)
                award.edit_comments = json.dumps(new)
                award.save()
            else:
                comment = {request.POST['block']:request.POST['comment'],}
                jcomment = json.dumps(comment)
                award.edit_comments = json.loads(jcomment)
                award.save()


        return redirect(award)
def password_change_done(request):
    return redirect('project:index')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class AwardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Awards.objects.all().order_by('pk')
    serializer_class = AwardsSerializer
def email(request):
    sg = SendGridAPIClient(settings.SENDGRID_API_KEY)  
    subject = 'This is a test email' 
    text_content = 'This is text content'
    html_content = '<strong>This is html content</strong>'
    message = Mail(from_email=settings.DEFAULT_SEND_GRID_EMAIL,to_emails=['aaron.m.weisberg@gmail.com'],subject=subject,plain_text_content=text_content,html_content=html_content)
    response = sg.send(message)


    return redirect('project:index')

