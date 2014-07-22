from django.db import models
import datetime
from django.utils import timezone
from datetime import date

# Create your models here.

class Quote(models.Model):
    
    # Choices for fields below
    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Arkansas'),
        ('AZ', 'Arizona'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('GU', 'Guam'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('MP', 'Northern Mariana Islands'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('PR', 'Puerto Rico'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VI', 'Virgin Islands'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('DC', 'Washington, D.C.'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    YESNO = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    
    CLASSES = (
        ('PB', 'Preferred Best'),
        ('PR', 'Preferred'),
        ('SP', 'Standard Plus'),
        ('ST', 'Standard'),
    )
    
    PERIODS = tuple(map(lambda x: (str(x), str(x)+' Years'), range(0,40,5)))
    
    # Fields
    first_name = models.CharField('First Name', max_length=50, blank=False, null=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False, null=False)
    DOB = models.DateField('Birth Date', max_length=20)
    state = models.CharField('State', max_length=2, choices=STATES, blank=False, null=False) # add choices of all months
    gender = models.CharField('Gender', max_length=2, choices=GENDERS, blank=False, null=False) # add choices of male and female
    tobacco = models.CharField('Tobacco Use', max_length=2, choices=YESNO, blank=False, null=False) # add choices for yes and no
    health_class = models.CharField('Health Class', max_length=3, choices=CLASSES, blank=False, null=False) # add choices for health classifications
    term_period = models.CharField('Level Term Period', max_length=2, choices=PERIODS, blank=False, null=False) # add choices for term periods in 5 year intervals
    coverage_amount = models.IntegerField('Coverage Amount', blank=False, null=False)
    
    # Quote object name
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
        
    