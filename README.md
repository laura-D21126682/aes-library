# AES Library
Implementation of the 128-bit variant of [AES (Advanced Encryption Standard)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) as a C Library.

### Submodule - AES Python
Python implementation of AES - used as a reference for C library and testing:
+ **Local Directory**: 'python-aes'
+ **Repo URL**: [https//github.com/boppreh/aes](https://github.com/boppreh/aes)

## References
Key references:
1. Creel, “AES Encryption Series”, YouTube, 2015-2016. [Available Online](https://www.youtube.com/playlist?list=PLKK11LigqitiRH57AbtyJyzsfbNfA8nb-)
    - Easy to follow YouTube series on AES encryption in C
2. S. Trenholme, “The AES Encryption Algorithm”, Sam Trenholme’s Webpage, 2005. [Available Online](https://www.samiam.org/rijndael.html)
    - Series of articles which describe various aspects of the Rijndael (AES) encryption algorithm.
3. Rijndael Mixcolumns, Wikipedia, Feb. 06. 2024. [Available Online]( https://en.wikipedia.org/wiki/Rijndael_MixColumns)
    - Galois Multiplication lookup tables used in this project are available here
4. Forma Estudio, “Rijndael (AES) Animation”, Forma Estudio, 2004. [Available Online](https://formaestudio.com/portfolio/aes-animation/)
   </br></br></br>


## Main Encryption Stages:
The following is a high level description of the three main Rijndael AES encryption functions as implemented in this project:
#### Sub-Bytes Encryption:
- Each byte value in a block is substituted with a corresponding S-box lookup value.
- The current byte value of the block acts as the S-Box to get the new byte value.
</br></br></br>
![sub-bytes](/readme_images/sub-byte.png)

#### Shift-Rows Encryption:
- Each byte of each row is shifted to the left (except for the first row).
- This implmentation simplifies calculations through Galois multiplication lookup tables and XOR operations
- First row: no shift
- Second row: Shift left 1 position
- Third row: Shift left 2 positions
- Fourth row: Shift left 3 positions
   </br></br></br>
![sub-bytes](/readme_images/shift-row.png)
   </br></br></br>

#### Mix-Columns Encryption:
- Transforms the matrix, column by column
- Each byte of each column is transformed through Matrix multiplication in Rijndael's Galois field
- This method is simpthrough the use of Galois multiplication lookup tables and XOR operations
  </br></br></br>
![sub-bytes](/readme_images/mix-column.png)
