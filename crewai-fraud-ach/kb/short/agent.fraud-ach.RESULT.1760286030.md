```json
{
  "id": "69063e7b28360f06",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286030,
  "host_pid": "9e6742732c60:1",
  "hash": "7c9c2e60bedf1e83892c507ed5cf955ae84fc764bf9dd86fe9dcde0c8c2b5749",
  "cid": "QmV17c9c2e60bedf1e83892c507ed5cf955ae84fc764",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286030,
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
      "evaluated_at": 1760286030
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
  "sig": "948795ca7c81ab519ad478be4b9e795b207d4739f6922e719478e7e2a27bb402"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243431079
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285764, 'matching_hash': '441814efc7e72dab'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}