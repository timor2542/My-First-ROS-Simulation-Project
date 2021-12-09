# FRA502 Service Robot Project - Phase III: Final Presentation
### **ชื่อโครงงาน:**

#### การจำลองหุ่นยนต์เสิร์ฟอาหาร 1 ตัว ให้กับผู้ป่วยภายในพิเศษในโรงพยาบาล
### **อธิบายภารกิจโดยย่อ:** 
เริ่มต้นหุ่นยนต์จะอยู่ห้องพักหุ่นยนต์ หน้าที่ของหุ่นยนต์คือการเสิร์ฟอาหารให้กับผู้ป่วยทุกมื้อเช้า กลางวัน และเย็น โดยสั่งการคำพูดไปยังตัวหุ่นยนต์ให้มารับอาหารที่ห้องครัวเป็นอย่างแรก และบอกหมายเลขห้องของผู้ป่วยที่ต้องการนำไปส่ง
### **สร้างโดย:**
นายกฤตเมธ ถาวงศ์ รหัสนักศึกษา 61340500003 FIBO KMUTT FRAB5
## 1. OS and ROS
* OS: Ubuntu 20.04.3 LTS (Focal Fossa)
* ROS: Noetic Ninjemys
## 2. Dependencies
* actionlib
* actionlib_msgs
* anytree
* gazebo_ros
* geometry_msgs
* move_base_msgs
* nav_msgs
* pyaudio
* rospy
* sensor_msgs
* sound_play
* speech_recognition (Google Web Speech API)
* std_msgs
* tf
## 3. What I get from the basic learning goals.
* สร้างสภาพแวดล้อม (Environment) และโลก (World) ด้วยโปรแกรม Gazebo แล้วบันทึกให้เป็นไฟล์ URDF
* เขียนโปรแกรมสร้างการจำลองหุ่นยนต์แบบ Differiantial Drive 2 ล้อ แล้วบันทึกเป็นไฟล์ XACRO
* ใช้ movebase เป็น package ในการทำ Navigation
* ใช้ Laser ของ hokyo เป็น Topic ในการทำ Gmapping เพื่อสร้างแผนที่ และบันทึกเป็นไฟล์ pgm
* มี Node ในการสั่งการด้วยคำพูดจดจำเสียงที่เรียกว่า Speech Recognition ในทีนี้จะใช้ตัว Google Web Speech API เขียนด้วยภาษา Python
## 4. Commands
* คำสั่งเปิดตัว Gazebo และ Rviz เพื่อทำการ Gmapping
```
roslaunch my_robosim_project ifooddifbotv1_gmapping.launch
```
* คำสั่งบันทึกแผนที่ (Map) เมื่อสำรวจสภาพแวดล้อมทั้งหมดในแผนที่ที่ถูกสร้างโดยจากการ Gmapping
```
rosrun map_server map_server mymap.yaml
```
* คำสั่งเปิดตัว Gazebo และ Rviz เพื่อทำการ Navigation
```
roslaunch my_robosim_project ifooddifbotv1_navigation.launch
```
* คำสั่งรัน Node เพื่อสั่งการด้วยเสียงไปยังตัวหุ่นยนต์
```
rosrun my_robosim_project voice_command.py
```
## 5. Run project step by step
### **ภาษาที่ใช้เป็นคำสั่ง :**
ภาษาอังกฤษ (English)


5.1 พิมพ์คำสั่ง
```
roslaunch my_robosim_project ifooddifbotv1_navigation.launch
```
เพื่อเปิดตัว Gazebo และ Rviz แล้วทำการ Navigation


5.2 พิมพ์คำสั่ง
```
rosrun my_robosim_project voice_command.py
```
เพื่อรัน Node เพื่อสั่งการด้วยเสียงไปยังตัวหุ่นยนต์


5.3 หุ่นยนต์จะอยู่ห้องพักหุ่นยนต์ จากนั้นหุ่นยนต์ก็จะส่งเสียงด้วยคำถามว่า "Where should I go? Kitchen?"
  * ถ้าคนสั่งพูดว่า "Kitchen" หุ่นยนต์จะตอบกลับว่า "Kitchen, confirmed!" และ "I'm going to kitchen." ตามลำดับ
  * ถ้าคนสั่งพูดว่า "101", "102", "103", "104" หรือ "Office" นี้ หุ่นยนต์จะตอบกลับว่า "I don't get food yet!"
  * ถ้าคนสั่งพูดนอกเหนือจาก 2 กรณีข้างต้นนี้ หุ่นยนต์จะตอบกลับว่า "No goal." และวนการทำงานขั้นตอนที่ 5.3 อีกครั้ง
  
  ขั้นตอนนี้เป็นขั้นตอนการบังคับสั่งการให้ตัวหุ่นยนต์ไปรับอาหารที่ครัวก่อนเป็นอันดับแรก เนื่องจากหุ่นยนต์ยังไม่ได้รับอาหาร

5.4 เมื่อหุ่นยนต์เดินทางไปถึงห้องครัวเรียบร้อย หุ่นยนต์จะส่งเสียงตอบกลับมาว่า "Reached to kitchen." และถามว่า "Which room should I go?" ตามลำดับ
  * ถ้าคนสั่งพูดว่า "101", "102", "103", "104" หรือ "Office" นี้หุ่นยนต์จะตอบกลับว่า "\{ห้องที่ถูกเอ่ยชื่อ\}, confirmed!" และ "I'm going to \{ห้องที่ถูกเอ่ยชื่อ\}." ตามลำดับ
  * ถ้าคนสั่งพูดว่า "Kitchen" หุ่นยนต์จะตอบกลับว่า "I already have food yet!" 
  * ถ้าคนสั่งพูดนอกเหนือจาก 2 กรณีข้างต้นนี้ หุ่นยนต์จะตอบกลับว่า "No goal." และวนการทำงานขั้นตอนที่ 5.4 อีกครั้ง
  
  ขั้นตอนนี้ให้ถือว่าตัวหุ่นยนต์ที่ไปถึงห้องครัวได้รับอาหารเป็นที่เรียบร้อย และคนสั่งต้องเลือกห้องที่ตัวหุ่นยนต์ส่งอาหารไปให้
  
  ถ้าเลือกห้องเดิม \(ก็คือ ห้องครัว \) หุ่นยนต์จะโต้กลับว่า เราได้อาหารเป็นที่เรียบร้อยแล้ว

5.5 เมื่อหุ่นยนต์เดินทางไปถึงห้องตามที่คนสั่งเลือกห้องเรียบร้อยแล้ว หุ่นยนต์จะส่งเสียงตอบกลับมาว่า "Reached to \{ห้องที่ถูกเอ่ยชื่อ\}." และพูดว่า "Task completed! I will go back to my station." ตามลำดับ
  
  ขั้นตอนนี้ให้ถือว่าตัวหุ่นยนต์ที่ไปถึงห้องตามที่คนสั่งเลือกห้องให้อาหารให้กับผู้ป่วยหรือเจ้าหน้าที่เป็นที่เรียบร้อย และให้ถือว่างานเสร็จสิ้น (Task is completed.) จากนั้นหุ่นยนต์ก็กลับเข้าสู่ห้องพักหุ่นยนต์เหมือนเดิมโดยอัตโนมัติทันที สุดท้ายการทำงานจะวนไปขั้นตอนที่ 5.3

## 6. Problems
* เมื่อสร้างหน้าต่างให้กับบนกำแพงของตึกโรงพยาบาล มันทำให้โปรแกรม Gazebo ค้าง และถูกปิดโปรแกรมนี้โดยอัตโนมัติทันที
* บางครั้งเมื่อหุ่นยนต์เคลื่อนที่ถึงจุดหนึ่ง หุ่นยนต์จะหมุนรอบตัวเองก่อนจะหยุด

## 7. Resources
* [Video Link](https://youtu.be/yyTDNPj7Eag)
* [Gmapping and Navigation Configuration Folder Link](https://github.com/timor2542/My-First-ROS-Simulation-Project/tree/main/my_robosim_project/config)
* [Recorded Map Folder Link](https://github.com/timor2542/My-First-ROS-Simulation-Project/tree/main/my_robosim_project/maps)
* [Base Part (Mesh of Robot) was made by myself on Solidwork Link](https://github.com/timor2542/My-First-ROS-Simulation-Project/tree/main/my_robosim_project/meshes)
* [ROS Graph Nodes and Topics](https://raw.githubusercontent.com/timor2542/My-First-ROS-Simulation-Project/main/Assets/rosgraphnodeandtopicactive20211103.svg)
