"""Testing for submission"""

from exercises.ex06.dictionary import update_attendance

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday" , "Vrinda")
update_attendance(attendance_log, "Wednesday" , "Kaleb")
print(attendance_log)