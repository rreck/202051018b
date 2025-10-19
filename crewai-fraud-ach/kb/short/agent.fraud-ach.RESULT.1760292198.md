```json
{
  "id": "5053b475105781c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292198,
  "host_pid": "9e6742732c60:1",
  "hash": "57df5bfcb9a9d42ef451966a50f2c41d07d0387c2de27a3d22ae7eeb7516c2a2",
  "cid": "QmV157df5bfcb9a9d42ef451966a50f2c41d07d0387c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292198,
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
      "evaluated_at": 1760292198
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
  "sig": "af19d98922928829f5aa2fd5c88522c275c73646f378bc71b51e3b915395f5db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 78995712, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}