import json

from django.core.exceptions import ObjectDoesNotExist

from timeline.models import Event

def go():
    with open( "timeline/major_events.json" ) as f:
        raw_data = json.loads( f.read() )

    for raw_e in raw_data:
        exists = False
        try:
            e = Event.objects.get(name=raw_e['name'])
            exists = True
        except ObjectDoesNotExist:
            e = Event()

        e.year = raw_e['year']
        e.name = raw_e['name']

        if 'location' in raw_e:
            e.location = raw_e['location']

        if 'month' in raw_e:
            e.month = raw_e['month']

        if 'day' in raw_e:
            e.day = raw_e['day']

        if 'other' in raw_e:
            raw_o = raw_e['other']
            e.type = Event.SPAN_START
            if not exists:
                e_end = Event()
            else:
                e_end = e.other
            e_end.type = Event.SPAN_END
            e_end.year = raw_o['year']

            e_end.name = e.name + " End"

            if 'location' in raw_o:
                e_end.location = raw_o['location']

            if 'month' in raw_o:
                e_end.month = raw_o['month']

            if 'day' in raw_o:
                e_end.day = raw_o['day']

            e_end.save()

            e.other = e_end
        else:
            e.type = Event.SINGLE

        e.save()
