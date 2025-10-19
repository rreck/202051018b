```json
{
  "id": "e143ef6882de0183",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293087,
  "host_pid": "9e6742732c60:1",
  "hash": "772f67151724e8b3a69d4bf116106fc3c9197f27f19776be188b7c7cb26d1727",
  "cid": "QmV1772f67151724e8b3a69d4bf116106fc3c9197f27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293087,
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
      "evaluated_at": 1760293087
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
  "sig": "a0942b057ef54c9c206e1c8bb46f647e60d525985968a029f1140fa7e27932ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152597197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 56145834, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '6e11bb738f10d63a'}}}