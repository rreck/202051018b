```json
{
  "id": "5405d45206ba96b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291077,
  "host_pid": "9e6742732c60:1",
  "hash": "a442f002db06da88463e23d11cf826e1cf24532d796d378bffd5ad2928ae9e49",
  "cid": "QmV1a442f002db06da88463e23d11cf826e1cf24532d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291077,
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
      "evaluated_at": 1760291077
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
  "sig": "80aef3c127117875ef086c1e434e2bb70040a40fc500f557388f86de20bb014c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 49984260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}