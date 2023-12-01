from django.db import models

# Create your models here.
class Funcoes(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    funcao = models.ForeignKey(Funcoes,on_delete=models.CASCADE)
    pais_de_origem = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.funcao} {self.pais_de_origem}'

class Banda(models.Model):
    nome = models.CharField(max_length=50)
    pais_de_origem = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.pais_de_origem}'

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome



class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nome} {self.email} {self.login}'

class Biagrafia(models.Model):
    historia = models.CharField(max_length=2000)
    banda = models.ForeignKey(Banda,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.historia} {self.banda}'
class Album(models.Model):
    nome = models.CharField(max_length=50)
    banda = models.ForeignKey(Banda,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.banda}' 

class Musica(models.Model):
    nome = models.CharField(max_length=50)
    letra_da_musica = models.CharField(max_length=2000)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE)
    interprete = models.ForeignKey(Pessoa,related_name='interprete',on_delete=models.CASCADE)
    compositor = models.ForeignKey(Pessoa,related_name='compositor',on_delete=models.CASCADE)
    ano_de_lancamento = models.CharField(max_length=50)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.nome} {self.letra_da_musica} {self.genero} {self.interprete} {self.compositor} {self.ano_de_lancamento}'
    
class apresentacao(models.Model):
    nome = models.CharField(max_length=50)
    interprete = models.CharField(max_length=2000)
    nome_da_musica = models.ForeignKey(Musica,on_delete=models.CASCADE)
    data_de_apresentacao = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.interprete} {self.nome_da_musica} {self.data_de_apresentacao}'