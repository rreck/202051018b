```json
{
  "id": "50c19fc7e1c75e1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294863,
  "host_pid": "9e6742732c60:1",
  "hash": "dfac9b23093a76a3a64d6475d751c67eb4a7ff3f2c556723ca1544c70e429fff",
  "cid": "QmV1dfac9b23093a76a3a64d6475d751c67eb4a7ff3f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294863,
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
      "evaluated_at": 1760294863
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
  "sig": "a8bfdc1b07772814744765bc4e9fc1f1328b400a89ef5043d270bb3ba7dc6534"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151297418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 107347758, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '6f92d94cce52eccd'}}}