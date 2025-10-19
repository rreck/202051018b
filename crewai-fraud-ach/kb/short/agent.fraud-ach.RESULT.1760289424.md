```json
{
  "id": "752904bd01c57c1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289424,
  "host_pid": "9e6742732c60:1",
  "hash": "6b716d1ea3aee765cd40026359b5fa6ce5be32180627df11db3d42c3389db79b",
  "cid": "QmV16b716d1ea3aee765cd40026359b5fa6ce5be3218",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289424,
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
      "evaluated_at": 1760289424
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
  "sig": "d57fddc5d6140f14b397044a4b62a7b91bae2707c07c3ed8e3c7dc3cb1c73f54"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 530764332360017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 25173918, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '09bd6f4aa98253cc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}