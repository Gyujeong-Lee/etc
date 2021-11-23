# STS 설치 및 실행방법



### 1. 개발 환경 세팅

1. JDK 설치 및 환경변수 세팅

   - [OPEN JDK Zulu](https://www.azul.com/downloads/?package=jdk#download-openjdk) 에서 Open JDK 다운로드 (Java 8 버전) 

   ![image-20210727104724344](STS 설치 및 실행방법.assets/image-20210727104724344.png)

   .msi로 받은 후 설치하시면 됩니다.

   

   - 내 PC - 속성 - 고급 시스템 설정 - 환경 변수

   ![image-20210727105016327](STS 설치 및 실행방법.assets/image-20210727105016327.png)

   

   - 시스템 변수 - 새로 만들기 - JAVA_HOME 추가

     ![image-20210727105128420](STS 설치 및 실행방법.assets/image-20210727105128420.png)

     

   - 시스템 변수 - Path 편집 - **%JAVA_HOME%\bin** 추가

     ![image-20210727105302732](STS 설치 및 실행방법.assets/image-20210727105302732.png)

     

   - 명령 프롬프트 창에서 설치 확인 (java -version)

     ![image-20210727105346438](STS 설치 및 실행방법.assets/image-20210727105346438.png)



2. STS 설치

   - [STS 공식 홈페이지](https://spring.io/tools/) 에서 Spring Tools 다운로드

     ![image-20210727105627905](STS 설치 및 실행방법.assets/image-20210727105627905.png)

   - 다운로드 파일 압축 해제 후 contents.zip 압축풀기

     ![image-20210727105811104](STS 설치 및 실행방법.assets/image-20210727105811104.png)

     

   - SpringToolSuite4.exe 실행 후 Help의 Eclipse Marketplace

     ![image-20210727105945636](STS 설치 및 실행방법.assets/image-20210727105945636.png)

     

   - sts 검색 후 Spring Tools 3 3.9.14 인스톨

     ![image-20210727110110603](STS 설치 및 실행방법.assets/image-20210727110110603.png)

     

   - File - Open projects from file system 에서 backend 폴더 import

     ![image-20210727110358513](STS 설치 및 실행방법.assets/image-20210727110358513.png)

     import source 에서 directory에서 backend 폴더 선택

     ![image-20210727110506364](STS 설치 및 실행방법.assets/image-20210727110506364.png)

     

   - backend - src/main/resources에 jdbc.properties 파일 추가 (파일은 단톡방에 올려져 있음)

     ![image-20210727110729378](STS 설치 및 실행방법.assets/image-20210727110729378.png)



### 2. 서버 실행

backend 우클릭 - Run As - Spring boot app

![image-20210727110857875](STS 설치 및 실행방법.assets/image-20210727110857875.png)

![image-20210727111015464](STS 설치 및 실행방법.assets/image-20210727111015464.png)



이미 Vue 서버가 켜져 있는 경우 port가 겹쳐 error가 날 수 있음

그 때는 Vue 서버 실행 시

yarn serve --port 3000 으로 vue 프로젝트를 다른 포트로 실행