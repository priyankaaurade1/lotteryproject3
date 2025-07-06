from django.core.management.base import BaseCommand
from lottery.models import LotteryResult
from datetime import datetime, timedelta, time
import random

class Command(BaseCommand):
    help = "Generate all 10x10 lottery results for the day at once (9:00 AM to 9:30 PM)"

    def handle(self, *args, **kwargs):
        today = datetime.now().date()
        start_time = time(9, 0)
        end_time = time(21, 30)
        current = datetime.combine(today, start_time)

        while current.time() <= end_time:
            slot_time = current.time()

            for i in range(100):
                row = i // 10
                column = i % 10
                prefix = f"{i:02}"
                suffix = f"{random.randint(0, 99):02}"
                number = f"{prefix}{suffix}"

                LotteryResult.objects.get_or_create(
                    date=today,
                    time_slot=slot_time,
                    row=row,
                    column=column,
                    defaults={'number': number}
                )

            self.stdout.write(self.style.SUCCESS(f"✅ Generated results for slot: {slot_time.strftime('%I:%M %p')}"))
            current += timedelta(minutes=15)

        self.stdout.write(self.style.SUCCESS("🎉 All results for the day generated successfully."))