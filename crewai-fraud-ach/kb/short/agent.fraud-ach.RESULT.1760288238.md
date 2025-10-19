```json
{
  "id": "cf77ce530dc534d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288238,
  "host_pid": "9e6742732c60:1",
  "hash": "6536a252765d3978efac5c8ce5930e6f3fd3a14d4fd030de5afc521a0b7d1167",
  "cid": "QmV16536a252765d3978efac5c8ce5930e6f3fd3a14d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288238,
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
      "evaluated_at": 1760288238
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
  "sig": "1544971bd566357e3638f1ee4725b26689b934563a4a1bfd1bcc3de4b7e44b85"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 886156735269080
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 16686687, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}