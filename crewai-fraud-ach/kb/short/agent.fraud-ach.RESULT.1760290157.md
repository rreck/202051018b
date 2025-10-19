```json
{
  "id": "a73b059c269ab33e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290157,
  "host_pid": "9e6742732c60:1",
  "hash": "3765459800041c2049609664f6d3054aad1ccc93ac48adf7edfb54e78dbe95da",
  "cid": "QmV13765459800041c2049609664f6d3054aad1ccc93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290157,
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
      "evaluated_at": 1760290157
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
  "sig": "e9f141123703082e22729ef094e31c74ece770a8ba3bc7eff8ad7cfa573a9345"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244163284273009
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 47361314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}