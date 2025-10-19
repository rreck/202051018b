```json
{
  "id": "50e693efc4988d64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292006,
  "host_pid": "9e6742732c60:1",
  "hash": "85b7223b7389a3fc081a0c55f37a1cbbb1c2819e1a78c531567f4ef31fc7a27d",
  "cid": "QmV185b7223b7389a3fc081a0c55f37a1cbbb1c2819e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292006,
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
      "evaluated_at": 1760292006
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
  "sig": "81290ed3c74121f900d88e9bef711955c44e07568e97775f4cc66edc397c47ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467071616
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 84551872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}