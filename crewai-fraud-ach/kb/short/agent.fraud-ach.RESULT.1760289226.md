```json
{
  "id": "80180dc9a06f5be0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289226,
  "host_pid": "9e6742732c60:1",
  "hash": "a4fd0f4c012bef07d43a8f7f7a758b99431f9cd9c7161c2e804ccbe70b93c68e",
  "cid": "QmV1a4fd0f4c012bef07d43a8f7f7a758b99431f9cd9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289226,
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
      "evaluated_at": 1760289226
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
  "sig": "5862659384cae2341c1f3fdfc7e554b96a61ed0a93ed6e4b8600be9b16f2cdc9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 053611743401753
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 23839920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': 'ed032d3a1e3d03a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}