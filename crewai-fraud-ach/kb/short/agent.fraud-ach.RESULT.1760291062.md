```json
{
  "id": "4e447d302e611668",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291062,
  "host_pid": "9e6742732c60:1",
  "hash": "c8d926f3d58242b790320748a922cf808196589b73d0f08183b84fba28074cf2",
  "cid": "QmV1c8d926f3d58242b790320748a922cf808196589b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291062,
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
      "evaluated_at": 1760291062
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
  "sig": "ad266bd1990db950b0fd86845e10dd3b8cbffd15e42d58db25056194241830fd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 22516074, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}