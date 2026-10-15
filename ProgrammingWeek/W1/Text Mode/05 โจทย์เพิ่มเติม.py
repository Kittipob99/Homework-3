#โจทย์เพิ่มเติมจาก Text book, Think Python:How To Think Like a Computer Scientist, Allen B. Downey, 2024

#Exercise 2.11.2
#Repeating my advice from the previous chapter, whenever you learn a new feature, you should make errors on purpose to see what goes wrong.

#We’ve seen that n = 17 is legal. What about 17 = n?
n = 17
17 = n
#คำตอบ : 17 = n เป็น error เพราะชื่อตัวแปลไม่สามารถเริ่มต้นด้วยตัวเลขได้


#How about x = y = 1?
x = y = 1
#คำตอบ : ใช้งานได้โดยที่ทั้งตัวแปล x และ y จะมีค่าเป็น 1


#In some languages every statement ends with a semi-colon (;). What happens if you put a semi-colon at the end of a Python statement?

#คำตอบ : semi-colon (;) สามารถใช้ได้ใน Python โดยจะทำหน้าที่เป็นตัวแบ่ง statements เช่น:
x = 5; y = 10; print(x + y)
#โดยเราจะได้ Output เป็น 15


#What if you put a period (.) at the end of a statement?

#คำตอบ : ขึ้นอยู่กับ Syntax เช่น
print(x). #เราจะได้ SyntaxError: invalid syntax
#แต่ถ้าเป็น syntax พวกการแทนตัวแปรเช่น
x = 10. #x = 10 ที่เคยเป็น int จะถูกนับเป็น float โดยโปรแกรม


#What happens if you spell the name of a module wrong and try to import maath?
import maath
#คำตอบ : จะไม่สามารถ import ได้ เพราะโปรแกรมจะนับว่า module ที่ชื่อว่า maath ไม่มีอยู่จริง
 

