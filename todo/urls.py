from django.urls import path
from .views import DashboardView, BoardDetailView, CreateTaskView, MoveCardView, ExportProjectReportView, CustomLogoutView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('project/<str:project_id>/', BoardDetailView.as_view(), name='board_detail'),
    path('project/<str:project_id>/create-task/', CreateTaskView.as_view(), name='create_task'),
    path('card/move/', MoveCardView.as_view(), name='move_card'),
    path('project/<str:project_id>/export/', ExportProjectReportView.as_view(), name='export_project_report'),
    
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]