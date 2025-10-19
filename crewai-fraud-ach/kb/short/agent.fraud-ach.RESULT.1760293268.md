```json
{
  "id": "e05c2e93bf1f6861",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293268,
  "host_pid": "9e6742732c60:1",
  "hash": "e9f2a3d9866f2140c5c7feef4cab708e93161342cc6b4dcb870d4cb0c8f92083",
  "cid": "QmV1e9f2a3d9866f2140c5c7feef4cab708e93161342",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293268,
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
      "evaluated_at": 1760293268
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
  "sig": "4526f0639b4e74f8c87542714864aa0bbe8e95293f815a0b993bcf061329f809"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244163284273009
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 71207570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}