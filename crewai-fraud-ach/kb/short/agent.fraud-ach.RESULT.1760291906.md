```json
{
  "id": "464466ee22c10232",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291906,
  "host_pid": "9e6742732c60:1",
  "hash": "04b3d40b1a69bd038792d30d5e29c6d70f10709331ab16ad7fee2239dd22aa3b",
  "cid": "QmV104b3d40b1a69bd038792d30d5e29c6d70f107093",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291906,
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
      "evaluated_at": 1760291906
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
  "sig": "a70c341d3b307be3411a9931dd7d805285c39693fb536ca1fc1440c92152044a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 530764332360017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 38067876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '09bd6f4aa98253cc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}