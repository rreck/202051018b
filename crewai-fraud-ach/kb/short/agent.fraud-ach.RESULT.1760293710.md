```json
{
  "id": "5a70109db8e9debc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293710,
  "host_pid": "9e6742732c60:1",
  "hash": "ff4a21fc015c1c34111624b41c0f0d4cbecd20fa118f7326c166438b8a16d735",
  "cid": "QmV1ff4a21fc015c1c34111624b41c0f0d4cbecd20fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293710,
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
      "evaluated_at": 1760293711
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
  "sig": "82fe392084fb54ac920090fee89bf7bf5fe98e055c4476bd0d14de68bcbc3f10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032712325
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 81502624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '06a9425dc3ac5c5b'}}}