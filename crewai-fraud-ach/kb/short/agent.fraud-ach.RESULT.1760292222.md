```json
{
  "id": "a33570e2b95c10d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292222,
  "host_pid": "9e6742732c60:1",
  "hash": "c10e20e29e30a350eb653db49a3816972902ddc87b7cf2cced2f6ab39b437824",
  "cid": "QmV1c10e20e29e30a350eb653db49a3816972902ddc8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292222,
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
      "evaluated_at": 1760292222
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
  "sig": "6a523b49605b62f68d73358e4583c8c91b6f486c9f4eac05ddeb98b3c0ea1bdc"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 408733730305741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 78352596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285763, 'matching_hash': '77eebc6eb9f79eeb'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}