```json
{
  "id": "000aad232a611c2c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293029,
  "host_pid": "9e6742732c60:1",
  "hash": "ee90c1b22c0fc9646c16cb5d6d5b92077c8e31fe977c5043c71b7a84a32a27ea",
  "cid": "QmV1ee90c1b22c0fc9646c16cb5d6d5b92077c8e31fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293029,
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
      "evaluated_at": 1760293029
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
  "sig": "420655d5715c892b70b34fb5152ee4a3a34a1a02cf963b22bd1d03038ce9ea75"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 051442861806700
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 89467350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': '36501cb7899f5f80'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}