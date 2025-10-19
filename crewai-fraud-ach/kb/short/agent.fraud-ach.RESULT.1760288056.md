```json
{
  "id": "8286657c78b4a7fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288056,
  "host_pid": "9e6742732c60:1",
  "hash": "055fa854acd19b0f5f903ecbdcf8e65ffbb1a9affda5445ae813b66a6e9e3f50",
  "cid": "QmV1055fa854acd19b0f5f903ecbdcf8e65ffbb1a9af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288056,
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
      "evaluated_at": 1760288056
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "c269a60aa1631fa62b20de32f26ad422422a375145c10ebde84dc68c203fd5f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 12462741, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}