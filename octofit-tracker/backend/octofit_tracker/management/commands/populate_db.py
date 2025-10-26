from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Borrar datos previos solo si existen instancias con clave primaria
        for model in [Activity, Workout, Leaderboard, User, Team]:
            objs = model.objects.all()
            for obj in objs:
                if getattr(obj, 'id', None):
                    obj.delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios superhéroes
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Crear actividades
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-10-25')
        Activity.objects.create(user=users[3], type='Cycling', duration=45, date='2025-10-25')

        # Crear workouts
        w1 = Workout.objects.create(name='Full Body', description='Entrenamiento completo')
        w2 = Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular')
        w1.suggested_for.set(users[:3])
        w2.suggested_for.set(users[3:])

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de prueba (superhéroes, equipos Marvel y DC)'))
