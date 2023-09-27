<div align="center">

# โปรแกรมจัดการดันเจียน

</div>

### การทำงานของโปรแกรมนี้
- ให้ทำการวนซ้ำสามารถเลือกได้เรื่อยๆจนกว่าจะพิมพ์ 0
```
         <|Manage The Dungeon|>         
[1] Add items to the dungeon
[2] View items in the dungeon
[3] Let the hero enter the dungeon
[0] Close the dungeon
Choice : 0
```

# อธิบาย
- Add items to the dungeon คือการเพิ่มข้อมูลเข้าไปในดันเจี้ยน ให้กรอกข้อมูลเก็บไว้เป็น dict แบบ global ดังนี้
```
{'Item_name': '','Price':0,'Amount': 0}
```
การแสดงผลก็จะเป็นเป็นดังนี้
```
Enter Item name : Sword
Enter Price : 200
Enter Amount : 1
-------
Sword 200G 1x
```
หรือ
```
Enter Item name : HP
Enter Price : 50G
Enter Amount : 1
-------
HP 50G 1x
```
```
Enter Item name : HP
Enter Price : 50G
Enter Amount : 1
-------
HP 50G 1x
```
```
Enter Item name : HP
Enter Price : 50G
Enter Amount : 1
-------
HP 50G 1x
```
- View items in the dungeon คือการแสดงไอเทมทั้งหมดในดันเจี้ยนแสดงให้รูปแบบดังนี้
```
- Sword 200G 1x
- HP 50G 2x
```
- Let the hero enter the dungeon คือการให้ผู้เล่นเข้ามาดันเจี้ยนโดยให้มีลักษณะการทำงานดังนี้
```
Hero receives 1x Sword item.
```
หรือ
```
Hero receives 1x HP item.
```
     * ผู้เล่นจะได้รับไอเทมจะได้มาจากการสุ่มไอเทม และสุ่มจำนวนของไอเทม
     * เมื่อผู้เล่นได้รับไอเทมไปแล้วไอเทมที่อยู่ในคลังของดันเจี้ยนชิ้นนั้นก็จะถูกลดลงไปตามจำนวนที่ผู้เล่นได้ไป

# ฟังค์ชั่น
- จะมีฟังก์ชันที่มีมาให้
```python
    def match_funct(choice:int):
        match choice:
            case 1:
                pass

    def run_dungeon():
        while True:
            print('<|Manage The Dungeon|>'.center(40," "))
            print('[1] Add items to the dungeon')
            print('[2] View items in the dungeon')
            print('[3] Let the hero enter the dungeon.')
            print('[0] Close the dungeon.')
            choice = input('Choice : ')
            match_funct(choice)
```
