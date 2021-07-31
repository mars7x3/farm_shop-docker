from django.db import models


class Category (models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(primary_key=True, verbose_name='Слаг')
    parent = models.ForeignKey('self',
                               on_delete=models.DO_NOTHING,
                               related_name='children',
                               blank=True, null=True,
                               verbose_name='Родительская категория')

    def __str__(self):
        if self.parent:
            return f'{self.parent} | {self.title}'
        return self.title

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'



class Product(models.Model):
    STATUS_CHOICES = (
        ('В наличии', 'В наличии'),
        ('Нет в наличии', 'Нет в наличии'),
        ('В ожидании', 'В ожидании')
    )
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.FileField(upload_to='products',
                              verbose_name='Изображение')
    category = models.ForeignKey(Category,
                                 on_delete=models.DO_NOTHING,
                                 related_name='products',
                                 verbose_name='Категория')
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=20, verbose_name='Статус')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'product_id': self.pk})

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'



class Content(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    company_text = models.TextField(verbose_name='О компании')


class Order(models.Model):
    USER_STATUS = (
        ('Новая', 'Новая'), ('В обработке', 'В обработке'), ('Готово', 'Готово')
    )

    user_name = models.CharField(max_length=100, verbose_name='Имя')
    user_email = models.EmailField(verbose_name='Почта')
    user_phone = models.CharField(max_length=100, verbose_name='Телефон')
    user_message = models.TextField(verbose_name='Сообщение')
    user_status = models.CharField(choices=USER_STATUS, max_length=100, verbose_name='Статус', default='Новая')
    time_create = models.TimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['-id', ]
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


