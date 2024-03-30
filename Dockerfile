FROM debian
RUN apt-get update && apt-get install wget default-jre-headless -y
RUN wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure_2.27.0-1_all.deb
RUN dpkg -i allure_2.27.0-1_all.deb
EXPOSE 39533
ENTRYPOINT ["allure", "serve", "-p", "39533", "/root/results"]