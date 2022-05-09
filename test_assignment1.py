##
## Unit tests for ME369P/396P Spring 2022 Assignment 1
##

import pytest
import importlib
import os
import io
import sys
import random

path  = os.getcwd() + '/' + 'assignment1.py'
spec = importlib.util.spec_from_file_location("assignment1", path)
my_script = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(my_script)
    print("PASS: SCRIPT IS EXECUTABLE")
except Exception as ex:
    print('\n\nFAIL: EXCEPTION THROWN WHILE RUNNING FUNCTION:')
    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
except:
    print('\n\nFAIL: NON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


def test_scifiAuthors():
    # redirect student stdout
    file = "scifibookfavorites.txt"
    example = "example_scifibookfavorites.txt"
    my_output = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = my_output
    try:
        my_script.scifiAuthors(file)
    except Exception as ex:
        print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
        print(type(ex).__name__,': ',ex, end='\n\n', sep='')
    except:
        print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 
    #stdout is to console again
    sys.stdout = old_stdout
    my_output = my_output.getvalue()
    example_output = open(example).read()
    assert my_output == example_output




def test_animalCollectives():
    random.seed(1)
    file = "collecti.txt"
    test_inputs = ["bears", "lions", "cats", "cats", "whale", "fox", "dog", "goose", "exit"]
    expected_out = [('sleuth','bears'),('pride','lions'),('clutter','cats'),('clowder','cats'),('pod','whales'),('skulk','foxes'),('knot','dog'),('gaggle','geese'),('clutch','chicks')]     

    test_idx = 0
    for in_text in test_inputs:
        old_stdin = sys.stdin
        s = io.StringIO(in_text)
        sys.stdin  = s

        my_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = my_output

        try:
            my_script.animalCollectives(file)
        except Exception as ex:
            print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
            print(type(ex).__name__,': ',ex, end='\n\n', sep='')
        except:
            print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 

        #return input to stdin
        sys.stdin = old_stdin
        #stdout is to console again
        sys.stdout = old_stdout
        my_output = my_output.getvalue()

        if in_text == "exit" or in_text == "quit":
            expected_response = "A %s of %s got you!" % (expected_out[test_idx][0],expected_out[test_idx][1])
        else:
            expected_response = "A %s of %s is coming to git you!" % (expected_out[test_idx][0],expected_out[test_idx][1])

        #print(expected_response)
        #print("\n BREAK POINT \n")
        #print(my_output)
        assert expected_response in my_output
        test_idx += 1


def test_myCalculator():
    test_inputs = ["+\n3\n2\nq", "-\n5\n4\nq", "*\n3\n2\nq", "/\n4\n2\nq", "^\n3\n2\nq", "-\n\n\nq", "-\n3.1\n1\nq", "-\n2.7\n1.4\nq", "-\n2\n7\nq"]
    expected_out = ['5.0','1.0','6.0','2.0','9.0','0.0','2.1','1.3','-5.0']             

    test_idx = 0
    for in_text in test_inputs:
        old_stdin = sys.stdin
        s = io.StringIO(in_text)
        sys.stdin  = s

        my_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = my_output

        try:
            my_script.myCalculator()
        except Exception as ex:
            print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
            print(type(ex).__name__,': ',ex, end='\n\n', sep='')
        except:
            print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 

        #return input to stdin
        sys.stdin = old_stdin
        #stdout is to console again
        sys.stdout = old_stdout
        my_output = my_output.getvalue()
        
        assert expected_out[test_idx] in my_output
        test_idx += 1

#test_scifiAuthors()
#test_animalCollectives()
test_myCalculator()
