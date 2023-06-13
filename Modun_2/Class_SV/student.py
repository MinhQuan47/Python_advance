class Student:

    # Chứa dữ liệu sinh viên

    __data = []

    def addStudent(self):

        #Hàm thêm một sinh viên

        print ( "*** THÊM SINH VIÊN ***" )

    # Cấu trúc lưu trữ một sinh viên

        infor = {'id' : '',

                'name' : ''

                }

# Nhập ID, có kiểm tra trùng ID thì nhập lại

        print("Nhập ID sinh viên:")

        id = input()

        while True:

            student = self.findStudent(id)

            if student!= False:

                print ( "ID này đã tồn tại, vui lòng nhập lại:" )

                d = input()

            else:

                break

        infor[ 'id' ] = id

        # Nhập tên

        print ( "Nhập tên sinh viên:" )

        infor[ 'name' ] = input ()
        # Lưu vào danh sách sv

        self.listStudents.append(infor)

    def findStudent(self, id):

    #Hàm tìm một sinh viên

        for i in range (0 , len ( self.listStudents)):

            if self.listStudents[i]['id'] == id:

# Trả về mảng gồm 2 phần tử,

# 0 là vị trí tìm thấy và 1 là dữ liệu

                return [i, self.listStudents[i]]

        return False

    def deleteStudent(self):

    #Hàm xóa sinh viên

        print ( "*** XÓA SINH VIÊN ***" )

        print ( "Nhập ID sinh viên cần xóa:" )

        id = input ()

        student = self.findStudent( id )

        if student != False:           
            self.listStudents.remove(student[1])

            print ("Xóa sinh viên thành công")

        else:

            print ("Không tìm thấy sinh viên cần xóa")

    def showStudents(self):

    #"""Hàm hiển thị danh sách sv"""

        print ("*** DANH SÁCH SINH VIÊN HIỆN TẠI ***" )

        for i in range(0, len(self.listStudents)):

            print("[",self.listStudents[i]['id'],"]" , "[" , self.listStudents[i]['name'])
