from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group

from .models import Customer
from django.dispatch import receiver

"""

TypeError at /register/

Field 'id' expected a number but got (<Group: customer>, False).

@receiver(post_save, sender=User)
def customer_profiles(sender, instance,created, **kwargs):
	if created:
		group=Group.objects.get_or_create(name="customer")
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			name=instance.username,
			)
		print("profile created!")
#post_save.connect(customer_profile, sender=User)

"""

@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwagrs):
    if created:
        group, is_created = Group.objects.get_or_create(name='customer')
        if is_created:
            instance.groups.add(Group.objects.get(name='customer'))
        else:
            instance.groups.add(group)
        Customer.objects.create(
                user = instance,
                name = instance.username
            )
        print('Profile created.!')




