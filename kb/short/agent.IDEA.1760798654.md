```json
{
  "id": "agent.IDEA.1760798654",
  "scope": "agent",
  "key": "IDEA",
  "epoch": 1760798654,
  "host_pid": "rreck-MS-7D25:1134546",
  "hash": "8ba49fe45bf45f63a6efb060216cf11b79393fabd160bcd9ae9fac57f3de8634",
  "cid": "cid:1b3532fb42b82aa1",
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
        "id": "urn:uuid:285b942f5f90f1ce86bfac3d75de2ed1",
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
  "sources": [],
  "edges": [],
  "metrics": {
    "priority": 0.8999999999999999
  },
  "thresholds": {
    "tau_days": 7,
    "lambda_decay": 0.01,
    "cluster_min_sources": 5,
    "cluster_min_weight": 0.6
  },
  "tags": [
    "architecture",
    "pmem"
  ],
  "sig": "6b9f83eb6c705d359bdf4751e0d97ce98c550bed0a27970387a70e1d3ba1597e"
}
```

Create UCON constraint validator
