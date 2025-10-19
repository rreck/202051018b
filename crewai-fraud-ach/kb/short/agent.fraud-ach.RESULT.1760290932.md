```json
{
  "id": "721830739680a0cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290932,
  "host_pid": "9e6742732c60:1",
  "hash": "e6fc6ed6403ae36dc1765ec11815e67de2ff5eb762d72dd5fe057f53e4d2e3d7",
  "cid": "QmV1e6fc6ed6403ae36dc1765ec11815e67de2ff5eb7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290932,
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
      "evaluated_at": 1760290932
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "c92c65404a519cba186e579030216e19f6d8ef3d88162ac760a7040ee8fe2d2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278947252
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 35746063, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'c008d048aedbdb99'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}