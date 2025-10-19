```json
{
  "id": "466d88ee3f128996",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290436,
  "host_pid": "9e6742732c60:1",
  "hash": "9209cd68ea9717a5221847a787f4e2d220c36ef278fc62a10647b4133b4e8a6f",
  "cid": "QmV19209cd68ea9717a5221847a787f4e2d220c36ef2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290436,
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
      "evaluated_at": 1760290436
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
  "sig": "03f88662dbedd67c78852a52e50687a75b1a6b9c1eee60e2e1bd76dfde93ee8c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818590551241151
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 38260950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '902b02e4e6ce46b6'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818590557', 'validation_error': 'Invalid routing number checksum'}}}