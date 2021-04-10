pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
        app_version = '0.1'
    }
    stages {
        // stage('Test'){
        //     steps{
        //         sh "bash pytest.sh" // write bash script that tests all microservices in 1 container.
        //     }
        // }
        stage('Build'){
            steps{
                sh 'docker-compose build'
            }
        }
        stage('Push'){
            steps{
                script{
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                        sh "docker login -u ${docker-hub-credentials_USR} -p ${docker-hub-credentials_PSW} && docker-compose push"
                    }
                }
            }
        }
        stage('Config'){
            steps{
                sh "cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }
        stage('Deploy'){
            steps{
                sh "bash deploy.sh"
            }
        }
    }
}
