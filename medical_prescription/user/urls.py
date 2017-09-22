from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^$', views.show_homepage, name='home'),

    url(r'^register_health_professional/$', views.register_health_professional, name='register health professional'),
    url(r'^view_health_professional/$', views.view_health_professional, name='view health professional'),
    url(r'^edit_health_professional/(?P<pk>[0-9]+)/$',
        views.UpdateHealthProfessional.as_view(), name='edit health professional'),
    url(r'^delete_health_professional/(?P<pk>[0-9]+)/$',
        views.DeleteHealthProfessional.as_view(), name='delete health professional'),

    url(r'^register_patient/$', views.register_patient, name='register patient'),
    url(r'^view_patient/$', views.view_patient, name='view patient'),
    url(r'^edit_patient/(?P<pk>[0-9]+)/$', views.UpdatePatient.as_view(), name='edit patient'),
    url(r'^delete_patient/(?P<pk>[0-9]+)/$',
        views.DeletePatient.as_view(), name='delete patient'),
)
