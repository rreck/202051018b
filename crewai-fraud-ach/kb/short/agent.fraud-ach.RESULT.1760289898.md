```json
{
  "id": "ad62cc15d881185a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289898,
  "host_pid": "9e6742732c60:1",
  "hash": "6568cd0ce41b063a39dbd27282a8691d310b22636089e95d86791b1ab8eafaeb",
  "cid": "QmV16568cd0ce41b063a39dbd27282a8691d310b2263",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289898,
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
      "evaluated_at": 1760289898
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
  "sig": "8c15d6fa5ba01b0a8f84a79b7ca41ed078c6fcb44f1ddf2d86e1281a350e78f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276179264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 23318016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}