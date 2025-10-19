```json
{
  "id": "2093672fa1520077",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293121,
  "host_pid": "9e6742732c60:1",
  "hash": "a25ec92b144ab74ef449738c0a2c90ed59116d047cde0768566c9e5fe2c570a1",
  "cid": "QmV1a25ec92b144ab74ef449738c0a2c90ed59116d04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293121,
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
      "evaluated_at": 1760293121
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
  "sig": "b39d2e1442949d4e9a7d281b9e3bad9736aaf6b61d62e6fab404395ab4854187"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 472304306013162
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 96096844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285764, 'matching_hash': '18e6c75ff941397c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}