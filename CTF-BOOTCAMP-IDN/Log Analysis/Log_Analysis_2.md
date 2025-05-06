# Log Analysis 2

- [Challenge information](#challenge-information)
- [Solve](#solve)
- [FLAG](#flag)

## Challenge information

```text
awas, hati-hati, pelan-pelan, ada .....

Format Flag : IDN_CTF{jawaban}

Author : Aditya Firman Nugroho
```

## Solve
Sama Seperti sebelumnya saya mencoba memfilter hasil capturenya dengan
```text
frame contains "IDN"
```

Dan saya menemukan record yang lumayan asing dengan protocol HTTP yang sendang melakukan post ke server
saat saya cek response yang dilakukannya saya menemukan FLAGnya

![Screenshot 2025-05-06 120233](https://github.com/user-attachments/assets/b38d760b-aea6-42d7-8d6e-16a908979da0)



## FLAG
IDN_CTF{M4l2Wre_S3ReM}
