```json
{
  "id": "6fcde611d7fa862e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293161,
  "host_pid": "9e6742732c60:1",
  "hash": "54d3713d28dc06ca41ecc5a7a36d7c5c08d10a7b9c6d5fbaf864cb71b1fe12b3",
  "cid": "QmV154d3713d28dc06ca41ecc5a7a36d7c5c08d10a7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293161,
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
      "evaluated_at": 1760293161
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
  "sig": "bda736e2e64ae1c412d84349bc79fa668fd9639b45170bd64e7177740f03b3ac"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 261425243879882
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 70363911, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': 'bea146cfc71ce9bb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}