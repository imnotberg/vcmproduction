from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from project.models import Client, Project, Video,Awards,File


class ProjectForm(ModelForm):
    class Meta:
        model = Awards
        fields = ['project_name', 'date', 'number_of_awards']
        widgets = {'date': forms.SelectDateWidget()}


class Video(ModelForm):
    class Meta:
        model = Video
        fields = '__all__'


class PromotionForm1(forms.Form):
    organization = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()


class PromotionForm2(forms.Form):
    name = forms.CharField(max_length=200, label='Name', help_text='Name of Event')
    date = forms.DateField(widget=forms.SelectDateWidget, label='Date', help_text='Event Start Date')
    venue = forms.CharField(max_length=100, label='Venue')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=2, label='State')


class PromotionForm3(forms.Form):
    theme = forms.CharField(widget=forms.TextInput, label='Theme', help_text='What is the theme of your event?')
    guests = forms.CharField(widget=forms.TextInput, label='Guests', required=False,
                             help_text='List any keynote speakers or special guests. Separate by commas')


class PromotionForm4(forms.Form):
    TARGET_AUDIENCE = [('attendees', 'Attendees'), ('exhibitors', 'Exhibitors'), ('sponsors', 'Sponsors')]
    target_audience = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TARGET_AUDIENCE,
                                                label='Target Audience',
                                                help_text='Whom are you trying to attract? (Pick all that apply)')


class PromotionForm7(forms.Form):
    logo = forms.URLField(label='Event Logo', help_text='Link to event logo', required=False)
    assets = forms.URLField(label='Pictures/Videos', help_text='Link to assets', required=False)


class PromotionForm5(forms.Form):
    attendees = forms.IntegerField(min_value=0)
    exhibitors = forms.IntegerField(min_value=0)


class PromotionForm6(forms.Form):
    feature_1 = forms.CharField(max_length=20000, widget=forms.TextInput,
                                error_messages={'required': 'Please enter one feature'})
    feature_2 = forms.CharField(required=False, max_length=20000, widget=forms.TextInput)
    feature_3 = forms.CharField(required=False, max_length=20000, widget=forms.TextInput)
    feature_4 = forms.CharField(required=False, max_length=20000, widget=forms.TextInput)
    feature_5 = forms.CharField(required=False, max_length=20000, widget=forms.TextInput)


class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField()


class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100)
    salary = forms.CharField(max_length=100)
    job_description = forms.CharField(widget=forms.Textarea)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class AwardForm1(forms.Form):
    award_number = forms.IntegerField(min_value=1, max_value=100, label='Award Number',required=False)
    award_name = forms.CharField(max_length=200, label='Award Name')


class AwardForm2(forms.Form):
    award_description = forms.CharField(max_length=20000, widget=forms.Textarea,
                                        help_text='What are the values represented by the award', required=False,
                                        label='Award Description')


class AwardForm3(forms.Form):
    award_winner = forms.CharField(max_length=2000, label='Award Winner',widget=forms.Textarea,help_text='Winner or Winners separated by comma')
    award_project = forms.CharField(max_length=2000,label='Winning Project',widget=forms.Textarea,help_text='Name of Project',required=False)


class AwardForm4(forms.Form):
    award_comments = forms.CharField(max_length=20000, label='Jury Comments', widget=forms.Textarea,required=False)
    


class AwardForm5(forms.Form):
    award_assets = forms.URLField(required=False, label='Assets',
                                  help_text='Folder URL for videos,pictures and graphics')
    #award_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class MessageCreateForm(forms.Form):
    name = forms.CharField(label='Video Title', help_text='Name your video message', required=False)
    representatives = forms.CharField(widget=forms.Textarea, label='Organization Representatives',
                                      help_text='Leader or leaders who will apper in video separated by comma',
                                      required=False)
    date = forms.DateField(label='Release Date', help_text='Ideal date for distribution', widget=forms.DateTimeInput,
                           required=False)
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    theme = forms.CharField(label='Video Theme', help_text='Overall theme for your video', widget=forms.Textarea,
                            required=False)
    message = forms.CharField(label='Video Message',
                              help_text='Let us know what you want to communicate, and we will work on a draft script',
                              widget=forms.Textarea)

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']
        help_text = {'file':'Select One, Multiple files or One Folder to the project'}
        widgets = {'file':forms.ClearableFileInput(attrs={'multiple':True})}
class CommentForm(forms.Form):
    block = forms.IntegerField(required=False,widget=forms.NumberInput,min_value=1,help_text='Please enter the script-block the comment pertains',label='Script Block')
    comment_type = forms.ChoiceField(required=False,choices=(('',''),('Script','Script'),('Draft','Draft'),('Final','Final'),('General','General')),label='Comment Type')
    time = forms.CharField(required=False,help_text='Time of video for comment')
    comment = forms.CharField(required=True,widget=forms.Textarea)






    
















