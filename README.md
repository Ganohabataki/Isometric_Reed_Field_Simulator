# Isometric Reed Field Simulator

### In a nutshell
 - Run it in the terminal
 - Real-time trigonometric coordinates simulator, with the form of windy field of reed.
 - Pseudo 2.5D(isometric projection)
 - It simulates x and y as time goes(t)

A procedural animation project that visualizes a wind-swept reed field using trigonometric functions and isometric projection in a terminal environment.

### 1. Wind Force (Physics)

* **Trigonometric Wave Summation**: Instead of simple random values, it uses the superposition of three different sine and cosine waves to create a natural atmospheric flow.
* **Continuous Flow**: Since values oscillate smoothly between -1 and 1, it achieves a seamless, waving motion of the reeds without abrupt jumps.

### 2. Wind to Reed (Data Mapping)

* **Real-time Mapping**: The calculated wind force (float) is mapped to specific ASCII characters (`.:!|/(...`) in real-time.
* **Dynamic Highlighting**:
* **Strong Wind**: Areas with higher wind force are rendered in **Bright Yellow**, simulating light reflecting off the swaying reed tops.
* **Weak Wind**: Areas with calmer air are rendered in **Dim Green**, providing depth and shadow to the field.



### 3. Isometric Projection (Spatial Depth)

* **2.5D Realization**: By transforming 2D grid coordinates into an isometric perspective, it provides a sense of 3D depth within a flat terminal window.
* **Wide View**: The coordinate system is optimized with a wide aspect ratio to create an expansive, panoramic field of reeds.

---

# 등각 투사 갈대밭 시뮬레이터 (Isometric Reed Field Simulator)

터미널 환경에서 삼각함수와 등축 투영법(Isometric Projection)을 활용해 바람에 흔들리는 갈대밭을 구현한 **절차적 애니메이션(Procedural Animation)** 프로젝트입니다.

### 1. Wind Force (바람의 물리력)

* **삼각함수 파동 중첩**: 단순한 무작위 값이 아닌, 서로 다른 주기와 방향을 가진 3개의 사인/코사인 파동을 중첩하여 자연스러운 기류를 생성합니다.
* **연속적인 흐름**: 값이 -1에서 1 사이를 부드럽게 오가기 때문에, 끊김 없이 일렁이는 갈대밭의 움직임을 자연스럽게 묘사합니다.

### 2. Wind to Reed (갈대의 시각화)

* **실시간 매핑**: 계산된 바람의 세기(실수 값)를 실시간으로 그에 맞는 ASCII 문자(`.:!|/(...`)로 변환하여 출력합니다.
* **동적 하이라이트**:
* **강한 바람**: 바람을 강하게 받아 갈대가 크게 휘어지는 부분은 **밝은 노란색**으로 표현하여 빛의 반사를 묘사합니다.
* **잔잔한 바람**: 바람이 적은 곳은 **짙은 녹색**으로 처리하여 들판의 입체감과 그림자를 표현합니다.



### 3. Isometric Projection (공간감)

* **2.5D 공간감 구현**: 평면적인 2차원 그리드 좌표를 등축 투영 공식으로 변환하여, 터미널 창 안에서 깊이감 있는 3D 시점을 제공합니다.
* **파노라마 뷰**: 가로세로 출력 비율을 최적화하여 끝없이 펼쳐진 듯한 넓은 평행사변형 형태의 갈대 평원을 구현했습니다.

---

**다음에 해볼 만한 작업:**
작성하신 README에 이 프로그램의 실행 방법(예: `python main.py`)이나 **조작법(q를 눌러 종료 등)** 섹션을 추가해 볼까요? 혹은 터미널 환경에서 더 멋진 연출을 위해 **시간의 흐름(낮과 밤)에 따라 색상이 변하는 기능**을 추가해 보시는 건 어떠신가요?