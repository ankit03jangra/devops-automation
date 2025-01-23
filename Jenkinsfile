pipeline {
    agent any
    tools{
        maven 'maven_3_8_4'
    }
    environment {
        OPENAI_API_KEY = credentials('openai-api-key')
    }
    stages{
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        /* stage('Install Dependencies') {
            steps {
                sh 'C:/Users/Ankit_Jangra/AppData/Local/Programs/Python/Python312/python.exe -m pip install -r requirements.txt'
            }
        } */
        stage('Build Maven'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ankit03jangra/devops-automation']]])
                sh 'mvn clean install'
            }
        }
        stage('AI Feedback'){
            steps{
                script {
                    sh 'C:/Users/Ankit_Jangra/AppData/Local/Programs/Python/Python312/python.exe scripts/ai_feedback.py'
                }
            }
        }
        stage('Post Comment to PR') {
            steps {
                script {
                    sh 'C:/Users/Ankit_Jangra/AppData/Local/Programs/Python/Python312/python.exe scripts/post_comments_to_pr.py'
                }
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
    post {
            success {
                echo 'Workflow completed successfully.'
            }
            failure {
                echo 'Workflow failed.'
            }
        }
}