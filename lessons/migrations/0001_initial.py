import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicStudentUser',
             fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'blank': 'Username cannot be blank.', 'invalid': 'Username must start with @ and can only contain letters and numbers.', 'max_length': 'Username cannot be more than 30 characters long.', 'null': 'Username cannot be null.', 'unique': 'A user with that username already exists.'}, max_length=30, unique=True, validators=[django.core.validators.RegexValidator(message='Username must start with @ and contain only letters and numbers.', regex='^@[a-zA-Z0-9]{3,30}$')])),
                ('first_name', models.CharField(error_messages={'blank': 'First name cannot be blank.', 'max_length': 'First name cannot be more than 50 characters long.', 'null': 'First name cannot be null.'}, max_length=50)),
                ('last_name', models.CharField(error_messages={'blank': 'Last name cannot be blank.', 'max_length': 'Last name cannot be more than 50 characters long.', 'null': 'Last name cannot be null.'}, max_length=50)),
                ('email', models.EmailField(error_messages={'blank': 'Email cannot be blank.', 'invalid': 'Email must be a valid email address, containing alphanumeric characters.', 'max_length': 'Email cannot be more than 254 characters long.', 'null': 'Email cannot be null.', 'unique': 'A user with that email already exists.'}, max_length=254, unique=True, validators=[django.core.validators.RegexValidator(message='Email must be a valid email address, containing alphanumeric characters.', regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')])),
                ('bio', models.TextField(blank=True, error_messages={'invalid': 'Bio can only contain alphanumeric characters and the following special characters: !@#$%^&*()_+-=,./<>?;\':"[]{}|`~', 'max_length': 'Bio cannot be more than 520 characters long.'}, max_length=520, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9!@#$%^&*()_+-=,./<>?;\':\\"\\[\\]{}|`~ ]{0,520}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
             managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
