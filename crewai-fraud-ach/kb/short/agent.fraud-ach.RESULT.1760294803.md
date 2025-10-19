```json
{
  "id": "4fdac1b821a0a615",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294803,
  "host_pid": "9e6742732c60:1",
  "hash": "abdeda03adfb1b3595e99073fae1fa8627318793d7a227e095947f7c095bfd63",
  "cid": "QmV1abdeda03adfb1b3595e99073fae1fa8627318793",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294803,
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
      "evaluated_at": 1760294803
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
  "sig": "0ad6f4dd681496fedd73c0e3ad8cf48a9bf3797877ac527309fcc50e8608f8ed"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 929669860929959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 51447795, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}