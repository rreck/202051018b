```json
{
  "id": "5dc5606f0e1a7721",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293550,
  "host_pid": "9e6742732c60:1",
  "hash": "e86818becbd15025cb22c9bfaae7579fb1e903fec2d441a2f840fda76fe8cfde",
  "cid": "QmV1e86818becbd15025cb22c9bfaae7579fb1e903fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293550,
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
      "evaluated_at": 1760293550
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
  "sig": "895891844af12db654da2fae372b5f47e9dc66213e91b96f670378d03ebe8b64"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 929669860929959
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 46408011, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'bbfcfb9a6aef8521'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '929669867', 'validation_error': 'Invalid routing number checksum'}}}