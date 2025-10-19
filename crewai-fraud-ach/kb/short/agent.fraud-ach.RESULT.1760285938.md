```json
{
  "id": "13d4a2861af0527a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285938,
  "host_pid": "9e6742732c60:1",
  "hash": "3188b11139b087e3a30cab37f7a65886ea55e37e1d0a09d55d61b00eeccaf62b",
  "cid": "QmV13188b11139b087e3a30cab37f7a65886ea55e37e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285938,
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
      "evaluated_at": 1760285938
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
  "sig": "c5c1b4e8a1e07a23248276d0beada71089a18e469d561740288b29b69ef21c29"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100277570300
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285763, 'matching_hash': '94740eaab516570d'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '864091464', 'validation_error': 'Invalid routing number checksum'}}}