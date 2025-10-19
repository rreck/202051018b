```json
{
  "id": "9d06e164f515bbbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294355,
  "host_pid": "9e6742732c60:1",
  "hash": "dde451520f9bad52c2b847bd7e3ee2d6e56e566e4869b08b5e36b43905221897",
  "cid": "QmV1dde451520f9bad52c2b847bd7e3ee2d6e56e566e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294355,
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
      "evaluated_at": 1760294355
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
  "sig": "ccd9b583a94c82082ba421bfd7247046482a68029da15224c38f52aa1f92b03f"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 160455148414817
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 85669180, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': 'c57b46b00801b500'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '160455141', 'validation_error': 'Invalid routing number checksum'}}}