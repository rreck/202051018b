```json
{
  "id": "44b0f5a0bc14da00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288919,
  "host_pid": "9e6742732c60:1",
  "hash": "57f39ab241977035b2e4ffbfe2f1d2a11471d40f5e139681ab8aa448b29da1c5",
  "cid": "QmV157f39ab241977035b2e4ffbfe2f1d2a11471d40f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288919,
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
      "evaluated_at": 1760288919
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
  "sig": "78f08ab5365081f8598d81f1ddb84fba1671e3d48eba222c39de7c42943c7604"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023390591
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 33804432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285764, 'matching_hash': '65b6a0d7e3017724'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}