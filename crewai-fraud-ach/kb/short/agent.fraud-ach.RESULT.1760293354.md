```json
{
  "id": "1b0cb740be9822c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293354,
  "host_pid": "9e6742732c60:1",
  "hash": "7cbf7f8f917601c205bb2994f95320708519290fde53891d8b8b6e377d992c8b",
  "cid": "QmV17cbf7f8f917601c205bb2994f95320708519290f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293354,
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
      "evaluated_at": 1760293354
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
  "sig": "a181bed36deed6cbf24000f3f8837085bf52c58a65ec80314a4af9c317303d05"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 929669860929959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 45568047, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}