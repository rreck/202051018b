```json
{
  "id": "653e46d730081cdb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286922,
  "host_pid": "9e6742732c60:1",
  "hash": "a6ad0f3a548de6069629a50316770b65a14507b434ef4908924b1c8cb1145a1f",
  "cid": "QmV1a6ad0f3a548de6069629a50316770b65a14507b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286922,
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
      "evaluated_at": 1760286922
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
  "sig": "f05f2d9acfc50b815e17dc6d407ae68907538f071d4607740df751aabd7521d2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105151297418
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 18327666, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': '6f92d94cce52eccd'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '085520764', 'validation_error': 'Invalid routing number checksum'}}}