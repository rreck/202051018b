```json
{
  "id": "3012d23962ebff4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292929,
  "host_pid": "9e6742732c60:1",
  "hash": "cf8163fed74bbe73f4fbf4d361a979d26fd4bdf20ac78b68f883f38a25a44259",
  "cid": "QmV1cf8163fed74bbe73f4fbf4d361a979d26fd4bdf2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292929,
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
      "evaluated_at": 1760292929
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
  "sig": "9b37bb6a779e1304b8a0371298f495608cac4ea4da190480716bf87e2edf989c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 304701772219564
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 49717200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285764, 'matching_hash': '19ec134c2c5b9271'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '304701776', 'validation_error': 'Invalid routing number checksum'}}}