from django.db import models

# Create your models here.


class Company(models.Model):
    """Model definition for Company."""

    companyname = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companys'

    def __str__(self):
        """Unicode representation of Company."""
        return '%s: %s' % (self.companyname, self.city)


class Employee(models.Model):
    """Model definition for Employee."""

    # TODO: Define fields here

    username = models.CharField(max_length=50)
    company = models.ForeignKey('Company', related_name='companies', on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Employee."""

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        """Unicode representation of Employee."""
        return '%s: %s' % (self.username, self.company)
