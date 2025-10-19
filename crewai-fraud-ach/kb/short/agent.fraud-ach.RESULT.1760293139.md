```json
{
  "id": "e43d82b30b910fcf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293139,
  "host_pid": "9e6742732c60:1",
  "hash": "dd8d46b14edd4521310ed1baecffb7b8b54be606ec26fe267145890736bf760b",
  "cid": "QmV1dd8d46b14edd4521310ed1baecffb7b8b54be606",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293139,
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
      "evaluated_at": 1760293139
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
  "sig": "1b9b7cc1b8fa2c0831ade521b5565b778c43a81e2088594c187c1c59d598229d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271369125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 32830108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': 'b975113295de86ab'}}}