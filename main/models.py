from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User

def validation_date(departure_date):
    if departure_date < timezone.now().date():
        raise ValidationError("Дата выезда не может быть в прошлом")

class Tour(models.Model):
    DIRECTION = [                   
        ('Phuket','Пхукет, Таиланд'),
        ('Hurghada','Хургада, Египет'),
        ('Bali','Бали, Индонезия'),
        ('Male','Мале, Мальдивы'),
        ('Zermatt','Церматт, Швейцария'),
        ('Grindelwald','Гриндельвальд, Швейцария'),
        ('Chamonix','Шамони, Франция'),
        ('Caruiso','Каруизо, Италия'),
        ('Paris','Париж, Франция'),
        ('Rome','Рим, Италия'),
        ('Istanbul','Стамбул, Турция'),
        ('Saint-Petersburg','Санкт-Петербург, Россия')
    ]

    STATUS_CHOICES = [
        ('pending','Новая'),        # только создана
        ('processing','В обработке'), # админ смотрит
        ('cancel','Отменено'),
        ('completed','Завершено')   # готово
    ]

    status = models.CharField(choices=STATUS_CHOICES, default="pending")
    direction = models.CharField(max_length=100, choices=DIRECTION, verbose_name="Направление") 
    departure_date = models.DateField(verbose_name="Дата выезда", validators=[validation_date]) 
    #Личные данные
    name = models.CharField(max_length=15, verbose_name="Имя")
    surname = models.CharField(max_length=15, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=15, verbose_name="Отчество", blank=True)
    # Контактные данные
    number = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Email")
    # Согласие
    personal_data = models.BooleanField(default=False, verbose_name="Согласие на обработку персональных данных")
    advertise_valls = models.BooleanField(default=False, verbose_name="Согласие на получение рекламы и звонков")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class ExcursionTour(Tour):

    PARIS_EXCURSION = [
        ('eifell_tower','Эйфелева Башня'),
        ('louvre','Лувр'),
        ('notre_dame','Нотр-Даме-де-Пари')
    ]

    ROME_EXCURSION = [
        ('coliseum','Колизей'),
        ('pantheon','Пантеон'),
        ('st_peter','Собр Святого Петра')
    ]

    ISTANBUL_EXCURSION = [
        ('hagua_sophia','Айя-София'),
        ('blue_mosque','Голубая мечеть')
    ]

    SAINT_PETERBURG = [
        ('hermitage','Эрмитаж'),
        ('peter_paul','Петропавловская крепость')
    ]

    paris_excursion = models.CharField(choices=PARIS_EXCURSION, verbose_name="Экскурсия в Париж, Франция", blank=True)
    rome_excursion = models.CharField(choices=ROME_EXCURSION, verbose_name="Экскурсия в Рим, Италия", blank=True)
    istanbul_excursion = models.CharField(choices=ISTANBUL_EXCURSION, verbose_name="Экскурсия в Стамбул, Турция", blank=True)
    saint_excursion = models.CharField(choices=SAINT_PETERBURG, verbose_name="Экскурсия в Санкт-Петербург, Россия", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class BeachTour(Tour):

    PHUKET_BEACH = [
        ('patong','Патонг'),
        ('kata','Ката')
    ]

    HURGHADA_BEACH = [
        ('sahl_hasheesh','Сахл Хашиш'),
        ('el_gouna','Эль-Гуна')
    ]

    BALI_BEACH = [
        ('kuta','Кута'),
        ('nusa_dua', 'Нуса Дуа')
    ]

    MALE_BEACH = [
        ('ari_atoll','Ари Атолл'),
        ('baa_atoll','Баа Атолл')
    ]

    phuket_beach = models.CharField(choices=PHUKET_BEACH, verbose_name="Пляж в Пхукет, Таиланд", blank=True)
    hurghada_beach = models.CharField(choices=HURGHADA_BEACH, verbose_name="Пляж в Хургада, Египет", blank=True)
    bali_beach = models.CharField(choices=BALI_BEACH, verbose_name="Пляж в Бали, Индонезия", blank=True)
    male_beach = models.CharField(choices=MALE_BEACH, verbose_name="Пляж в Мале, Мальдивы", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class SkiTour(Tour):
    ZERMATT_SKI = [
        ('matterhorn', 'Маттерхорн')
    ]

    GRINDELWALD_SKI = [
        ('iger','Айгер')
    ]

    CHAMONIX_SKI = [
        ('montBlanc','Монблан (4 810 м)')
    ]

    CARUISO_SKI = [
        ('Val-Gardena','Валь-Гардена'),
        ('Gran San Bernardo','Гран-Сан-Бернардо')
    ]

    zermatt_ski = models.CharField(choices=ZERMATT_SKI, max_length=20, verbose_name="Гора в Церматт, Швейцария", blank=True)
    grindelwald_ski = models.CharField(choices=GRINDELWALD_SKI, verbose_name='Гора в Гриндельвальд, Швейцария', blank=True)
    chamonix_ski = models.CharField(choices=CHAMONIX_SKI, max_length=20, verbose_name="Гора в Шамони, Франция", blank=True)
    caruiso_ski = models.CharField(choices=CARUISO_SKI, verbose_name='Гора в Валь-Гардена, Гран-Сан-Бернардо, Италия', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Presentation(models.Model):
    #Личные данные
    name = models.CharField(max_length=15, verbose_name="Имя")
    surname = models.CharField(max_length=15, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=15, verbose_name="Отчество", blank=True)

    # Контактные данные
    number = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Email")

    # Согласие
    personal_data = models.BooleanField(default=False, verbose_name="Согласие на обработку персональных данных")
    advertise_valls = models.BooleanField(default=False, verbose_name="Согласие на получение рекламы и звонков")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



