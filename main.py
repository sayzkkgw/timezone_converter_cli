import fire
import datetime
import pytz

from timezones import tz


class Converter(object):
    def __init__(self, zones: tuple):
        self._zones = zones
        self.local_tz = 'jst'
        self.tz_fmt = '%m-%d %H:%M%z'

    def get_cur_time(self):
        for zone in self._zones:
            try:
                target_timezone = pytz.timezone(tz.get(zone))
            except Exception as e:
                return e, f'specified timezone is wrong. Write the correct timezone'
            target_local_time = datetime.datetime.now(
                target_timezone).strftime(self.tz_fmt)
            print(f'TZ:{zone} {target_local_time}')

    def get_target_time(self, start_time: datetime, end_time: datetime = None):
        local_timezone = pytz.timezone(tz.get(self.local_tz))

        s_year, s_month, s_day, s_hour, s_minute = str(
            start_time).split('-')
        dt_start = datetime.datetime(int(s_year), int(s_month), int(
            s_day), int(s_hour), int(s_minute), 00)

        if end_time:
            e_year, e_month, e_day, e_hour, e_minute = str(
                end_time).split('-')
            dt_end = datetime.datetime(int(e_year), int(e_month), int(
                e_day), int(e_hour), int(e_minute), 00)

        for zone in self._zones:
            local_dt_s = local_timezone.localize(dt_start)
            local_dt_e = local_timezone.localize(dt_end)
            try:
                target_timezone = pytz.timezone(tz.get(zone))
            except Exception as e:
                return e, f'specified timezone is wrong. Write the correct timezone'

            print(
                f"TZ: {zone} Start Time: {local_dt_s.astimezone(target_timezone).strftime(self.tz_fmt)}",
                f"End Time: {local_dt_e.astimezone(target_timezone).strftime(self.tz_fmt) if end_time else None}",
                # sep='\t'
            )


if __name__ == '__main__':
    fire.Fire(Converter)
