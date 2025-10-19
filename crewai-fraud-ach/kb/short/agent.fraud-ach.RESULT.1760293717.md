```json
{
  "id": "17218457ba76f4b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293717,
  "host_pid": "9e6742732c60:1",
  "hash": "a77cd02ed1a256f5a0faca74fce95c3944985e4e90e192b9a7c677678b51d83b",
  "cid": "QmV1a77cd02ed1a256f5a0faca74fce95c3944985e4e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293717,
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
      "evaluated_at": 1760293717
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
  "sig": "02a90b15b3cd5d913a7cb4a8208071ccde11735085d26ff883501aa804c3f71c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151200756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 36426656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'e0249734267f8906'}}}