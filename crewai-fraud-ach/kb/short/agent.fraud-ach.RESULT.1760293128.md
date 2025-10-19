```json
{
  "id": "0a2f6ae386bc29f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293128,
  "host_pid": "9e6742732c60:1",
  "hash": "62ad8484f69fbae7053c8a193d8ac3e2ccea779eec2c8d3a12eb48b7f068eb37",
  "cid": "QmV162ad8484f69fbae7053c8a193d8ac3e2ccea779e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293128,
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
      "evaluated_at": 1760293128
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
  "sig": "41735dd78e4be45966bfb975dcc1c2bfb510c0f5004627a7df18c93d4ef64941"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270124106
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 87777752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '785cd1c2415b19ab'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}