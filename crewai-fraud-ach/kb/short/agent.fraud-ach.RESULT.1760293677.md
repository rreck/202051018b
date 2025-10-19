```json
{
  "id": "2d68a3d8b57ff963",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293677,
  "host_pid": "9e6742732c60:1",
  "hash": "9240826c10b2e53e23747874e56f5be021b503cf660142ec167262d5189e7a21",
  "cid": "QmV19240826c10b2e53e23747874e56f5be021b503cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293677,
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
      "evaluated_at": 1760293677
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
  "sig": "86a52b99798c1c1f0dee1c82b31f79c1ed90e7454fd3456b2d1c4040b2a2e77e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026783731
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 91750228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'dea6d8bb62de6c67'}}}