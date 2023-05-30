import datetime
jam = datetime.datetime.now()
#===========================================================FUNCTION DICTIONARY==========================================================================
#[1]. Database
#[2]. Regular Functions Used in the Application
#   [1]. app() => To run the main application.
#   [2]. print_menu() => To print navigation menu (at home or root).
#   [3]. nav_menu() => to process user input to navigate to another location.
#   [4]. is_student_registered(input_nis) => to validate if the user already exists or not in the database. it requires 1 parameter which is NIS.
#   [5]. is_semester_registered(index, NIS) => to check if a student already register the scores on certain semester, it requires 2 parameter input (INDEX, NIS).
#   [6]. search_index_student(NIS) => to check where the user data is stored on the list index. require 1 parameter input (NIS).
#   [7]. verif_input_matematika()/verif_input_fisika()/verif_input_kimia()/verif_input_biologi() => to check if the user input is valid (checking if the input is numeric, >= 0 or <=100).
#   [8]. input_nilai_semester()=> to register scores of ALL courses in certain semester. Requires 2 parameter (index, semester).
#   [9]. printing_registered_scores_semester() => to print the scores that is successfully registered or saved.
#   [10].print_nilai_sudah_ada() => to print the students scores of certain semester. to remind the user that the student score on the certain semester is already filled.
#   [11].input_data_siswa()=>To register student data into the database.
#   [12].tambah_siswa() => part of input_data_siswa() func. to append the data into the database. 
#   [13].tampilkan_nilai_siswa() => to print all the students scores of all semester. 
#   [14].header_sub_input_1()=> to print the header of sub input 1.
#   [15].header_update_menu()=> to print the header on the update menu.
#   [16].header_delete_menu()=> to print the header on the delete menu.
#   [17].hapus_nilai_siswa()=> to delete students score 
#   [18].hapus_data_siswa()=> to delete all of certain student data
#   [19].perbaharui_nilai_per_semester() => to update all of students score on a certain semester.
#   [20].perbaharui_nilai_per_pelajaran()=> to update student's score on a certain subject.
#   [21].show_students_desc()=> to display all student data sorted by NIS in descending order.
#   [22].show_students_asc()=> to display all student data sorted by NIS in ascending order.

#============================================================PROGRAM FLOW===========================================================================
# [1]. Menambah Nilai Siswa
#    [1][1]. Menambah Nilai Siswa Yang Sudah Terdaftar.
#    [1][2]. Mendaftarkan Siswa Terlebih Dahulu.
#    [1][3]. Kembali Ke Menu Utama
# [2]. Menampilkan Nilai Siswa
#    [2][1]. Menampilkan nilai seluruh semester.
#    [2][2]. menampilkan nilai berdasarkan semester.
#    [2][3]. Kembali Ke Menu Utama
# [3]. Memperbaharui Nilai Siswa
#    [3][1]. Memperbaharui nilai seluruh pelajaran pada semester tertentu
#    [3][2]. Memperbaharui nilai pelajaran tertentu pada suatu
#    [3][3]. Kembali Ke Menu Utama
# [4]. Menghapus Nilai Siswa
#    [4][1]. Menghapus semua data seorang siswa
#    [4][2]. Menghapus nilai siswa berdasarkan semester yang  dipilih
#    [4][3]. Kembali Ke Menu Utama
# [5]. Menambah data Siswa
# [6]. Menampilkan Data Siswa
#    [6][1]. Menampilkan Data Siswa Secara Ascending Berdasarkan NIS
#    [6][2]. Menampilkan Data Siswa Secara Descending Berdasarkan NIS
# [7]. Exit

#===============================================SISTEM AKADEMIK TERPADU SMA PURWADHIKA==============================================================
#[1]INITIAL DATABASE
# ''' The Database Consists of :
#     [1]. NIS = Nomor Induk Siswa. this column is being used as primary key
#     [2]. Nama. this is being used to store student's full name
#     #Courses
#           [Semester 1]              [2. Semester 2]                    [Semester 3]                       [Semester4]
#     [3]. semester1_matematika  [7]. semester2_matematika      [11]. semester3_matematika      [15]. semester4_matematika        
#     [4]. semester1_fisika      [8]. semester2_fisika          [12]. semester3_fisika          [16]. semester4_fisika
#     [5]. semester1_kimia       [9]. semester2_kimia           [13]. semester3_kimia           [17]. semester4_kimia
#     [6]. semester1_biologi     [10]. semester2_biologi        [14]. semester3_biologi         [18]. semester4_biologi
          
#           [Semester 5]              [Semester 6]
#     [19]. semester5_matematika [23]. semester6_matematika 
#     [20]. semester5_fisika     [24]. semester6_fisika 
#     [21]. semester5_kimia      [25]. semester6_kimia
#     [22]. semester5_biologi    [26]. semester6_biologi 
# '''
#===========================================================INITIALIZING DATABASE===================================================================
students_db  = [
    {
        "NIS" : "202101",
        "Nama" : "Arief Kurniawan",
        "1": True, "semester1_matematika" : 100, "semester1_fisika" : 75, "semester1_kimia" : 85, "semester1_biologi" : 75,
        "2": True, "semester2_matematika" : 100, "semester2_fisika" : 75, "semester2_kimia" : 85, "semester2_biologi" : 75,
        "3": True, "semester3_matematika" : 100, "semester3_fisika" : 75, "semester3_kimia" : 85, "semester3_biologi" : 75,
        "4": True, "semester4_matematika" : 100, "semester4_fisika" : 75, "semester4_kimia" : 85, "semester4_biologi" : 75,
        "5": True, "semester5_matematika" : 100, "semester5_fisika" : 75, "semester5_kimia" : 85, "semester5_biologi" : 75,
        "6": True, "semester6_matematika" : 100, "semester6_fisika" : 75, "semester6_kimia" : 85, "semester6_biologi" : 75
    },
    {
        "NIS" : "202102",
        "Nama" : "Sharon Kurniawan",
        "1": True, "semester1_matematika" : 100, "semester1_fisika" : 75, "semester1_kimia" : 85, "semester1_biologi" : 75,
        "2": True, "semester2_matematika" : 100, "semester2_fisika" : 75, "semester2_kimia" : 85, "semester2_biologi" : 75,
        "3": True, "semester3_matematika" : 100, "semester3_fisika" : 75, "semester3_kimia" : 85, "semester3_biologi" : 75,
        "4": True, "semester4_matematika" : 100, "semester4_fisika" : 75, "semester4_kimia" : 85, "semester4_biologi" : 75,
        "5": True, "semester5_matematika" : 100, "semester5_fisika" : 75, "semester5_kimia" : 85, "semester5_biologi" : 75,
        "6": True, "semester6_matematika" : 100, "semester6_fisika" : 75, "semester6_kimia" : 85, "semester6_biologi" : 75
    },
    {
        "NIS" : "202103",
        "Nama" : "Stephanie Anastasia",
        "1": True, "semester1_matematika" : 100, "semester1_fisika" : 75, "semester1_kimia" : 85, "semester1_biologi" : 75,
        "2": True, "semester2_matematika" : 100, "semester2_fisika" : 75, "semester2_kimia" : 85, "semester2_biologi" : 75,
        "3": True, "semester3_matematika" : 100, "semester3_fisika" : 75, "semester3_kimia" : 85, "semester3_biologi" : 75,
        "4": True, "semester4_matematika" : 100, "semester4_fisika" : 75, "semester4_kimia" : 85, "semester4_biologi" : 75,
        "5": True, "semester5_matematika" : 100, "semester5_fisika" : 75, "semester5_kimia" : 85, "semester5_biologi" : 75,
        "6": True, "semester6_matematika" : 100, "semester6_fisika" : 75, "semester6_kimia" : 85, "semester6_biologi" : 75
    },
    {
        "NIS" : "202104",
        "Nama" : "Stella Windaya",
        "1": True,"semester1_matematika" : 100, "semester1_fisika" : 75, "semester1_kimia" : 85, "semester1_biologi" : 75,
        "2": True,"semester2_matematika" : 100, "semester2_fisika" : 75, "semester2_kimia" : 85, "semester2_biologi" : 75,
        "3": True,"semester3_matematika" : 100, "semester3_fisika" : 75, "semester3_kimia" : 85, "semester3_biologi" : 75,
        "4": True,"semester4_matematika" : 100, "semester4_fisika" : 75, "semester4_kimia" : 85, "semester4_biologi" : 75,
        "5": True,"semester5_matematika" : 100, "semester5_fisika" : 75, "semester5_kimia" : 85, "semester5_biologi" : 75,
        "6": True,"semester6_matematika" : 100, "semester6_fisika" : 75, "semester6_kimia" : 85, "semester6_biologi" : 75
    },
    {
        "NIS" : "202105",
        "Nama" : "Indah Windaya",
        "1": True, "semester1_matematika" : 100, "semester1_fisika" : 75, "semester1_kimia" : 85, "semester1_biologi" : 75,
        "2": True, "semester2_matematika" : 100, "semester2_fisika" : 75, "semester2_kimia" : 85, "semester2_biologi" : 75,
        "3": True, "semester3_matematika" : 100, "semester3_fisika" : 75, "semester3_kimia" : 85, "semester3_biologi" : 75
    }
] #Database menggunakan dictionary dalam list
#===============================================================================================================================================
#MAIN APP
def app():
    input_menu = nav_menu() 
    while input_menu != 7 :
        #=======================================================[1]TAMBAH NILAI================================================================ 
        if input_menu == "1":
            header_sub_input_1()
            sub_input_1 = input("Masukkan Pilihan : ")
            if sub_input_1 == "1": #Menambah nilai untuk siswa yang sudah terdaftar
                sub_sub_input_nim = input("Masukkan Nomor Induk Siswa : ")
                if is_student_registered(sub_sub_input_nim) == True: #Validasi apakah student sudah terdaftar atau belum
                    index_temp = search_index_student(sub_sub_input_nim) #Mencari index pada list dimana student terdaftar
                    sub_sub_input_semester = input("Masukkan Semester Yang Akan Dipilih : ")
                    if is_semester_registered(index_temp,sub_sub_input_semester) == False: #Validasi apakah siswa sudah memiliki nilai pada semester yang di maksud
                        if sub_sub_input_semester > '0' and sub_sub_input_semester < '7' and (sub_sub_input_semester.isnumeric()==True): #validasi semester yang diinput
                            input_nilai_semester(index_temp,sub_sub_input_semester)
                            printing_registered_scores_semester(index_temp,sub_sub_input_semester)
                            input_menu = nav_menu()
                        else:
                            print("❌ Semester tidak valid. Hanya dapat menginput semester 1 hingga 6. ❌")
                            input_menu = nav_menu()
                    else:
                        print(f"{10*' '} Daftar nilai pada semester ini sudah ada")
                        print_nilai_sudah_ada(index_temp)
                        print(f"  Nilai Pada Semester ini Tidak dapat ditambahkan Karena Sudah Terisi Sebelumnya.")
                        input_menu = nav_menu()
                else :
                    print(f"{140*'='}")
                    print()
                    print(f"{' '*40}[❌] Siswa Tidak Terdaftar, harap daftarkan terlebih dahulu. [❌] ")
                    print()
                    print(f"{140*'='}")
                    input_menu = nav_menu()
            elif sub_input_1 == "2": #Menu Apabila Siswa Belum Terdaftar, maka perlu didaftarkan terlebih dahulu 
                input_data_siswa()
            elif sub_input_1 == "3":
                input_menu = nav_menu()
            else :
                print("Silahkan Masukkan Input Sesuai Yang Tertera Pada Daftar Menu.")
                input_menu = nav_menu()
        #========================================================[2]Menampilkan nilai siswa=========================================================    
        elif input_menu == "2":
            header_read_menu()
            sub_input_menu2 = input("Masukkan Menu Yang Akan Dipilih : ")
            if sub_input_menu2 == '1': #Tampilkan seluruh nilai seluruh semester
                input_nim = input("Masukkan Nomor Induk Siswa : ")
                index_read = search_index_student(input_nim) #mencari index pada list berdasarkan NIS yang diinput
                if index_read != -1:
                    print_nilai_sudah_ada(index_read) #jika index ditemukan maka mencetak nilai
                else:
                    print(f"{110*'='}")
                    print(f"{' '*40}❌ Student tidak ditemukan ❌") #jika index tidak ditemukan maka mencetak notifikasi 
                    print(f"{110*'='}")
                input_menu = nav_menu()
            elif sub_input_menu2 == '2': #Tampilkan nilai per semester
                input_nim = input("Masukkan Nomor Induk Siswa : ")
                index_read2 = search_index_student(input_nim)
                if is_student_registered(input_nim):#== True #validasi student apakah sudah terdaftar  atau belum
                    input_semester = input("Masukkan Semester Yang Akan Dipilih : ")
                    if is_semester_registered(index_read2,input_semester) == True: #validasi apakah student sudah memiliki nilai pada semester tertentu
                        tampilkan_nilai_siswa(input_nim,input_semester)
                        input_menu = nav_menu()
                    else:
                        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Nilai pada semester ini tidak ada.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print()
                        input_menu = nav_menu()
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Student tidak terdaftar~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
                    input_menu = nav_menu()
            #====================
            elif sub_input_menu2 =='3': #Kembali ke menu utama
                input_menu = nav_menu()
            else:
                print("Tolong Masukkan menu sesuai pilihan yang tersedia. Kembali ke menu utama")
                input_menu = nav_menu()
#==============================================================[4]UPDATE=======================================================================
        elif input_menu == "3": #UPDATE
            header_update_menu() #mencetak header 
            sub_menu_3 = input("Masukkan menu yang akan dipilih : ")
            if sub_menu_3 == '1':
                input_nim = input("Masukkan Nomor Induk Siswa (NIS) : ")
                index_upd = search_index_student(input_nim)
                if is_student_registered(input_nim):#== True #validasi apakah student sudah terdaftar
                    input_semester = input("Masukkan Semester Yang Akan Dipilih : ")
                    if is_semester_registered(index_upd,input_semester) == True: #validasi apakah semester sudah terdaftar
                        tampilkan_nilai_siswa(input_nim,input_semester) #menampilkan nilai sebelum  di perbaharui
                        perbaharui_nilai_per_semester(index_upd, input_semester) #memperbaharui nilai
                        print(f"{130*'='}")
                        print(f"{60*' '}Data Berhasil Diperbaharui!")
                        print(f"{130*'='}")
                        input_menu = nav_menu()
                    else:
                        print()
                        print(f"{110*'='}")
                        print(f"{35*' '}❌ Nilai pada semester ini tidak ada. ❌")
                        print(f"{110*'='}")
                        input_menu = nav_menu()
                else:
                    print("❌ Student tidak terdaftar sehingga tidak dapat memperbaharui data ❌")
                    input_menu = nav_menu()
            elif sub_menu_3 == '2':
                input_nim = input("Masukkan Nomor Induk Siswa (NIS) : ")
                index_upd2 = search_index_student(input_nim)
                if is_student_registered(input_nim):#== True #validasi siswa apakah sudah terdaftar atau belum
                    input_semester = input("Masukkan Semester Yang Akan Dipilih : ")
                    if is_semester_registered(index_upd2,input_semester) == True: #validasi semester
                        tampilkan_nilai_siswa(input_nim,input_semester) #menampilkan nilai apabila lolos dari kedua validasi diatas
                        print('''====================================================================================================================
                    
                    [1]. Masukkan 1 untuk memperbaharui nilai matematika
                    [2]. Masukkan 2 untuk memperbaharui nilai fisika
                    [3]. Masukkan 3 untuk memperbaharui nilai kimia
                    [4]. Masukkan 4 untuk memperbaharui nilai biologi

                        ''')
                        input_pelajaran = input("Masukkan pilihan : ")
                        while input_pelajaran not in ['1','2','3','4']: 
                            print("Masukkan input sesuai dengan pilihan yang tersedia!. ")
                            input_pelajaran = input("Masukkan pilihan : ")
                        perbaharui_nilai_per_pelajaran(index_upd2, input_semester,input_pelajaran)
                        tampilkan_nilai_siswa(input_nim,input_semester)
                        input_menu = nav_menu()
                    else:
                        print("Nilai pada semester ini tidak ada.")
                        input_menu = nav_menu()
                else:
                    print("❌ Student tidak terdaftar sehingga tidak dapat memperbaharui data ❌")
                    input_menu = nav_menu()
            elif sub_menu_3 == '3':
                input_menu = nav_menu()
            else:
                print("Masukkan input sesuai pilihan yang tersedia!. Kembali ke menu utama.")
                input_menu = nav_menu()
#======================================================[4]DELEtE===================================================================================
        elif input_menu == "4":
            header_delete_menu()#mencetak header delete
            input_sub_menu_4 = input("Masukkan menu : ")
            if input_sub_menu_4 == '1': #Hapus nilai seluruh data seorang siswa
                input_nim = input("Masukkan Nomor Induk Siswa : ")
                index_for_del = search_index_student(input_nim) #mencari index student
                if is_student_registered(input_nim): #validasi student
                    print('''Apakah anda yakin akan menghapus data siswa? 
        [Y] untuk menghapus
        [N] Untuk tidak menghapus
        ''')        
                    input_del_student = input("Masukkan Pilihan : ")
                    while (input_del_student not in ["Y","y","n","N"]):
                        print("❌ Input yang dimasukkan salah, silahkan masukkan input kembali. ❌")
                        input_del_student = input("Masukkan Pilihan : ")
                    if (input_del_student == "Y") or (input_del_student == "y"):
                        hapus_data_siswa(index_for_del)
                        input_menu = nav_menu()
                    else :
                        print("Tidak ada data yang dihapus. Kembali  ke menu utama")
                        input_menu = nav_menu()
                else:
                    print("Student tidak terdaftar. Sehingga tidak dapat menghapus data siswa. Kembali ke menu utama")
                    input_menu = nav_menu()
            elif input_sub_menu_4 == '2': #Hapus nilai per semester
                input_nim = input("Masukkan Nomor Induk Siswa : ")
                index_temp = search_index_student(input_nim)
                if is_student_registered(input_nim):
                    input_semester = input("Masukkan Semester Yang Akan Dipilih : ")
                    if is_semester_registered(index_temp, input_semester) == True:
                        tampilkan_nilai_siswa(input_nim,input_semester)
                        #=
                        print('''Apakah anda yakin akan menghapus data siswa? 
                                    [Y] untuk menghapus
                                    [N] Untuk tidak menghapus
                                    ''')        
                        input_del_student = input("Masukkan Pilihan : ")
                        while (input_del_student not in ["Y","y","n","N"]):
                            print("❌ Input yang dimasukkan salah, silahkan masukkan input kembali. ❌")
                            input_del_student = input("Masukkan Pilihan : ")
                        if (input_del_student == "Y") or (input_del_student == "y"):
                            hapus_nilai_siswa(index_temp,input_semester)
                            input_menu = nav_menu()
                        else :
                            print(f"{140*'='}")
                            print(f"{' '*40}Tidak ada data yang dihapus. Kembali ke menu utama")
                            print(f"{140*'='}")
                            input_menu = nav_menu()
                            #=
                            
                    else:
                        print(f"{140*'='}")
                        print(f"{' '*40}Nilai pada semester ini tidak ada. Kembali  ke menu utama")
                        print(f"{140*'='}")
                        input_menu = nav_menu()
                else:
                    print("Student tidak terdaftar. Kembali  ke menu utama")
                    input_menu = nav_menu()
            elif input_sub_menu_4== '3':
                input_menu = nav_menu()
            else:
                print("Masukan input sesuai dengan menu navigasi yang tertera!")
#=======================================================[5]DAFTAR SISWA BARU==================================================================
        elif input_menu == "5":
            input_data_siswa()#NIS harus unik
            input_menu = nav_menu()
#=======================================================[6]Menampilkan  data siswa============================================================
        elif input_menu == "6":
            print('''
            [1]. Masukkan 1 untuk menampilkan data siswa secara ascending
            [2]. Masukkan 2 untuk menampilkan data siswa secara descending
            [3]. Kembali ke menu utama [ ↩ ]
            ''')
            sub_input_menu_6 = input("Masukkan pilihan menu : ")
            while sub_input_menu_6 not in ['1','2','3']:
                print("Menu yang anda masukkan tidak tersedia. Silahkan pilih menu kembali ")
                print()
                print('''
            [1]. Masukkan 1 untuk menampilkan data siswa secara ascending
            [2]. Masukkan 2 untuk menampilkan data siswa secara descending
            [3]. Kembali ke menu utama [ ↩ ]
            ''')
                sub_input_menu_6 = input("Masukkan pilihan menu : ")
        
            if sub_input_menu_6 == '1':
                show_students_asc() #function untuk menampilkan student secara ascending by nis
             
            elif sub_input_menu_6 =='2':
                show_students_desc() #function untuk menampilkan student secara desc by nis
             
            elif sub_input_menu_6 == '3':
                input_menu = nav_menu()
        elif input_menu == "7":
            break
        else:
            print("Silahkan Masukkan Input Sesuai Yang Tertera Pada Daftar Menu.")
            input_menu = nav_menu()
      
def print_menu(): #mencetak navigasi menu
    print(f"{'    '}{'_'*135}")
    print(f'''{" "*40 }Selamat Datang di Sistem Akademik Terpadu SMA Purwadhika{" "*17}{jam}
    {'_'*135}
    {" "*135}
    {" "*5}Navigation Menu
    {" "*5}------------------------------------------
    {" "*5}[1]. Menambah Nilai Siswa. \t\t[C]
    {" "*5}[2]. Menampilkan Nilai Siswa. \t\t[R]
    {" "*5}[3]. Memperbaharui Nilai Siswa. \t[U]
    {" "*5}[4]. Menghapus Nilai Siswa. \t\t[D]
    {" "*5}[5]. Menambah Data Siswa. 
    {" "*5}[6]. Menampilkan Data Siswa. 
    {" "*5}[7]. Exit. [X]
    ''')


def nav_menu(): #menu utama
    print()
    print()
    print_menu()
    input_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_menu

def is_student_registered(input_nis): #function untuk melakukan validasi apakah student studah terdaftar atau belum
    flagger = False
    counter = 0
    for i in range(len(students_db)):
        for value in students_db[counter].values():
            if input_nis == value :
                flagger = True #jika value sama dengan input nis maka merubah data bool dari false menjadi true
                break
        counter+=1
        if counter == len(students_db): #ketika nilai counter sama dengan panjang database maka break
            break
    return flagger        #if True then Student is found, else student is not found   
    
def is_semester_registered(index, input_semester): #validasi apakah semester sudah terdaftar atau belum
    flagger  = False
    for j in students_db[index].keys():
        if j == input_semester :
            flagger = True #jika semester ditemukan maka flagger berubah mjd true
            break
        else:
            flagger = False 
    return flagger
    
def search_index_student(input_nis): #mencari index pada list dimana nis itu berada
    student_indexer = -1
    for i in range(len(students_db)):
        for j in students_db[i].values():
            if j == input_nis:
                student_indexer = i #menyimpan index pada variabel student indexer
    return student_indexer

def verif_input_matematika(): #validasi nilai matematika harus numerik dan >=0 dan <=100
    verif_status = False
    while verif_status == False :
        input_matematika = input("Masukkan Nilai Matematika : ") #Input dalam bentuk string supaya dapat di cek numerik semua tanpa mengeluarkan error
        if (input_matematika.isnumeric() == True):
            if (int(input_matematika) < 0) or (int(input_matematika) > 100) :
                print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100! ❌")
            else: 
                verif_status = True #jika ok maka mereturn nilai matematika dalam bentuk integer
                return int(input_matematika)
        else:
            print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100! ❌")


def verif_input_fisika(): #validasi nilai fisika harus numerik dan >=0 dan <=100
    verif_status = False
    while verif_status == False :
        input_fisika = input("Masukkan Nilai Fisika : ")
        if (input_fisika.isnumeric() == True):
            if (int(input_fisika) < 0) or (int(input_fisika) > 100) :
                print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100 ❌")
            else: 
                verif_status = True
                return int(input_fisika)
        else:
            print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100❌ ")
            
def verif_input_kimia(): #validasi nilai kimia harus numerik dan >=0 dan <=100
    verif_status = False
    while verif_status == False :
        input_kimia = input("Masukkan Nilai Kimia : ")
        if (input_kimia.isnumeric() == True):
            if (int(input_kimia) < 0) or (int(input_kimia) > 100) :
                print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100! ❌")
            else: 
                verif_status = True
                return int(input_kimia)
        else:
            print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100 ❌")
       
def verif_input_biologi(): #verifikasi input nilai biologi
    verif_status = False
    while verif_status == False :
        input_biologi = input("Masukkan Nilai Biologi : ")
        if (input_biologi.isnumeric() == True) : #nilai harus numerik
            if (int(input_biologi) < 0) or (int(input_biologi) > 100): 
                print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100 ❌")
            else:
                verif_status = True
                return int(input_biologi)
        else:
            print("❌ Nilai harus bilangan positif dan lebih kecil sama dengan 100 ❌")

def input_nilai_semester(index,semester): #melakukan input untuk seluruh pelajaran pada suatu semester tertentu
    mat = verif_input_matematika()
    fis = verif_input_fisika()
    kim = verif_input_kimia()
    bio = verif_input_biologi()
    students_db[index].update({
        f"{semester}": True,
        f"semester{semester}_matematika" : mat,
        f"semester{semester}_fisika" : fis,
        f"semester{semester}_kimia" :  kim,
        f"semester{semester}_biologi" : bio
    })

def printing_registered_scores_semester(index,semester): #mencetak nilai yang sudah berhasil dimasukkan ke dalam database
    print()
    print()
    print()
    print()
    print(f"{'='*100}")
    print()
    print(f"{'_'*32}Nilai Berhasil dimasukkan ke dalam database.{'_'*24}")
    print()
    print(f"{'_'*25}berikut adalah nilai-nilai yang telah dimasukkan ke dalam database :_______")
    print(f"{45*'='}Semester {semester}{45*'='}")
    print(f"{' '*36}Matematika \t: \t{students_db[index][f'semester{semester}_matematika']}")
    print(f"{' '*36}Fisika \t: \t{students_db[index][f'semester{semester}_fisika']}")
    print(f"{' '*36}Kimia \t: \t{students_db[index][f'semester{semester}_kimia']}")
    print(f"{' '*36}Biologi \t: \t{students_db[index][f'semester{semester}_biologi']}")
    print()
    print(f"{'='*100}")
    print()
        
def print_nilai_sudah_ada(index): #mencetak nilai siswa seluruh semester
    print(f"{130*'='}")
    for key,value in students_db[index].items():
        if "semester" in key:
            print(f"\t |\tPelajaran :\t {key[10:]}{' '*10} \t  Nilai : {value}\t|")
        elif len(key)==1:
            print(f"{' '*40}SEMESTER {key} ")
        else:
            print(f"{' '*9}{key} : {value}")
        print(f"{'_'*83}")
    print(f"{83*'='}")
    if len(students_db[index].keys())==2:
        print("================================================Siswa Ini Belum Memiliki Nilai===============================================")

def input_data_siswa(): #menambah data siswa baru. 
    print("===============================================================================================================================")
    print()
    input_nis_siswa = input("Masukkan Nomor Induk Siswa (NIS) : ")
    while is_student_registered(input_nis_siswa) == True : #loop akan terus berjalan selama nis yang diinput sudah terdaftar di database, maka perlu input nis baru yg belum ada.
        print()
        print(f"{130*'='}")
        print(f"{40*' '}NIS Sudah Terdaftar!, Silahkan Masukkan Dengan NIS yang Berbeda.")
        print(f"{130*'='}")
        print()
        input_nis_siswa = input("Masukkan Nomor Induk Siswa (NIS) : ")
    input_nama_siswa = input("Masukkan Nama Lengkap Siswa : ")
    while (input_nis_siswa.isnumeric()==False) and (len(input_nis_siswa) >= 7) :
        print("NIS HARUS BERUPA ANGKA DAN BERJUMLAH 6 DIGIT!.")
        input_nis_siswa = input("Masukkan Nomor Induk Siswa (NIS) : ")
        input_nama_siswa = input("Masukkan Nama Lengkap Siswa : ")
    tambah_siswa(input_nis_siswa, input_nama_siswa) #memanggil fungsi untuk menambah siswa

def tambah_siswa(NIS, Nama): #Menambah data siswa baru
    students_db.append({
        "NIS": NIS,
        "Nama" : Nama
    })
    print()
    print(f"{130*'='}")
    print(f"{' '*50}[✓] Data Siswa Berhasil Ditambahkan [✓]")
    print(f"{' '*40}Nama : {Nama}, dengan Nomor Induk Siswa (NIS): {NIS}")
    print(f"{130*'='}")

def tampilkan_nilai_siswa(NIS, semester): #Mencetak nilai siswa berdasarkan semester
    stored_counter  = -1
    for i in range(len(students_db)): #melakukan loop sebanyak data list yang ada di database
        for j in students_db[i].values():
            if j == NIS :  #jika value sama dengan nis siswa, maka variabel stored counter menyimpan indexnya, lalu break
                stored_counter = i
                break

    print(f'''================================================================DATA SISWA================================================================
Berikut adalah data siswa dengan keterangan sebagai berikut ini:
    Nama    = {students_db[stored_counter]["Nama"]}
    NIS     = {students_db[stored_counter]["NIS"]}''')
    print(f"=================================================================Semester {semester}========================================================")
    for key,value in students_db[stored_counter].items():
        if (f"semester{semester}") in key:
            print(f"                                                     Pelajaran : {key[10:]}, Nilai : {value}")
            
#====================================================REG FUNC UNTUK MENAMPILKAN HEADER==============================================================
def header_sub_input_1(): #Mencectak header untuk create menu
    print(f'{"="*135}')
    print(f"{' '*50} Menu Penambahan Nilai Siswa")
    print(f'{"="*135}')
    print()
    print(f"{' '*5}Apakah Siswa Sudah Terdaftar? : ")
    print()
    print(f'''{' '*5}○ Masukkan 1 apabila Siswa sudah terdaftar.
{' '*5}○ Masukkan 2 apabila Siswa belum terdaftar.
{' '*5}○ Masukkan 3 untuk kembali [ ↩ ].
    ''')
    print(f'{"="*135}')

def header_read_menu(): #Mencectak header read menu
    print(f'''{130*"="}
{" "*50}{"MENU MENAMPILKAN NILAI"}{" "*32}{jam}
{130*"="}

○ Masukkan 1 Tampilkan seluruh nilai seluruh semester.
○ Masukkan 2 untuk Menampilkan Nilai Siswa Berdasarkan Semester.
○ Masukkan 3 untuk kembali ke menu utama [ ↩ ].

            ''')

def header_update_menu(): #Mencectak header update menu
    print("================================================================================================================================")
    print('''○ Masukkan 1 untuk memperbaharui nilai untuk seluruh pelajaran pada satu semester.
○ Masukkan 2 untuk memperbaharui nilai per pelajaran pada semester tertentu.
○ Masukkan 3 untuk kembali ke menu utama [ ↩ ].
            ''')

def header_delete_menu(): #Mencectak header delete menu
    print(f"=============================================================================================================================={jam}")
    print("==================================================================================================================================Menu Penghapusan Nilai")
    print("========================================================================================================================================================")
    print()
    print('''\t○ Untuk menghapus seluruh data seorang siswa, maka masukkan 1.
\t○ Untuk menghapus nilai siswa berdasarkan semester, maka masukkan 2.
\t○ Untuk kembali ke menu utama, masukkan 3 [ ↩ ].

===================================================================================================================================================
    ''')
def hapus_nilai_siswa(index,semester): #Menghapus nilai per semester siswa berdasarkan indexnya dan semesternya
    print("===================================================================================================================================")
    print()
    for key,value in students_db[index].items():
        if f"semester{semester}" in key :
            print(f"{10*' '}Pelajaran {key[10:]} dengan nilai {value} telah berhasil di hapus!") #slicing key digunakan untuk mengambil nama pelajarannya
    print()
    del students_db[index][f'semester{semester}_matematika']
    del students_db[index][f'semester{semester}_fisika']
    del students_db[index][f'semester{semester}_kimia']
    del students_db[index][f'semester{semester}_biologi']
    del students_db[index][f'{semester}']
    print()
    print(f"=====================================Seluruh Nilai pada semester-{semester} sudah terhapus!===================================================")
 

def hapus_data_siswa(index): #Menghapus data siswa berdasarkan index yang ada pada list
    print(f"Data siswa bernama {students_db[index]['Nama']} dengan NIS {students_db[index]['NIS']} Berhasil dihapus" )
    del students_db[index]
    print()
    print("==============================================================Data Siswa Berhasil Dihapus=======================================================")
    print()

def perbaharui_nilai_per_semester(index, semester):
    mat = verif_input_matematika() #Nilai yang akan diperbaharui divalidasi terlebih dhaulu. apabila sudah OK maka dilakukan input ke dalam database
    fis = verif_input_fisika()
    kim = verif_input_kimia()
    bio = verif_input_biologi()
    students_db[index][f"{semester}"] = True
    students_db[index][f'semester{semester}_matematika'] = mat
    students_db[index][f'semester{semester}_fisika'] = fis
    students_db[index][f'semester{semester}_kimia'] = kim
    students_db[index][f'semester{semester}_biologi'] = bio
    
def perbaharui_nilai_per_pelajaran(index, semester, pilihan):
    #Pertama-tama menyimpan nilai yang sudah ada ke dalam temporary variabel masing-masing pelajaran
    temp_val_mat = students_db[index][f'semester{semester}_matematika']
    temp_val_fis = students_db[index][f'semester{semester}_fisika'] 
    temp_val_kim = students_db[index][f'semester{semester}_kimia'] 
    temp_val_bio = students_db[index][f'semester{semester}_biologi']
    if pilihan == '1' :
        mat = verif_input_matematika() #Memperbaharui nilai matematika
        students_db[index][f"{semester}"] = True
        students_db[index][f'semester{semester}_matematika'] = mat #Menyimpan nilai matematika yang baru dan menyimpan nilai pelajaran lain dengan nilai yang lama
        students_db[index][f'semester{semester}_fisika'] = temp_val_fis #Alasan menyimpan ulang supaya urutan pada list dict tidak teracak
        students_db[index][f'semester{semester}_kimia'] = temp_val_kim
        students_db[index][f'semester{semester}_biologi'] = temp_val_bio
    elif pilihan == '2':
        fis = verif_input_fisika() #Memperbaharui nilai fisika
        students_db[index][f"{semester}"] = True
        students_db[index][f'semester{semester}_matematika'] = temp_val_mat
        students_db[index][f'semester{semester}_fisika'] = fis
        students_db[index][f'semester{semester}_kimia'] = temp_val_kim
        students_db[index][f'semester{semester}_biologi'] = temp_val_bio
    elif pilihan == '3':
        kim = verif_input_kimia() #Memperbaharui nilai kimia
        students_db[index][f"{semester}"] = True
        students_db[index][f'semester{semester}_matematika'] = temp_val_mat
        students_db[index][f'semester{semester}_fisika'] = temp_val_fis
        students_db[index][f'semester{semester}_kimia'] = kim
        students_db[index][f'semester{semester}_biologi'] = temp_val_bio

    elif pilihan == '4': #Memperbaharui nilai biologi
        bio = verif_input_biologi()
        students_db[index][f"{semester}"] = True
        students_db[index][f'semester{semester}_matematika'] = temp_val_mat
        students_db[index][f'semester{semester}_fisika'] = temp_val_fis
        students_db[index][f'semester{semester}_kimia'] = temp_val_kim
        students_db[index][f'semester{semester}_biologi'] = bio
    print("===============================================================================================================")
    print("====================================Nilai Pelajaran berhasil Diperbaharui======================================")
    print("===============================================================================================================")

def show_students_desc():  #Menampilkan daftar siswa secara descending
    list_kosong=[]
    for i in range(len(students_db)):
        for key,value in students_db[i].items():
            if key == "Nama":
                list_kosong.append([students_db[i]["NIS"], value]) #Menyimpan NIS dan Nama siswa ke dalam list kosong
    list_kosong.sort(reverse=True)
    print("="*130)
    print()
    print(f"{'_'*55} TABEL SISWA {'_'*62}")
    print(f"{'_'*130}")
    print(f"{' '*40} Urutan {' '*10} NIS {' '*20} Nama")
    print(f"{'-'*130}")
    for i in range(len(list_kosong)):
        print(f"{' '* 35}       ke-{i+1}. | \t  {list_kosong[i][0]}. \t   |    {list_kosong[i][1]} \t") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*130}")
    print(f"{'_'*104} ORDERED BY NIS DESCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong

def show_students_asc(): #Menampilkan daftar siswa secara ascending
    list_kosong=[]
    for i in range(len(students_db)):
        for key,value in students_db[i].items(): 
            if key == "Nama":
                list_kosong.append([students_db[i]["NIS"], value]) #Menyimpan NIS dan Nama siswa ke dalam list kosong
    list_kosong.sort() #List kosong di sort
    print("="*130)
    print()
    print(f"{'_'*55} TABEL SISWA {'_'*62}")
    print(f"{'_'*130}")
    print(f"{' '*40} Urutan {' '*10} NIS {' '*20} Nama")
    print(f"{'-'*130}")
    for i in range(len(list_kosong)):
        print(f"{' '* 35}       ke-{i+1}. | \t  {list_kosong[i][0]} \t   |    {list_kosong[i][1]} \t") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*130}")
    print(f"{'_'*105} ORDERED BY NIS ASCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong

#RUNNING APLIKASI UTAMA
app()
print(f"{35*'='} Terima kasih telah menggunakan Sistem Akademik Terpadu SMA Purwadhika {45*'='}")



