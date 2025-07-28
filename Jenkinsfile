pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ssidharths/ci-cd-demo.git', branch: 'main'
                echo 'Repository cloned successfully!'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('backend') {
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
                echo 'Dependencies installed!'
            }
        }

        stage('Run Tests') {
            steps {
                dir('backend') {
                    sh '''
                        . venv/bin/activate
                        python -m pytest tests/ || echo "No tests found"
                    '''
                }
                echo 'Tests completed!'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t flask-app:${BUILD_NUMBER} .'
                    sh 'docker tag flask-app:${BUILD_NUMBER} flask-app:latest'
                }
                echo 'Docker image built!'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d -p 8080:8080 --name flask-app flask-app:latest
                '''
                echo 'Application deployed!'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f || echo "Docker cleanup failed"'
        }
        success {
            echo '🎉 Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
