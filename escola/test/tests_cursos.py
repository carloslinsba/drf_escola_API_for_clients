from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse ('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', descricao = 'Curso_teste 1', nivel= 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT2', descricao = 'Curso_teste 2', nivel= 'I'
        ) 

    def test_requisicao_get_para_listar_cursos(self):
        """testing get response"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_criar_cursos(self):
        """testing post and its response"""
        data = {
            'codigo_curso': 'CTT3P',
            'descricao': 'Curso teste Post',
            'nivel': 'A'
        }
        
        response = self.client.post(self.list_url, data = data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
    
    def test_requisicao_put_para_atualizar_cursos(self):
        """testing put and its response and update"""
        data = {

            'codigo_curso': 'CTT3PN',
            'descricao': 'Curso teste Post Atualizado',
            'nivel': 'A'
        }
        
        response = self.client.put('/cursos/1/', data = data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        def test_requisicao_delete_para_deletar_cursos(self):
            """testing delete not permitted and its response"""
            response = self.client.delete('/cursos/1/')
            self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
            
    