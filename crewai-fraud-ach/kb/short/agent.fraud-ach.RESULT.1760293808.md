```json
{
  "id": "0405c514f0d7c66c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293808,
  "host_pid": "9e6742732c60:1",
  "hash": "23f15e1f5804741595155a67f23e35570e1d9f2c435a78494fd0e8b9cbf7f495",
  "cid": "QmV123f15e1f5804741595155a67f23e35570e1d9f2c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293808,
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
      "evaluated_at": 1760293808
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
  "sig": "316a2d8a30bd22d07a946754ec780c99606c39fdb52a47ea3d9d0e2dd5366fc7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 18673250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}