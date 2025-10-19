```json
{
  "id": "a372164a4dd0e777",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294734,
  "host_pid": "9e6742732c60:1",
  "hash": "d39d22920c9cdef1fccb897e7d45ac819cc714ae44b5e7065c1171f1a1c218e5",
  "cid": "QmV1d39d22920c9cdef1fccb897e7d45ac819cc714ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294734,
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
      "evaluated_at": 1760294734
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "45a9cd2aa6ea1cc546196514c2d0b204e297e7d89b4e93c7b8794f4d1a30c6bc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 589241761167275
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 76208202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': 'a1dced1ef969015f'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '589241760', 'validation_error': 'Invalid routing number checksum'}}}