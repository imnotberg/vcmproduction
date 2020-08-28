from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from .views import *
from .forms import *

app_name = 'project'

urlpatterns = [
	path('',auth_views.LoginView.as_view(template_name='project/login.html',redirect_authenticated_user=True),name='no_page'),
	path('register/',views.register,name='register'),
	path('index/',views.index,name='index'),
	path('login/', auth_views.LoginView.as_view(template_name='project/login.html'),name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name='logout'),
	path('org/<pk>',views.OrganizationDetailView.as_view(),name='organization_detail'),
	path('partner/<pk>',views.PartnerProjectList.as_view(),name='partner_projects'),
	path('partner/<partner_id>/project/<project_id>',views.ProjectOverview.as_view(),name='project_overview'),
	path('partner/<partner_id>/project/<project_id>/video/<pk>',views.VideoDetailView.as_view(),name='video_detail'),
	path('partner/<partner_id>/project/<project_id>/video/add/',views.AwardFormView.as_view(),name='video_create'),
	path('partner/<partner_id>/project/add/',views.ProjectCreateView.as_view(),name='project_create'),
	path('partner/<partner_id>/project/<project_id>/video/<pk>/edit',views.VideoUpdateView.as_view(),name='video_edit'),
	path('partner/<partner_id>/project/<pk>/edit',views.ProjectUpdateView.as_view(),name='project_edit'),
	path('promotion/add',PromotionFormView.as_view(),name='promotion_add'),
	path('partner/<partner_id>/promotion/<pk>',PromotionDetailView.as_view(),name='promotion_detail'),
	path('get/type/<project_type>/project_id/<project_id>',views.get_project,name='get_project'),
	path('org/<org_id>/message_create',views.message_create,name='message_create'),
	path('org/<org_id>/message/<pk>',views.MessageDetailView.as_view(),name='message_detail'),
	path('org/<org_id>/awards-create',views.AwardsCreateView.as_view(),name='awards_create'),
	path('org/<org_id>/awards/<pk>',views.AwardsDetailView.as_view(),name='awards_detail'),
	path('org/<org_id>/awards/<pk>/edit',views.AwardsUpdateView.as_view(),name='awards_update'),
	path('org/<org_id>/awards/<awards_id>/award/add/',views.AwardFormView.as_view(),name='award_create'),
	path('org/<org_id>/awards/<awards_id>/award/<pk>',views.AwardDetailView.as_view(),name='award_detail'),
	path('org/<org_id>/awards/<awards_id>/award/<pk>/edit',views.AwardUpdateView.as_view(),name='award_edit'),
	path('password_change_done',views.password_change_done,name='password_change_done'),

	#path('org/<org_id>/awards/<awards_id>/award/<award_id>/upload/',views.FileUpload.as_view(),name='upload_form'),
	path('uploads/simple/', views.model_form_upload, name='simple_upload'),
	path('org/<org_id>/awards/<awards_id>/award/<award_id>/upload',views.test_upload,name='test_upload'),
	path('org/<org_id>/awards/<awards_id>/award/<award_id>/upload-files',views.upload_file,name='upload_file'),
	path('org/<org_id>/awards/<awards_id>/award/<award_id>/comment',views.comment_view,name='comment_view'),
	path('password-change',auth_views.PasswordChangeView.as_view(template_name='project/password_change_form.html'),name='password_change'),
	path('email',views.email,name='email'),
	path('comments-update',views.comments_update,name='comments-update'),
	]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)