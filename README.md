# Red Hat Openshift Data Foundation

## Object Storage 

### Application s3app

Application écrite en Python pour manipuler les objets S3 pour fins de démonstrations.

#### Le script s3_create_objects.py

Écrit 10 objets dans un bucket contenant du texte et du metadata.

#### Le script s3_list_objects.py

Affiche la liste des objets d'un bucket et affiche le métadata et le contenu de l'objet Key=myfiles20

### Commandes utiles

Afficher la liste des buckets
```
aws s3 --endpoint-url=https://s3-openshift-storage.apps.openshift.rhcasalab.com ls
```

Afficher la liste des fichiers
```
aws s3 --endpoint-url=https://s3-openshift-storage.apps.openshift.rhcasalab.com ls s3://demo834-1-a61a1c8d-3be1-4d4e-b755-ee4aa05b699a
```

Afficher la liste des objets
```
aws s3api --endpoint-url=https://s3-openshift-storage.apps.openshift.rhcasalab.com list-objects --bucket demo834-1-a61a1c8d-3be1-4d4e-b755-ee4aa05b699a
```

Effacer le contenu d'un bucket
```
aws s3 --endpoint-url=https://s3-openshift-storage.apps.openshift.rhcasalab.com rm s3://demo834-1-a61a1c8d-3be1-4d4e-b755-ee4aa05b699a --recursive
```