import FCMManger as fcm
from datetime import datetime

print("fecha:"+ str(datetime.now()))
token = ["fFhD7jIzHOQ:APA91bErqVqloGMJdMtziizzxlBBSOW_hSiJ9z9MIFC2AwHQhiOe8szB6xiTWY6z1nMpjRiZYrXor1NIBsxqk9n2xKuE0h_XQ7_oF3lL16s9v_DnBEePQ3gSmZVH2lqG6PjXt2xrReGx"]
fcm.sendPush("hello", "mensaje", token)
fcm.send_notification_to_user("admin", ["Hello"])