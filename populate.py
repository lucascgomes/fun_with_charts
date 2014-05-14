import os


def populate():
    default_chart = add_chart(name='Random Chart')

    add_timestamp(chart=default_chart, time=1, value=1)
    add_timestamp(chart=default_chart, time=2, value=2)
    add_timestamp(chart=default_chart, time=3, value=4)
    add_timestamp(chart=default_chart, time=5, value=8)
    add_timestamp(chart=default_chart, time=7, value=15)


def add_chart(name):
    c = Chart.objects.get_or_create(name=name)[0]
    return c

def add_timestamp(chart, time, value):
    t = TimeStamp.objects.get_or_create(chart=chart, time=time, value=value)[0]
    return t

if __name__ == '__main__':
    print "Starting chartapp population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fun_with_charts.settings')
    from chartapp.models import Chart, TimeStamp
    populate()