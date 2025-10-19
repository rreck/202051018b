```json
{
  "id": "5d0ae7b32ed7beaf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290771,
  "host_pid": "9e6742732c60:1",
  "hash": "e1ce0601598b20b152fe45786a6d8c4ab6d62b0ef78ff255d1e4fc03fa240cda",
  "cid": "QmV1e1ce0601598b20b152fe45786a6d8c4ab6d62b0e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290771,
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
      "evaluated_at": 1760290771
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
  "sig": "84c72c645fde967b6f35881919dc9243c1490958b8a3ab129aa3b2d897588583"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467455813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 10784970, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': 'dd25b8ab6718ff18'}}}