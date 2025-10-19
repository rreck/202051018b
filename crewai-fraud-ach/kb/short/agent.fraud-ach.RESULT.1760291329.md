```json
{
  "id": "e214cd20b282ecc2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291329,
  "host_pid": "9e6742732c60:1",
  "hash": "ff664b967c0253b7e7b56559a7c7b820eba195411f8e287bcd896379d70dc222",
  "cid": "QmV1ff664b967c0253b7e7b56559a7c7b820eba19541",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291329,
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
      "evaluated_at": 1760291329
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
  "sig": "cf757e9b2118c4d61bf30b28013a54099d5df30d6a459f09802406343e42831c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240153207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 43000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285764, 'matching_hash': '9e24c0ed91a48db3'}}}