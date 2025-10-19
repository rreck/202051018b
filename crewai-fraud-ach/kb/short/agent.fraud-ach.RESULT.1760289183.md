```json
{
  "id": "11b5653c15c191d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289183,
  "host_pid": "9e6742732c60:1",
  "hash": "70c945f7bbb532afd4512c808749e412b1e009bd7eb3e5120b17daf0f82dba32",
  "cid": "QmV170c945f7bbb532afd4512c808749e412b1e009bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289183,
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
      "evaluated_at": 1760289183
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
  "sig": "76ebaf696e9f819729a917498c7d331e3748141f48da96c2ba1a25da130132d7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 294015856728576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 56046560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '68167a889af65895'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '294015854', 'validation_error': 'Invalid routing number checksum'}}}