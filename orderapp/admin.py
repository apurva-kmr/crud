from django.contrib import admin
from orderapp.models import Login,Coustumer
#from orderapp.models import Coustumer
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display=['Coustumer_id','Email_id','Pass','Attempts','Locked']

class CoustumerAdmin(admin.ModelAdmin):
    list_display=['Transaction_ID','Customer_ID','Transdate','Cfname','Clname','Country','Ccity','Product','Qty','Amount']

admin.site.register(Login,LoginAdmin)
admin.site.register(Coustumer,CoustumerAdmin)
