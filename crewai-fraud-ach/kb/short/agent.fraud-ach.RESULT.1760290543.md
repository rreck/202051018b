```json
{
  "id": "88c2e04d0dc46dc1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290543,
  "host_pid": "9e6742732c60:1",
  "hash": "b58d242802a2722abaebae863f2a898c9ebda955a80e078e6c2fc09f1584a949",
  "cid": "QmV1b58d242802a2722abaebae863f2a898c9ebda955",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290543,
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
      "evaluated_at": 1760290543
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
  "sig": "c9d71c9a7946cdebe9b3938e6cff8caec5383f8d4277829be22a50a89a9e1d9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028017264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 69569559, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '707a4137bac9b143'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}