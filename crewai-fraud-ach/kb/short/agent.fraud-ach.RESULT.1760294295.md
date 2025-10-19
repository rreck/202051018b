```json
{
  "id": "b19b3ae4657647d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294295,
  "host_pid": "9e6742732c60:1",
  "hash": "b6a703918b9cdb30c5bd0b664a56d9c09eef7206dd0a7c270da895d2eac1f2c1",
  "cid": "QmV1b6a703918b9cdb30c5bd0b664a56d9c09eef7206",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294295,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760294295
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "6541f08edc2359bc1f97aca808180bb23df44049cae2f8b5923ef0e83063b52c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 89256055, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}