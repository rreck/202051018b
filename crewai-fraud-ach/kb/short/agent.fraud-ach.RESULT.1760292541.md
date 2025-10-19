```json
{
  "id": "f4c155346625d89e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292541,
  "host_pid": "9e6742732c60:1",
  "hash": "3b5daf074379da4a84dabd308128305c9a8bad34eb427991d6ec2035ee6563ad",
  "cid": "QmV13b5daf074379da4a84dabd308128305c9a8bad34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292541,
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
      "evaluated_at": 1760292541
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
  "sig": "b7a9bf7cbcd93667e49e80f719b9fc6eea7ca95b840ebe6c6c19de52e190f942"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 701651307465811
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 41617000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '31f29b630ea434da'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}