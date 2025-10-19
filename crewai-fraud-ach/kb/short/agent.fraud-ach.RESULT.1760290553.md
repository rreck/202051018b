```json
{
  "id": "008ae7411d96f269",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290553,
  "host_pid": "9e6742732c60:1",
  "hash": "627d47388e5a004a40b928a39dd45d6d8c41c401fc94cb40d443b723f72cb0a8",
  "cid": "QmV1627d47388e5a004a40b928a39dd45d6d8c41c401",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290553,
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
      "evaluated_at": 1760290553
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
  "sig": "8621537170077e67c9cdb8c5d1b70df19f6835a2c2bc486dac9ebbbdae321a1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029285635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 53279037, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '952b5fd24342145c'}}}