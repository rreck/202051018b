```json
{
  "id": "116a8c03895796bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294346,
  "host_pid": "9e6742732c60:1",
  "hash": "19a31db7073b6a2137294596ea475f5cf6a8dfdc6961f26374f25a86d784a436",
  "cid": "QmV119a31db7073b6a2137294596ea475f5cf6a8dfdc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294346,
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
      "evaluated_at": 1760294346
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
  "sig": "3206c7cbfe9326159846f48616bfa93f0a073c52bfb9cf1cecb8ef38c531ae50"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 000042122595756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 312, 'threshold': 50, 'total_amount': 123170112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 311, 'first_seen': 1760284979, 'matching_hash': 'f607cf2148e042a7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '000042121', 'validation_error': 'Invalid routing number checksum'}}}