```json
{
  "id": "ce9f7526eec87bc8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289262,
  "host_pid": "9e6742732c60:1",
  "hash": "37b8cfa712f0a21b146448d0bf4d1458a11348b46e546d414896dedbbca2aeaf",
  "cid": "QmV137b8cfa712f0a21b146448d0bf4d1458a11348b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289262,
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
      "evaluated_at": 1760289262
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
  "sig": "232f8993ac3ebf6dafade59199cdc7f9e89634fb48eba28d1c6f05ae67d1c689"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 12533488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}