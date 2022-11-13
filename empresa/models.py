from django.db import models



class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia


class Empresa(models.Model):
    choices_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design'),
        ('T', 'Tecnologia'),
        ('E', 'Eletrônicos'),
        ('C', 'Cosméticos'),
        ('D', 'Design'), 
        ('B', 'Bebidas'),
        ('G', 'Games'),
        ('F', 'Financeiro')
    )

    logo = models.ImageField(upload_to="logo_empresa")
    nome = models.CharField(max_length=45)
    email = models.EmailField(null=True)
    cidade = models.CharField(max_length=30)
    tecnologias = models.ManyToManyField(Tecnologias)
    endereco = models.CharField(max_length=80)
    nicho_mercado = models.CharField(max_length=10, choices=choices_nicho_mercado)
    caracteristica_empresa = models.TextField()

    def __str__(self):
        return self.nome

    def qtd_vagas(self):
        return Vagas.objects.filter(empresa__id=self.id).count()


class Vagas(models.Model):

    choices_experiencia = (
        ('E', 'Estágio'),
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('R', 'Aguardando retorno'),
        ('F', 'Finalizado'),
        ('T', 'Trabalhando')
    )
    
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField(max_length=68)
    nivel_experiencia = models.CharField(max_length=2, choices=choices_experiencia)
    data_final = models.DateField()
    status = models.CharField(max_length=30, choices=choices_status)
    tecnologias_dominadas = models.ManyToManyField(Tecnologias)
    tecnologias_estudar = models.ManyToManyField(Tecnologias, related_name='estudar')

    def __str__(self):
        return self.titulo

