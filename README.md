# Deployment of Microservices Application in Kubernetes C6 Assignment Group-11
This is GitHub repository of Microservices Assignment designed by Group 11

# Project Title 

# Microservices Application for fetching Student Details 

This project aims to develop microservices for student_score details using database per service design pattern.The data will be stored and retrieved from SQLite database in JSON format. The API is open to all the users who have access to the codebase.


# Technology Stack

This project uses Django to develop endpoints for students and their scores. It uses SQLite Database to store the data received from endpoints. The project is continuation of previous assignment which aims at deploying the application on kubernetes.

# Project Screenshots

## Deployment in Kubernetes using Minikube 
![minikube-dashboard-deployment](https://user-images.githubusercontent.com/94062868/182042454-2e3ff2c5-0372-4690-a962-b3bd4e4ba106.png)
![deployment-view](https://user-images.githubusercontent.com/94062868/182042459-24614fd7-fe33-4fe2-b87a-57e5ad73b615.png)
![pods-with-metrics](https://user-images.githubusercontent.com/94062868/182042478-4f39e677-dbdc-4154-956a-8a1e76bb80d8.png)
![replica-sets](https://user-images.githubusercontent.com/94062868/182042496-df2b4abb-e83a-48d6-840d-9c9d91df8eed.png)
![services-view](https://user-images.githubusercontent.com/94062868/182042686-affb4ad6-e161-447a-bdec-26d127c2bc51.jpeg)
![kubernetes-namespaces](https://user-images.githubusercontent.com/94062868/182042506-46b2771a-338b-4096-9c9a-dc10bc7d1426.png)

## Rolling out Deployment 
![rollout-update](https://user-images.githubusercontent.com/94062868/182042723-a2699fef-4aa8-47e9-b269-4f7dc940181e.png)
![rollout-in-progress](https://user-images.githubusercontent.com/94062868/182042733-434ec093-00bb-4dde-b546-c88a376b9da0.png)
![rollout-new-update](https://user-images.githubusercontent.com/94062868/182042730-1abd5e9b-2f68-4313-a709-f9196855368d.png)

## Deployed on Kubernetes
![student-view](https://user-images.githubusercontent.com/94062868/182042764-f73810ca-72c1-4bb1-b879-82fb65ca3f2c.png)
![student-deployment-view](https://user-images.githubusercontent.com/94062868/182042791-d40ce4fb-d88c-4e81-aabd-9417a9292152.png)
![scores-view](https://user-images.githubusercontent.com/94062868/182042781-c9074b95-59e2-482e-ac16-072a5feda1ff.png)
![scores-deployment-view](https://user-images.githubusercontent.com/94062868/182042806-9f61951a-8da2-4912-98b3-c44a63814962.png)
![all-details-domain-deployment](https://user-images.githubusercontent.com/94062868/182042783-e14f6c3f-3adb-4f13-a981-229fa82b0aa5.png)
![all-details-view](https://user-images.githubusercontent.com/94062868/182043825-fef7820d-44fe-46fe-ad77-eace4be6cfc2.png)

## Horizontal Pod Auto-Scaling of Deployment 
![pods-with-cpu-usage](https://user-images.githubusercontent.com/94062868/182042874-afb60ae6-86af-4cc0-9d75-ed29b560c331.png)
![Screenshot (154)](https://user-images.githubusercontent.com/94062868/182043827-8fbc03b4-6537-42d6-bc55-41945339e323.png)

## Events in kubernetes cluster 
![services-view](https://user-images.githubusercontent.com/94062868/182043844-c03c4a33-9d44-43b0-867f-8ad92742e10f.png)


## Student's Scores Details Application Output Screenshots
![student_domain_endpoints](https://user-images.githubusercontent.com/94062868/170861117-4e51ff94-e2bf-4355-8bd7-6a3711e53ffa.PNG)
![scores_domain_endpoints](https://user-images.githubusercontent.com/94062868/170861125-06ef4df2-e9a0-4f48-bfd9-5a3442248f17.PNG)
![all_details_endpoint](https://user-images.githubusercontent.com/94062868/170861129-32e45e42-fbd8-4a02-9a73-461348531d65.PNG)
![student_list](https://user-images.githubusercontent.com/94062868/170861089-6e851a7b-4851-4ee3-a064-210bb705e4ff.PNG)
![student_list_all](https://user-images.githubusercontent.com/94062868/170861091-19162ce8-374a-40b9-ac1c-caf927daaa75.PNG)
![student_list_success](https://user-images.githubusercontent.com/94062868/170861094-addf57de-db12-418c-aa5d-27467c381567.PNG)
![student_detail_view](https://user-images.githubusercontent.com/94062868/170861111-f16c0d27-1934-4360-ad04-458ab33aa4f6.PNG)
![scores_list](https://user-images.githubusercontent.com/94062868/170861157-960425ba-45ef-4be5-93bd-a5e99be87e3d.PNG)
![scores_lists_all](https://user-images.githubusercontent.com/94062868/170861159-f8c4bb6f-afc9-4ce0-ac89-e3f3f42be295.PNG)
![scores_filter](https://user-images.githubusercontent.com/94062868/170861179-742202a3-ff40-465c-820e-31eeb2607e83.PNG)
![scores_list_success](https://user-images.githubusercontent.com/94062868/170861158-ad5c8032-04f2-4181-8ef4-813b65361ce4.PNG)
![scores_detailed_view](https://user-images.githubusercontent.com/94062868/170861204-aa40c372-ed67-4558-aa7c-7d4652a3e8b0.PNG)
![all-details](https://user-images.githubusercontent.com/94062868/170861209-3ebaa8ce-0b90-4f2c-823f-2417557ac667.jpeg)

## Assumptions made:
1. Student Score Details Application is configured on docker and is active and running.
2. Student Score Details Application is pushed to docker hub with each service as a independent and a separate repository.
3. Minikube is installed on docker desktop and is running.

## Execution Instructions for Deployment on Kubernetes
1. Clone the repository:
The code is maintained in GitHub and can be pulled to our local machine using the below command.
git clone <b><i>https://github.com/2021cfse031/Deploying_Microservices_with_K8s_C6_Assignment_Group_11.git</i></b>
2. Run the minikube dashboard using the following command
<b><i>minikube dashboard</i></b>
3. Apply deployment using deployment.yaml file with the following command
<b><i>kubectl apply -f deployment.yaml</i></b>
4. Create and expose the deployment through LoadBalancer Service
<b><i>kubectl expose deployment student-ms  --type=LoadBalancer  --port=30001  --target-port=8000 </i></b>
<b><i>kubectl expose deployment scores-ms  --type=LoadBalancer  --port=30002  --target-port=7000 </i></b>
<b><i>kubectl expose deployment all-details-ms  --type=LoadBalancer  --port=30003  --target-port=9000 </i></b> 
5. Launching the application and navigate to endpoints
Each microservice will be running on a different server. The server’s here are isolated using different ports for respective microservices.
a. Student’s Domain is conﬁgured on port 30001 & navigate to localhost:300001/student <br/>
b. Scores Domain is conﬁgured on port 30002 & navigate to localhost:300002/scores <br/>
c. All Details Domain is conﬁgured on port 30003 & navigate to localhost:300003/get-details <br/>
   ![student-view](https://user-images.githubusercontent.com/94062868/182042764-f73810ca-72c1-4bb1-b879-82fb65ca3f2c.png)
   ![scores-view](https://user-images.githubusercontent.com/94062868/182042781-c9074b95-59e2-482e-ac16-072a5feda1ff.png)
   ![all-details-domain-deployment](https://user-images.githubusercontent.com/94062868/182042783-e14f6c3f-3adb-4f13-a981-229fa82b0aa5.png) 

6.  Commands for Rolling Out a deployment
<b><i>docker build . t kiranbs13/student-ms:v1 </i></b><br/><br/>
<b><i>docker push kiranbs13/student-ms:v1 </i></b><br/>
<b><i><b><i>kubectl set image deployments/student-ms student-microservice=kiranbs13/student-ms:v1 </i></b><br/>
<b><i>kubectl rollout status deployments/student-ms </i></b> <br/>
<b><i>kubectl rollout undo deployments/student-ms </i></b><br/>

7.  Commands for Scaling a deployment
	
<b><i>kubectl autoscale deployment student-ms --cpu-percent=50 --min=4 --max=10 </i></b><br/>
<b><i>kubectl get hpa</i></b><br/>
<b><i>kubectl get hpa student-ms --watch</i></b><br/>
   
# Reflection

Deployment of Applications in Docker followed by Kubernetes was a interesting task. Until now we were having a clear understanding of Jenkins software but had got stuck in deployment of multiple services. Kubernetes gave a clear understanding of deployments and rolling out deployments with easy commands. Our Team was happy to work this assignment and get the desired output very soon than expected. Throughout the assignment timeline we had ample time to tweek the features of Minikube Dashboard amd understand Kubernetes even better. Tasks like the deployments on Kubernetes are monitored and outputs are recorded for cluster information, logs, stats of events and summary were performed. The features of Kubernetes are explored by performing a rollout and rollback for an updated version of docker hub image, auto-scaling the deployment through horizontal pod autoscaler method. Additionally, a metrics server is integrated into the minikube dashboard, to get an intuitive view of resources usage like CPU, Memory for every deployment, pods and replica sets. 
