from datetime import datetime


class KCObj:
    def __init__(self, kc_json_obj):
        self.timestamp = datetime.strptime(kc_json_obj['timestamp'].strip('Z'), "%Y-%m-%dT%H:%M:%S")
        self.close = float(kc_json_obj['close'])
        self.cross_status = kc_json_obj['cross_status']
        self.bbwap = float(kc_json_obj['bbwap'])
        self.emaL = float(kc_json_obj['emaL'])
        self.emaM = float(kc_json_obj['emaM'])
        self.emaH = float(kc_json_obj['emaH'])