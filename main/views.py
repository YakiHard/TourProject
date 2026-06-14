from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from .models import Presentation, ExcursionTour, BeachTour, SkiTour

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Добро пожаловать {user}!')
            return redirect('index')
        else:
            return render(request, 'main/login/login.html', {
                'error_user_pass': 'Неверный логин или пароль'
            })
    return render(request, 'main/login/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        errors = {}

        if User.objects.filter(username=username).exists():
            errors['username_dublicate'] = 'Имя пользовавтеля существует'
        if len(password1) < 6:
            errors['pass_len_error'] = 'Пароль должен быть не менее 6 символов'
        if (password1 != password2):
            errors['pass1_pass2_error'] = 'Пароли не совпадают'
        if errors:
            errors['errors'] = True
            return render(request, 'main/login/register.html', errors)

        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        auth_login(request, user)
        return redirect('login')
    
    return render(request, 'main/login/register.html')

def logout_views(request):
    if request.method == 'GET':
        logout(request)
        return redirect("index")


def index(request):
    if request.method == 'POST':
        try:
            # Бронирование
            name=request.POST.get('name', '')
            surname=request.POST.get('surname', '')
            patronymic=request.POST.get('patronymic', '')
            number=request.POST.get('number', '')
            email=request.POST.get('email', '')

            # Согласие
            personal_data=request.POST.get('personal_data', '') == 'on'
            advertise_valls=request.POST.get('advertise_valls', '') == 'on'
               
            errors = {}

            if not name:
                errors['name_error'] = True
            if not surname:
                errors['surname_error'] = True
            if not number:
                errors['number_error'] = True
            if not email:
                errors['email_error'] = True
            if errors:
                errors['error_message'] = 'Пожалуйста, заполните все поля'
                return render(request, 'main/index.html', errors)
            
            tours = Presentation (
                name=name,
                surname=surname,
                patronymic=patronymic,
                number=number,
                email=email,
                personal_data=personal_data,
                advertise_valls=advertise_valls
            )
            tours.full_clean()
            tours.save()
            messages.success(request, 'Заявка на презентацию отправлена!')
            return redirect('index')
        except ValidationError:
            return render(request, 'main/index.html', {
                'error': 'Повторите запрос'
            })
    return render(request, 'main/index.html')
        
def create_excursion(request):
    if request.method == 'POST':
        try:
            # Бронирование
            direction=request.POST.get('direction', '')
            paris_excursion=request.POST.get('paris_excursion', '')
            rome_excursion=request.POST.get('rome_excursion', '')
            istanbul_excursion=request.POST.get('istanbul_excursion', '')
            saint_excursion=request.POST.get('saint_excursion', '')
            departure_date=request.POST.get('departure_date', '')
            name=request.POST.get('name', '')
            surname=request.POST.get('surname', '')
            patronymic=request.POST.get('patronymic', '')

            # Контактные данные
            number=request.POST.get('number', '')
            email=request.POST.get('email', '')

            # Согласие
            personal_data=request.POST.get('personal_data', '') == 'on'

            errors = {}

            if not direction:
                errors['direction_error'] = True
            if(direction == 'Paris' and not paris_excursion) or \
                (direction == 'Rome' and not rome_excursion) or \
                (direction == 'Istanbul' and not istanbul_excursion) or \
                (direction == 'Saint-Petersburg' and not saint_excursion):
                    errors['direction_error'] = True
            if not departure_date:
                errors['deoarture_date'] = True
            if departure_date < str(date.today()):
                errors['departure_date_today_error'] = True
            if not name:
                errors['name_error'] = True
            if not surname:
                errors['surname_error'] = True
            if not number:
                errors['number_error'] = True
            if not email:
                errors['email_error'] = True
            if errors:
                errors['error_message'] = 'Пожалуйста, заполните все поля'
                return render(request, 'main/excursion_form.html', errors)

            tours = ExcursionTour(
                user=request.user,
                direction=direction,
                paris_excursion=paris_excursion,
                rome_excursion=rome_excursion,
                istanbul_excursion=istanbul_excursion,
                saint_excursion=saint_excursion,
                departure_date=departure_date,
                name=name,
                surname=surname,
                patronymic=patronymic,
                number=number,
                email=email,
                personal_data=personal_data,
            )
            tours.full_clean()
            tours.save()
            messages.success(request, 'Заявка отправлена!')
            return redirect('my_tour_index')
        except ValidationError:
            return render(request, 'main/excursion_form.html', {
                'error': 'Повторите запрос'
            })
    return render(request, 'main/excursion_form.html')

def create_beach(request):
    if request.method == 'POST':
        try:
            direction=request.POST.get('direction', '')
            phuket_beach=request.POST.get('phuket_beach', '')
            hurghada_beach=request.POST.get('hurghada_beach', '')
            bali_beach=request.POST.get('bali_beach', '')
            male_beach=request.POST.get('male_beach', '') 
            departure_date=request.POST.get('departure_date', '')

            # Бронирование  
            name=request.POST.get('name', '')
            surname=request.POST.get('surname', '')
            patronymic=request.POST.get('patronymic', '')
            number=request.POST.get('number', '')
            email=request.POST.get('email', '')

            # Согласие
            personal_data=request.POST.get('personal_data', '') == 'on'

            errors = {}

            if not direction:
                errors['direction_error'] = True
            if(direction == 'Phuket' and not phuket_beach) or \
                (direction == 'Hurghada' and not hurghada_beach) or \
                (direction == 'Bali' and not bali_beach) or \
                (direction == 'Male' and not male_beach):
                    errors['direction_error'] = True
            if not departure_date:
                errors['departure_date_error'] = True
            if departure_date < str(date.today()):
                errors['departure_date_today_error'] = True
            if not name:
                errors['name_error'] = True
            if not surname:
                errors['surname_error'] = True
            if not number:
                errors['number_error'] = True
            if not email:
                errors['email_error'] = True
            if errors:
                errors['error_message'] = 'Пожалуйста, заполните все поля'
                return render(request, 'main/beach_form.html', errors)
            
            tours = BeachTour(
                user=request.user,
                direction=direction,
                phuket_beach=phuket_beach,
                hurghada_beach=hurghada_beach,
                bali_beach=bali_beach,
                male_beach=male_beach,
                departure_date=departure_date,
                name=name,
                email=email,
                surname=surname,
                patronymic=patronymic,
                number=number,
                personal_data=personal_data,
            ) 
            tours.full_clean()
            tours.save()
            messages.success(request, 'Заявка отправлена!')
            return redirect('my_tour_index')
        except ValidationError as e:
            return render(request, 'main/beach_form.html', { 
                'error': str(e),
            })
    return render(request, 'main/beach_form.html')

def create_ski(request):
    if request.method == 'POST':
        try:
            direction=request.POST.get('direction', '')
            zermatt_ski=request.POST.get('zermatt_ski', '')
            grindelwald_ski=request.POST.get('grindelwald_ski', '')
            chamonix_ski=request.POST.get('chamonix_ski', '')
            caruiso_ski=request.POST.get('caruiso_ski', '')
            departure_date=request.POST.get('departure_date', '')

            # Бронирование
            name=request.POST.get('name', '')
            surname=request.POST.get('surname', '')
            patronymic=request.POST.get('patronymic', '')
            number=request.POST.get('number', '')
            email=request.POST.get('email', '')
            
            # Согласие
            personal_data=request.POST.get('personal_data', '') == 'on'

            errors = {}

            if not direction:
                errors['direction_error'] = True
            if(direction == 'Zermatt' and not zermatt_ski) or \
                (direction == 'Grindelwald' and not grindelwald_ski) or \
                (direction == 'Chamonix' and not chamonix_ski) or \
                (direction == 'Caruiso' and not caruiso_ski):
                    errors['direction_error'] = True
            if not departure_date:
                errors['departure_date_error'] = True
            if departure_date < str(date.today()):
                errors['departure_date_tiday_error'] = True
            if not name:
                errors['name_error'] = True
            if not surname:
                errors['surname_error'] = True
            if not number:
                errors['number_error'] = True
            if not email:
                errors['email_error'] = True
            if errors:
                errors['error_message'] = 'Пожалуйста, заполните все поля'
                return render(request, 'main/ski_form.html', errors)
            
            tours = SkiTour(
                user=request.user,
                direction=direction,
                zermatt_ski=zermatt_ski,
                grindelwald_ski=grindelwald_ski,
                chamonix_ski=chamonix_ski,
                caruiso_ski=caruiso_ski,
                departure_date=departure_date,
                name=name,
                email=email,
                surname=surname,
                patronymic=patronymic,
                number=number,
                personal_data=personal_data,
            )
            tours.full_clean()
            tours.save()
            messages.success(request, "Заявка отправлена!")
            return redirect('my_tour_index')
        except ValidationError as e:
            return render(request, 'main/ski_form.html', {
                'error': "Повторите запрос"
            })
        
    return render(request, 'main/ski_form.html')
    
@login_required
def my_tour(request):
    excursion_tours = ExcursionTour.objects.filter(user=request.user)
    beach_tours = BeachTour.objects.filter(user=request.user)
    ski_tours = SkiTour.objects.filter(user=request.user)

    tours = []

    for tour in excursion_tours:
        tours.append(tour)
    for tour in beach_tours:
        tours.append(tour)
    for tour in ski_tours:
        tours.append(tour)
    if not tours:
        return render(request, 'main/null.html')
    return render(request, 'main/my_tour.html', {
        'tours': tours
    })

def cancel_tour(request, tour_id):
    for model in [ExcursionTour, BeachTour, SkiTour]:
        try:
            tour = model.objects.get(id=tour_id, user=request.user)
            tour.status = 'cancel'
            tour.save()
            messages.success(request, 'Заявка отмненена')
            break
        except:
            pass
    return redirect('my_tour_index')

def restart_tour(request, tour_id):
    for model in[ExcursionTour, BeachTour, SkiTour]:
        try:
            tour = model.objects.get(id=tour_id, user=request.user)
            tour.status = 'pending'
            tour.save()
            messages.success(request, 'Заявка возобновлена')
            break
        except:
            pass
    return redirect('my_tour_index')

def delete_tour(request, tour_id):
    for model in[ExcursionTour, BeachTour, SkiTour]:
        try:
            tour = model.objects.get(id=tour_id, user=request.user)
            tour.delete()
            messages.success(request, 'Заявка удалена')
            break
        except:
            pass
    return redirect('my_tour_index')

def null(request):
    return render(request, 'main/null.html')

def ski_history(request):
    return render(request, 'main/ski_history.html')

