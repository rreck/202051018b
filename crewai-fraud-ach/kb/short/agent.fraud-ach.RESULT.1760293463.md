```json
{
  "id": "a33f140aa1e5f1c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293463,
  "host_pid": "9e6742732c60:1",
  "hash": "bef750a1a9a8a8b9bb7833f64d188ca09cb3f343b8b23fb8c876a79c5012e9fc",
  "cid": "QmV1bef750a1a9a8a8b9bb7833f64d188ca09cb3f343",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293463,
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
      "evaluated_at": 1760293463
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
  "sig": "fb646acf88cd6b87622298ba3d89da5122957f927b996c11a6935d2a47c6844d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244163284273009
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 72532362, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}