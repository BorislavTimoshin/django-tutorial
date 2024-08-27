from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Слаг',
    )
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.IntegerField(
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус',
    )
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Категории',
    )
    tags = models.ManyToManyField(
        'TagPost',
        blank=True,
        related_name='posts',
        verbose_name='Теги',
    )
    husband = models.OneToOneField(
        'Husband',
        on_delete=models.SET_NULL,
        null=True,
        related_name='woman',
        verbose_name='Муж',
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = 'Известная женщина'
        verbose_name_plural = 'Известные женщины'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='Слаг',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
