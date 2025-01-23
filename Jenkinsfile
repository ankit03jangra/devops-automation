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
    }
}