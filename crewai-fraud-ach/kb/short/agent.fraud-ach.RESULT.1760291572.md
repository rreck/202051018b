```json
{
  "id": "54fae35e78519ad0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291572,
  "host_pid": "9e6742732c60:1",
  "hash": "c6fc3dc752dae0b4f1064d98cbc6d4ebfc339452e4fac781ba88cd5044bdd15f",
  "cid": "QmV1c6fc3dc752dae0b4f1064d98cbc6d4ebfc339452",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291572,
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
      "evaluated_at": 1760291572
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
  "sig": "66cb8ce44da06281a638af6cb64bc1a675d6ade9c04858717b6ca964376a585c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 443655357779767
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 66090154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': 'b8048cbf6aca9902'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '443655354', 'validation_error': 'Invalid routing number checksum'}}}