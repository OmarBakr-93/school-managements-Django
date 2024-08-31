from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
     path('',include('attendence.urls'),name='attendence'),
    path('',include('marksheet.urls'), name='marksheet'),
    path('',include('user.urls'),name='user'),
    path('',include('Fee.urls'),name='Fee'),
    path('',include('event.urls'),name='event'),
    path('',include('games.urls'),name='games'),
    path('',include('student_parent.urls'),name='student_parent'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
