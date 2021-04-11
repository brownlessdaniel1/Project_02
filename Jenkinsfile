pipeline{
    agent any
    environment{
        VERSION = '2.5.1'
        rollback = 'true'
        replicas = 10
        DATABASE_URI = credentials("DATABASE_URI")
        docker_password = credentials("docker_password")
        docker_username = credentials("docker_username")
    }
    stages {
        stage('Test'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh "bash testing.sh"
                    }
                }
            }
        }
        stage('Build'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh "docker-compose build --parallel --build-arg VERSION=${VERSION}"
                    }
                }   
            }
        }
        stage('Push'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh "docker login -u ${env.docker_username} -p ${env.docker_password} && docker-compose push"
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
