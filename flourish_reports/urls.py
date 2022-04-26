"""flourish_reports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .admin_site import flourish_reports_admin
from .views import (
    EnrolmentReportView, RecruitmentReportView, DownloadReportView)


app_name = 'flourish_reports'

urlpatterns = [
    path('admin/', flourish_reports_admin.urls),
    path('recruitment', RecruitmentReportView.as_view(), name='recruitment_report_url'),
    path('download', DownloadReportView.as_view(), name='download_report_url'),
    path('enrolment', EnrolmentReportView.as_view(), name='enrolment_report_url'),
]
