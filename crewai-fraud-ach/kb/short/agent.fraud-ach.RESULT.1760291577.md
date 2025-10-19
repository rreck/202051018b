```json
{
  "id": "c47946b3fbb89f54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291577,
  "host_pid": "9e6742732c60:1",
  "hash": "6d0a68a941dea890feb7dd19495477ae05588adb86993f1d707fc033aa8c87b5",
  "cid": "QmV16d0a68a941dea890feb7dd19495477ae05588adb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291577,
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
      "evaluated_at": 1760291577
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
  "sig": "a3f559497cffb9b8875e3f24e3f0c71545702d9c782c0b4ea95090a28212a36f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030330812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 36080956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '72f4f50a1c3c0bfc'}}}