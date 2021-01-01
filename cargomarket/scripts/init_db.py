from django.contrib.auth.models import User
import time
from account.models import DriverProfile, CompanyProfile, License, DrivingLicense
import django
from cargomarket import settings as cargomarket_settings
from django.conf import settings
from django.core.management import call_command

def migrate():
    if not settings.configured:
        settings.configure(cargomarket_settings)
    django.setup()
    call_command("makemigrations", "account")
    call_command("migrate")


def run():
    migrate()

    # Create some dummy licenses
    patlayici = License(license_name="Patlayici Lisans", license_description="Patlayici tasiyabilir")
    patlayici.save()

    yanici = License(license_name="Yanici Lisans", license_description="Yanici tasiyabilir")
    yanici.save()

    # Create some dummy driving licenses
    b = DrivingLicense(driving_name="B", driving_description="Otomobil ve Kamyonet")
    b.save()

    c1 = DrivingLicense(driving_name="C1", driving_description="7500 kg’a Kadar Kamyon ve Çekici")
    c1.save()

    c1e = DrivingLicense(driving_name="C1E", driving_description="12000 KG’A Kadar Kamyon ve Çekici")
    c1e.save()

    c = DrivingLicense(driving_name="C", driving_description="Kamyon ve Çekici")
    c.save()
    
    d1 = DrivingLicense(driving_name="D1", driving_description="Minübüs")
    d1.save()

    # DRIVER USER BEGIN --->>>>>>>>>
    # Create a new Driver user
    driver_user = User(is_superuser=False)
    driver_user.username = "driver"
    driver_user.set_password("zisan123")
    driver_user.email = "driver@driver.com"
    driver_user.first_name = "Zişan"
    driver_user.last_name = "Karsatar"
    driver_user.save()

    # Create a new Driver profile, and associate with above driver user
    dp = DriverProfile()
    dp.phone_number = "+90212"
    dp.age="21"
    dp.gender = "Kadın"
    dp.nationality = "Türk"
    dp.experience= "4 yıl"
    dp.facebookUrl = "www.facebook.com"
    dp.websiteUrl = "www.website.com"
    dp.truck_model = "Mercedes Benz"
    dp.max_capacity = 25.8
    dp.languages= "Türkçe,İngilzce"
    dp.user = driver_user
    dp.save()
    dp.driving_licenses.add(b,c,c1e)
    dp.licenses.add(patlayici)

    # <<<<<------ DRIVER USER END

    # COMPANY USER BEGIN ---->>>>>>>
    # Create a new Company user
    company_user = User(is_superuser=False)
    company_user.username = "company"
    company_user.set_password("zisan123")
    company_user.email = "company@company.com"
    company_user.first_name = "Zişan"
    company_user.last_name = "Karsatar"
    company_user.save()

    # Create a new Company profile and associate with above company user
    cp = CompanyProfile()
    cp.phone_number = "+90555"
    cp.address = "Istanbul Maslak"
    cp.vd_no = "VD No: 3764783"
    cp.facebook = "www.facebook.com"
    cp.website = "www.website.com"
    cp.explain = "İp ve hali dokuma"
    cp.user = company_user
    cp.save()