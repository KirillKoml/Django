from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Категория",
        help_text="Введите название категорий",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание категорий",
        blank=True,
        null=True,
    )

    class Mete:
        verbose_name = "Товар"
        verbose_description = "Товара"

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Название",
        help_text="Введите название товара",
    )
    image = models.ImageField(
        upload_to="products/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        blank=True, null=True, verbose_name="Цена", help_text="Укажите цену"
    )
    data_bd = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата создания",
        help_text="укажите дату создания",
    )
    data_refresh = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата изменения",
        help_text="укажите дату изменения",
    )

    class Mete:
        verbose_name = "Товар"
        verbose_description = "Товара"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name


# Create your models here.
