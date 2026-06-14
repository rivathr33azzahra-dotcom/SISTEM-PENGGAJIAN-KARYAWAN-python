from abc import ABC, abstractmethod

class Karyawan(ABC):

    def __init__(self, nama, nip):
        self.__nama = nama
        self.__nip = nip

    def get_nama(self):
        return self.__nama

    def get_nip(self):
        return self.__nip

    @abstractmethod
    def hitung_gaji(self):
        pass