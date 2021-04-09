pipeline{
    agent any
    environment{
        // DATABASE_URI = credentials("DATABASE_URI")
        app_version = '0.1'
        rollback = 'false'
    }
    stages {
        // stage('Test'){
        //     steps{
        //         sh "bash pytest.sh" // write bash script that tests all microservices in 1 container.
        //     }
        // }
        stage('Build'){
            steps{
                script{
                    image_1 = docker.build("dbrownless1/project_02_service_01")
                    image_2 = docker.build("dbrownless1/project_02_service_02")
                    image_3 = docker.build("dbrownless1/project_02_service_03")
                    image_4 = docker.build("dbrownless1/project_02_service_04")
                }
            }
        }
        stage('Push'){
            steps{
                script{
                    docker.withRegistry('https://registry.hub.docker.com', docker-hub-credentials){
                        image_1.push("${env.app_version}")
                        image_2.push("${env.app_version}")
                        image_3.push("${env.app_version}")
                        image_4.push("${env.app_version}")
                    }
                }
            }
        }
        // stage('Config'){
        //     steps{
        //         sh "cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory playbook.yaml"
        //     }
        // }
        stage('Deploy'){
            steps{
                // sh "bash deploy.sh"
                sh "docker-compose pull && docker-compose up -d"
            }
        }
    }
}
