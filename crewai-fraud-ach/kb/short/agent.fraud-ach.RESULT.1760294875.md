```json
{
  "id": "beed088b670e1d20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294875,
  "host_pid": "9e6742732c60:1",
  "hash": "fb1eab39671ab4f81d7e170c49a6e02a0b2133fe8785f76191ae9fdc66c556ec",
  "cid": "QmV1fb1eab39671ab4f81d7e170c49a6e02a0b2133fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294875,
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
      "evaluated_at": 1760294875
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
  "sig": "b7d80f2048698ea3c6dfde3f9529fc10c9891136d8ab25393cadf5efda931557"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029588067
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 75711420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '5ca8480d00f733c5'}}}