from django.test import TestCase
from .models import Project

# Create your tests here.

class ProjectModelTest(TestCase):
    def test_autoincrement_sequence(self):
        """
        When project is added, it takes the next autoincrement pk; 
        when the project is deleted, the pk is not replaced. 
        This test identifies whether a sequential pk is missing
        """
        final_pk = Project.objects.count()
        
        reverse_list = Project.objects.all().order_by('-pk')
        
        correct_last_pk = Project.objects.filter(pk=final_pk)
        actual_last_entry = reverse_list #this is incomplete--I'm not sure why, but when I try to index the query set at [0] I get an index out of range error
        
        
        self.assertEqual(correct_last_pk, actual_last_entry)

        
        
 
