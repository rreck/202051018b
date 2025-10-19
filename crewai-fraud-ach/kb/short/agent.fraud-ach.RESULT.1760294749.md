```json
{
  "id": "aff0a39bfc19baa2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294749,
  "host_pid": "9e6742732c60:1",
  "hash": "10739768560b920f8caf84959d1129f03c59729330b79c7e01132662155659c5",
  "cid": "QmV110739768560b920f8caf84959d1129f03c597293",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294749,
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
      "evaluated_at": 1760294749
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
  "sig": "0d6c2b51b48fcbc86de71a0f27e007e6ca82dac5cfa9a32b6d2998dbb069a3e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244267355
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 36687840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '9a2cfa03d6a38585'}}}