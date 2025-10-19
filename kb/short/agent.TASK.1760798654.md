```json
{
  "id": "agent.TASK.1760798654",
  "scope": "agent",
  "key": "TASK",
  "epoch": 1760798654,
  "host_pid": "rreck-MS-7D25:1134546",
  "hash": "87f8b9746415ad65f2eabaec7219e5802130859051a0e531dc46bc1634c165aa",
  "cid": "cid:0b10fd4aeab9688f",
  "aicp": {
    "prov": {
      "@context": "https://www.w3.org/2018/credentials/v1",
      "type": [
        "VerifiableCredential",
        "AIContentProvenance"
      ],
      "issuer": "demo-agent",
      "issuanceDate": "2025-10-18T14:44:14Z",
      "credentialSubject": {
        "id": "urn:uuid:ec77182a38119d915550b1f472868ee2",
        "timestamp": 1760798654,
        "host_pid": "rreck-MS-7D25:1134546"
      }
    },
    "ucon": {
      "constraints": [],
      "obligations": [],
      "permissions": [
        "read"
      ]
    },
    "eval": {
      "quality": 0.0,
      "confidence": 0.0,
      "reviewers": []
    }
  },
  "sources": [
    "agent.IDEA.1760798654"
  ],
  "edges": [],
  "metrics": {},
  "thresholds": {
    "tau_days": 7,
    "lambda_decay": 0.01,
    "cluster_min_sources": 5,
    "cluster_min_weight": 0.6
  },
  "tags": [
    "implementation"
  ],
  "sig": "fc85212c8fb98c728640c32dedf03d8bcfd103bbdb3869b8015d460645d877f9"
}
```

Implement: Create UCON constraint validator
