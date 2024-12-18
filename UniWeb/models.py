from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=250)
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "UÝJ"
        verbose_name_plural = "UÝJ-lar"

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=250)
    first_year_students = models.IntegerField()
    second_year_students = models.IntegerField()
    third_year_students = models.IntegerField()
    fourth_year_students = models.IntegerField()
    fifth_year_students = models.IntegerField()

    class Meta:
        verbose_name = "fakultet"
        verbose_name_plural = "fakultetler"

    def __str__(self):
        return self.name


class CarouselImage(models.Model):
    header = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.header


class InfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.expression


class AboutInfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.expression


class CampusFirstInfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.expression


class CampusSecondInfoColumn(models.Model):
    expression = models.CharField(max_length=200)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.expression


class MainPageContent(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    image = models.ImageField(upload_to="main_page/")
    info_columns = models.ManyToManyField(InfoColumn)
    about_heading = models.CharField(max_length=200)
    about_description = models.CharField(max_length=200)
    carousel_images = models.ManyToManyField(CarouselImage)

    def __str__(self):
        return f"{self.id}. Baş sahypa maglumatlary"


class AdmissionsPage(models.Model):
    header = models.CharField(max_length=200)
    content = models.CharField(max_length=750)
    muted_text = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.id}. Kabul edilişik sahypa maglumatlary"


class AboutPage(models.Model):
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200)
    info_columns = models.ManyToManyField(AboutInfoColumn)

    def __str__(self):
        return f'{self.id}. "Biz barada" sahypa maglumatlary'


class CampusPage(models.Model):
    first_header = models.CharField(max_length=250)
    first_sub_header = models.TextField()
    first_info_columns_block = models.ManyToManyField(CampusFirstInfoColumn)

    second_header = models.CharField(max_length=250)
    second_sub_header = models.TextField()
    second_info_columns_block = models.ManyToManyField(CampusSecondInfoColumn)

    first_thumb_header = models.CharField(max_length=250)
    first_thumb_sub_header = models.TextField()
    first_thumb_image = models.ImageField(upload_to="campus/")

    second_thumb_header = models.CharField(max_length=250)
    second_thumb_sub_header = models.TextField()
    second_thumb_image = models.ImageField(upload_to="campus/")

    def __str__(self):
        return f"{self.id}. UÝJ sahypa maglumatlary"
