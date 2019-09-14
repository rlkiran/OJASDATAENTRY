import firebase_admin
from firebase_admin import firestore, credentials, db


def login():
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate("ojas-key.json")
        default_app = firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://ojas-c3eba.firebaseio.com/'
        })


TestData = {'TestName': 'TestName4', 'Parameter': 'Parameter', 'Units': 'units', 'RefRange': 'RefRange'}


def addTestDataToCloud(**TestData):
    login()
    try:
        store = firestore.client()
        doc_ref = store.collection(TestData['TestName']).document(TestData['Parameter'])
        doc_ref.set({u'Parameter': TestData['Parameter'], u'Units': TestData['Units'],
                     u'RefRange': TestData['RefRange']})
        insertCollectionName(TestData['TestName'])
        print("Data Added Successfully")
        TestData.clear()
    except Exception as e:
        print(str(e))


def insertCollectionName(testname):
    ref = db.reference('Tests')
    ref.update({
        testname: testname
    })


def delTestDataFromCloud(TestName):
    login()
    try:
        store = firestore.client()
        doc_ref = store.collection(TestName)
        docs = doc_ref.stream()
        for doc in docs:
            # print(doc.id)
            # print(u'Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()
        delCollectionName(TestName)
        print("Data Deleted Successfully")
        TestData.clear()
    except Exception as e:
        print(str(e))


def delCollectionName(testname):
    ref = db.reference('Tests/' + testname)
    ref.delete()


def deltechnologyName(techname):
    login()
    ref = db.reference('Technology/' + techname)
    ref.delete()


def addTechName(techname):
    login()
    ref = db.reference('Technology')
    ref.update({
        techname: techname
    })

# addTestDataToCloud(**TestData)
# delTestDataToCloud("TestName4")
