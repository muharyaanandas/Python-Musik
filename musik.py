class musik:
    judul = ''
    penyanyi = ''
    
    def __init__(self,penyanyi,judul):
        print("NAMA PENYANI YANG TAMPIL ADALAH :")
        self.penyanyi = penyanyi
        self.judul = judul
        
        
    def tampil(self):
      return print("NAMA PENYAYI : ",self.penyanyi,"\nJUDUL : ",self.judul)
       

arya = musik("HINDIA"," RUMAH KE RUMAH")
arya.tampil()