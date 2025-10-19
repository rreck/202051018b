```json
{
  "id": "1fc8fc73b1e2cbda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290979,
  "host_pid": "9e6742732c60:1",
  "hash": "a7a134cb5c3158c10b366eca7f8d162e99249569c3ae653a8b7e102c1e040f23",
  "cid": "QmV1a7a134cb5c3158c10b366eca7f8d162e99249569",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290979,
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
      "evaluated_at": 1760290979
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
  "sig": "51d21e7cfdca52c2c73ce7780ca08173ba8b4248a17526a64197955b1beacd97"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 23261924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}