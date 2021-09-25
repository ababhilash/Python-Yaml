pipeline {
    agent any
    stages{
        stage ('SCM chkout-1'){
            steps{
                git branch: 'main', credentialsId: 'b7bb71f2-0269-4e2c-b855-edceee0ba06f', url: 'https://github.com/ababhilash/Python-Yaml'
            }
        }
        stage ("Dynamically write dictionary variables") {
            steps{
                script{
                        def amap = ['veg': [ 'tomato': 2, 'potato': 2]]
                        sh 'rm -rf datas.yaml' 
                        writeYaml file: 'datas.yaml', data: amap
                        def read = readYaml file: 'datas.yaml'
                        sh 'cat datas.yaml >> items.yaml'
                }
            }
        }
        stage ("Output of yaml file") {
            steps{
                sh "cat items.yaml"
            }    
        }    
    }
}
