from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.text import slugify


class MyUserManager(BaseUserManager):
    def create_user(self, phone,email=None, fullname=None,password=None):

        if not phone:
            raise ValueError("Users must have an phone address")

        user = self.model(phone=phone, fullname=fullname, email=email)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, fullname, password=None):

        user = self.create_user(phone,password=password,fullname=fullname)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="آدرس ایمیل",max_length=255,null=True,blank=True)
    phone = models.CharField(verbose_name="شماره تلفن",max_length=11,unique=True,)
    profile = models.ImageField(null=True,blank=True, upload_to='profile')
    fullname = models.CharField(null=True, blank=True, verbose_name="نام کامل",max_length=255)
    user_id = models.CharField(null=True, blank=True, max_length=255, unique=True)
    bio = models.TextField(null=True,blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    is_admin = models.BooleanField(default=False,verbose_name='ادمین')

    objects = MyUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['fullname']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.phone

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)  # می‌توانید هر استراتژی برای تولید slug استفاده کنید
        super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Otp(models.Model):
    token = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=11)
    fullname = models.CharField(max_length=150,default='unknown')
    email = models.EmailField(null=True,blank=True)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.phone

    class Meta:
        unique_together = ['phone', 'code']






class OtpCode(models.Model):
    code = models.SmallIntegerField()
    token = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.phone

    class Meta:
        unique_together = ['phone', 'code']


class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='addresses')
    fullname = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField(null=True,blank=True)
    postal_code = models.CharField(max_length=11)

    def __str__(self):
        return self.address