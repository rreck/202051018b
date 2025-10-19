```json
{
  "id": "b9c72e3dfd447b75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288922,
  "host_pid": "9e6742732c60:1",
  "hash": "18878e3670120bc392bb8eb00679d08316b27351b7ba90840432f9b21c81393e",
  "cid": "QmV118878e3670120bc392bb8eb00679d08316b27351",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288922,
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
      "evaluated_at": 1760288922
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
  "sig": "2dcb30129f13f50e5e89bbf374062b45c8e63d56d87d393d500881d6fae2b083"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 19297656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}