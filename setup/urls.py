
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('aluno/<int:pk>/matricula/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matricula/', ListaAlunosMatriculados.as_view())

]+static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
