from celery import shared_task
from .models import MyModel
from .views import MyDataViewSet
from celery.schedules import interval


@shared_task(run_every=interval(minutes=60))
def update_data():
    # Call API endpoint to retrieve data
    data = MyDataViewSet.as_view({"get": "get"})({}, format="json")
    # Process and save data to database
    for item in data.data:
        MyModel.objects.update_or_create(
            id=item["id"],
            defaults={
                "field1": item["field1"],
                # ... map other fields
            },
        )