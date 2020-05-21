from django import template
from project.models import Video,Client,Awards,Award
import re

register = template.Library()

@register.filter
def video_list(value):
	return Award.objects.filter(awards=value)
	
@register.filter
def prt(value):
	print(value)
@register.filter
def name(value):
	print(value,'valeu')
	try:
		if value.type == 'awards':
			print('right here')
			return value.project_name
		elif value.type == 'promotion':
			return value.name
		elif value.type == 'message':
			return value.name
		elif value.type == 'award':
			return value.award_name
	except:
		return ''
@register.filter
def number(value):
	pass
@register.filter
def count(value):
	return len(value)
@register.filter
def client(value):
	return Client.objects.get(user_id=value).pk
@register.filter
def driveify(value):
	print(value)
	try:		
		slug = slug = re.findall('id=(.+)',value)[0]
		url = f"https://docs.google.com/file/d/{slug}/preview?usp=drivesdk"
		return url
	except:
		print('no slug')
		return "#"
@register.filter
def folderfy(value):
	try:
		slug = re.findall('id=(.+)',value)[0]
		url = f"https://drive.google.com/embeddedfolderview?id={slug}#list"
		return url
	except:
		return "#"
@register.filter
def vidify(value):
	print('cididd')
	#https://drive.google.com/file/d/1ARSiQ4zKy7Iu2MvrYEhViPBozI2GqJR3/view?usp=sharing
	try:
		slug = re.findall('id=(.+)',value)[0]
		print(slug)
		return slug
	except:
		return '#'








