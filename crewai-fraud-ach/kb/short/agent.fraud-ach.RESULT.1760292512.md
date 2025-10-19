```json
{
  "id": "715e3e7d174b290d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292512,
  "host_pid": "9e6742732c60:1",
  "hash": "0c54a37166487de36b5d3ab63bb166802f610fdf65acae518d8db3267cfe8e95",
  "cid": "QmV10c54a37166487de36b5d3ab63bb166802f610fdf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292512,
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
      "evaluated_at": 1760292512
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
  "sig": "ba211091b228bbffbbb125515cd19d033e70bb90b7b119be686169c84664c061"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 053611743401753
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 40548240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': 'ed032d3a1e3d03a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}