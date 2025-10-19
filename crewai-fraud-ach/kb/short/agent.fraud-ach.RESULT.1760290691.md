```json
{
  "id": "465f06a14c60b090",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290691,
  "host_pid": "9e6742732c60:1",
  "hash": "ac2169a1f64740374c5774c5ec36c10b6a638fb8f6ac4e6c4a71a67b872ebf4d",
  "cid": "QmV1ac2169a1f64740374c5774c5ec36c10b6a638fb8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290691,
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
      "evaluated_at": 1760290691
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
  "sig": "bbe584d0f909122a1050f82ad01f03eeaf93a89aa1734a168351c8fe35d3a242"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 667325182164908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 25774376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '7f033df851d7a625'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '667325181', 'validation_error': 'Invalid routing number checksum'}}}