<div align="center">

<!-- logo -->
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/title_dark.png"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/title_light.png"
  >
  <img
    src="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/title_light.png"
    width="600"
    alt="최적 정지 이론 모의 실험"
  >
</picture>

### 최적 정지 이론 모의 실험

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/help_dark.png"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/help_light.png"
  >
  <img
    src="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/main/help_light.png"
    width="400"
    alt="도움말"
  >
</picture>

[![GitHub Release](https://img.shields.io/github/v/release/HYB1022/opti_stopping_test?include_prereleases)](https://github.com/HYB1022/opti_stopping_test/releases)
[<img src="https://img.shields.io/badge/프로젝트 기간-2026.6.9~2026.6.16-fab2ac?style=flat&logo=&logoColor=white" />]()

</div> 
위 단추들이 제대로 표시되지 않는다면, 페이지를 새로고침 하거나, 잠시 후에 다시 접속 하십시오.

release는 v1.x.x 형식으로 표시되어야 합니다.

이 사이트는 다크모드를 지원합니다. 다만 라이트모드에 최적화 되어있기 때문에, 라이트모드 사용을 권장합니다.

## 📝 소개
진로 독서 활동 기록지용 리포지토리입니다.

<img src="https://raw.githubusercontent.com/HYB1022/opti_stopping_test/refs/heads/main/optimal_stopping_graph.png" width="500"/>

```
37% 법칙 작동 원리이 법칙은 후보의 총수 N을 알고 있으며, 한번 지나친 후보는 다시 선택할 수 없는 상황을 전제로 합니다.
1단계 (탐색): 전체 기간의 약 37%에 해당하는 기간(또는 후보 수) 동안은 무조건 결정을 보류하고 관찰합니다.
이 단계에서 관찰된 가장 우수한 대상을 나의 '기준선'으로 삼습니다.
2단계 (선택): 탐색 단계가 끝난 후부터는, 앞서 설정한 기준선보다 더 뛰어난 대상이 나타나는 즉시 선택합니다.
```
그래프의 y축은 최고 후보를 뽑는 데 성공한 확률을 의미합니다. 즉, 같은 조건으로 실험을 여러 번 반복했을 때 전체 후보 중 가장 우수한 대상을 선택한 비율입니다.

## 🧰 기능
1. 관찰 비율(1~99%)에 따른 최적 성공 확률 계산
2. 시뮬레이션 결과를 그래프로 시각화
3. 최적 정지 이론의 이론값과 실험값 비교
## ❓ How to?
1. https://www.python.org/downloads/ 에서 Python 설치 관리자를 다운로드한 후, 실행하여 Python을 설치합니다.
2. Win -> CMD를 검색하여 실행한 후, 다음 명령어를 입력합니다.

```cmd
pip install matplotlib
pip install pandas
```
3. 릴리즈 탭에 있는 Source code를 저장한 후, main.py를 실행하면 됩니다.

## 🤗 기여자
- 방현우 (@HYB1022) - 기획, 프롬프트, 깃헙 페이지 제작
- ChatGPT (@OpenAI) – simulation design, debugging, documentation support
