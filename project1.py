
import csv

def info_csv(info_list):
    with open('student.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
           writer.writerow(["Name","Age","Contact Number","E-mail"])
           
        writer.writerow(info_list)

if __name__=='__main__':
 condition=True
 student_num=1

 while(condition):

    student_info=input("Enter the student  information for student #{} in following format (Name,Age,Contact_no,Email):".format(student_num))
    # print( "Entered Informantion is: "+student_info)

    split_student_list=student_info.split(' ')
    # print("Split information is :"+str(split_student_list))
    print("\nThe entered information is -\nName: {}\nAge: {}\nContact Number: {}\nE-Mail id"
          .format(split_student_list[0],split_student_list[1],split_student_list[2],split_student_list[3]))

    choice_check=input("is entered information is correct? (yes/no) :")

    if choice_check=="yes":
       info_csv(split_student_list)

       condition_check=input("Choose from two option (yes/no), if you want to add another student data : ")
       if condition_check=="yes":
         condition=True
         student_num=student_num+1
       elif condition_check=="no" :
         condition=False
    elif choice_check=="no":
        print("\nPlease re-enter the values ")
    