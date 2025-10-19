```json
{
  "id": "7286df1cdb30a517",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291144,
  "host_pid": "9e6742732c60:1",
  "hash": "6dbf4adbe08e2319023c66ae771044b2ceca3db9a49620a0e8695bc0673e40ab",
  "cid": "QmV16dbf4adbe08e2319023c66ae771044b2ceca3db9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291144,
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
      "evaluated_at": 1760291144
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
  "sig": "b19084d22c3121029ea31860edcc151c4ce935bcb7f18b36f90248fcf57a87f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469153369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 15249696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285764, 'matching_hash': 'a6e88c6efc20349f'}}}