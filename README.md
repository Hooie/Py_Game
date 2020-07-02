## SPACE WAR 게임은 pygame 모듈을 바탕으로 제작되었습니다.

# 실행 방법
1. 우측 상단에 code -> DownloadZip 버튼을 통해 게임 파일을 다운로드 후 압축 해제를 합니다.
2. 압축 해제 후 생성된 폴더 내부의 SPACEWAR.py를 실행합니다.
3. 게임을 즐깁니다.
* images 와 sounds 폴더는 절대 건들지 않아야합니다.
* images와 sounds 폴더 내에는 게임 리소스로 활용되는 사진과 효과음이 있습니다.



# 조작법
* 플레이어는 하단에 있는 초록색 비행기를 조종합니다.

* ←방향키: 좌측으로 이동 / spacebar: 미사일 발사 / →방향키: 우측으로 이동 / LCTRL: 게임 3초간 일시정지

# 게임 진행 방식
* 세 종류의 적군이 랜덤으로 등장합니다.

* 플레이어는 떨어지는 두 종류의 운석을 피해 다가오는 적군을 미사일로 격추시켜야 합니다.

* 적군을 격추시킬 때마다 좌측상단 Enemy Defeated 점수가 오릅니다.

* 적군을 격추시킬 때마다 다가오는 적군의 속도가 0.1픽셀씩 빨라집니다.

* 운석은 종류에 상관없이 파괴하지 못합니다.

* 운석의 판정에는 버그가 있습니다.          
(아무 조작을 하지 않는 상태에서 어두운 원형운석을 통과할 수 있는 버그 / 운석의 왼쪽 판정 면적이 오른쪽 판정 면적보다 큰 버그가 있습니다)

# 게임 패배 기준
* 적군 및 운석에 피격당하면 즉시 게임오버입니다.

* 적군이 화면 최하단까지 도달하면 우측 상단 Enemy Passed 점수가 1점씩 오르며, 해당 점수가 5점이 되는 순간 게임 오버가 됩니다.

* 게임 오버가 된 후 3초후 자동으로 재시작합니다.

### 게임 사운드가 조금 클 수 있으므로 적당히 조절해주세요.

 
