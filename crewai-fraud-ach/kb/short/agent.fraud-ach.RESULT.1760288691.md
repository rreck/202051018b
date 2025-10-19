```json
{
  "id": "b04b3befcf4907ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288691,
  "host_pid": "9e6742732c60:1",
  "hash": "8739fa71a1970a9940d65b797f1ff44656013e45f63173f5b82ae831edfdf6c7",
  "cid": "QmV18739fa71a1970a9940d65b797f1ff44656013e45",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288691,
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
      "evaluated_at": 1760288691
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
  "sig": "fd319161bd62c34668a98dc83b5edb1ae8c528d9437d01e9d068c80897f185cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277046981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 31323130, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': '189e75bc7166d961'}}}