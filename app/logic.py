from mongoengine import Document, IntField, StringField, ReferenceField


class Table(Document):
    number = IntField()
    number_of_guests = IntField()


class Reservation(Document):
    table = ReferenceField(Table)
    name = StringField()

    @staticmethod
    def is_reserved(table_id):
        return Reservation.objects.filter(table=table_id).count() > 0


def reserve(table, name):
    res = Reservation(table=Table.objects.get(number=table), name=name)
    res.save()


def get_tables():
    return [{"obj": table, "reserved": Reservation.is_reserved(table.id)} for table in Table.objects]

