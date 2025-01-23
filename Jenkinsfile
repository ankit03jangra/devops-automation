pipeline {
    agent any
    tools{
        maven 'maven_3_8_4'
    }
    stages{
        stage('Build Maven'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ankit03jangra/devops-automation']]])
                sh 'mvn clean install'
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t ankit03jangra/devops-integration .'
                }
            }
        }
        stage('Push image to Hub'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                        sh "docker login -u ankit03jangra@gmail.com -p ${dockerhubpwd}"
                    }
                    sh 'docker push ankit03jangra/devops-integration'
                }
            }
        }
    }
}