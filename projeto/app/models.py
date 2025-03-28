from django.db import models
from django.contrib.auth.models import  BaseUserManager,AbstractUser, PermissionsMixin, AbstractBaseUser
import datetime

# Create your models here.

class Produto(models.Model):
    idproduto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False)
    preco = models.FloatField(null=False)
    descricao = models.CharField(max_length=255,null=False)
    quantidade = models.IntegerField(null=False)
    controlado = models.CharField(max_length=30, null=False)
    is_active = models.BooleanField(default=True)

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=16,null=False,primary_key=True)
    telefone = models.CharField(max_length=30, null=False)
    nomeEmpresa = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=False)
    numero = models.IntegerField(null=False)

class SaidaMercadoria(models.Model):
    idsaida = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    datacompra = models.DateField(default=datetime.date.today)
    idproduto = models.ForeignKey(Produto,to_field='idproduto',on_delete=models.CASCADE,null=True)

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    telefone = models.IntegerField( null=False)
    sobrenome = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=18)
    email = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    numero = models.IntegerField()
    is_active = models.BooleanField(default=True)

class RecebimentoMercadoria(models.Model):
    idrecebeu = models.AutoField(primary_key=True)
    datarecebeu = models.DateField(default=datetime.date.today)
    totalproduto = models.IntegerField()
    notaFiscal = models.IntegerField()
    cnpj = models.ForeignKey(Fornecedor,to_field='cnpj',on_delete=models.CASCADE,null=True)
    idproduto = models.ForeignKey(Produto,to_field='idproduto',on_delete=models.CASCADE,null=True)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    date_joined = models.DateField(default=datetime.date.today)
    email = models.EmailField(blank=True,unique=True ,null=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password']  # Aqui você define os campos obrigatórios

    def __str__(self):
        return self.email

class Devolucao(models.Model):
    id = models.AutoField(primary_key=True)
    quantidade = models.IntegerField(null=False)
    motivo = models.CharField(max_length=11, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    idproduto = models.ForeignKey(Produto,to_field='idproduto',on_delete=models.CASCADE,null=True)

class Fatura(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    codigoDeBarra = models.CharField(max_length=50, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

class Pagamento(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    formaDePagamento = models.CharField(max_length=50)
    codigoDeBarraFatura = models.ForeignKey(Fatura, to_field='codigoDeBarra', on_delete=models.CASCADE, null=False)

class Financas(models.Model):
    id = models.AutoField(primary_key=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fatura = models.ManyToManyField(Fatura)
    pagamento = models.ManyToManyField(Pagamento)


class NotaFiscal(models.Model):
    cnpj_emitente = models.CharField(max_length=14)
    cnpj_destinatario = models.CharField(max_length=14)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_emissao = models.DateTimeField(auto_now_add=True)
    chave_nfe = models.CharField(max_length=44, unique=True)
    status = models.CharField(max_length=20)

""" 
inserir no banco de dados

insert into app_usuario(username,password,is_active,is_staff,is_superuser,first_name,last_name,date_joined,email) values('kaua','123',True,False,False,'kaua','silva','2024-02-25','teste123@gmail.com')
"""