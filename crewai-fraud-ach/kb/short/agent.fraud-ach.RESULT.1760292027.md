```json
{
  "id": "f8b4e4066a5c58a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292027,
  "host_pid": "9e6742732c60:1",
  "hash": "1d1e649f5317741a3008bd635ae520434041cf1bbd00238e59eb24fcf0e0c067",
  "cid": "QmV11d1e649f5317741a3008bd635ae520434041cf1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292027,
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
      "evaluated_at": 1760292027
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
  "sig": "3161be92bcbe5e503a54d160acc0bf347e01cc48c06e859bf7bec56dca9187d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 47000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}