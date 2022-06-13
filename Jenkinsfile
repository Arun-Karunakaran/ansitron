pipeline {
    agent {label 'ansitron'}

    stages {
        stage('Build') {
            steps {
                sh 'pwd'
                dir("${env.WORKSPACE}/ansitron/ansitron-core"){
                    script {
                        if (fileExists("${env.WORKSPACE}ansitron/ansitron-core/setup.py")) {
                            echo "File setup.py found"
                            sh "python3 setup.py sdist bdist_wheel"
                        }
                    }
                }
            }
        }
    }
}
