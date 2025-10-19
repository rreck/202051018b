```json
{
  "id": "435682a47121f3fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288793,
  "host_pid": "9e6742732c60:1",
  "hash": "650605e5c5e712ef0b72f7c0fdd2d9b2209f2b4cf1d8399dcaf2c0c3148789b8",
  "cid": "QmV1650605e5c5e712ef0b72f7c0fdd2d9b2209f2b4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288793,
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
      "evaluated_at": 1760288793
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
  "sig": "721694511d1276e1dacab035ffeab2ed53062355c787e185dc4b1caf1a65cda6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244317854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 39475280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': '3595d612a0391b5c'}}}