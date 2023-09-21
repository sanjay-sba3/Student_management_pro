from django.core.management.base import BaseCommand
from student.models.user import Role, User
from student.models.student import Student, Branch



class Command(BaseCommand):
    def handle(self, *args, **options):   
        try:     
            # save role
            role_data = [
                {"role":"superadmin"
                },
                {"role":"admin"
                },
                {"role":"oparator"
                }, 
            ]
            
            for data in role_data:
                roles = Role(role=data["role"])
                roles.save()

            self.stdout.write(self.style.SUCCESS("Data Seed Succeefully"))


            branch = [
                {"student_branch":"civil"
                },
                {"student_branch":"Electronics"
                },
                {"student_branch":"CSE"
                 },
                 {"student_branch": "Mechanical"
                  },
                 
            ]
            
            for data in branch:
                branchs = Branch(student_branch=data["student_branch"])
                branchs.save()

            self.stdout.write(self.style.SUCCESS("Data Seed Succeefully"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"data not seeded, {e}"))       