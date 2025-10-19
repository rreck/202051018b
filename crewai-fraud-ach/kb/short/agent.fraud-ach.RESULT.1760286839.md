```json
{
  "id": "df1116eedcd31692",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286839,
  "host_pid": "9e6742732c60:1",
  "hash": "32a4d200db9a70c2c5024fe7a223648c883185535000b7e2b84e84aa66b743c0",
  "cid": "QmV132a4d200db9a70c2c5024fe7a223648c88318553",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286839,
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
      "evaluated_at": 1760286839
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4e2fafc329f49205588e61a1e5bd1bee1e7eb1ff2df368bd670135ecffcabaa6"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13209573, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}