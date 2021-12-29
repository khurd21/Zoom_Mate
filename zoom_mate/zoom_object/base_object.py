from zoom_mate import Zoom_Meeting

from config import Config
import csv


class ZoomObject:

    def __init__(self, config=Config):
        self._config   = config
        self.meetings  = self._gather_meetings()
        return 

    
    def _gather_meetings(self) -> list:

        meetings = []
        # CSV FORMAT: meeting-id,password,class-name,start-time,end-time,days
        with open(self._config.MEETINGS_CSV, 'r') as csvfile:

            csv_reader = csv.DictReader(csvfile=csvfile)
            for row in csv_reader:
                meetings.append(Zoom_Meeting(meeting_id=row['meeting-id'],
                                            password=row['password'], class_name=row['class-name'],
                                            start_time=row['start-time'], end_time=row['end-time'],
                                            days=row['days'],
                                            )
                                )
        return meetings

    
    def display_meetings(self) -> None:
        for i, meeting in enumerate(self.meetings):
            print(f'{i+1}. {meeting.class_name}\n' \
                f'Start Time: {meeting.start_time}\n' \
                    f'Days: {meeting.days}'
                    )
            