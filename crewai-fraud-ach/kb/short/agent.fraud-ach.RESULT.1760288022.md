```json
{
  "id": "8a424c70adc8dfbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288022,
  "host_pid": "9e6742732c60:1",
  "hash": "84ed841a6a4a74871aff4efe0ab909ab0f8ef66caee04bdb8a73b4d73852e9b7",
  "cid": "QmV184ed841a6a4a74871aff4efe0ab909ab0f8ef66c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288022,
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
      "evaluated_at": 1760288022
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
  "sig": "fe9515b650f00fade5575166a545f83ddbb3d8b626719e4cc36c93664f0fcbcd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 24345200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}