```json
{
  "id": "0075ae5ac5059504",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288848,
  "host_pid": "9e6742732c60:1",
  "hash": "ff598e1497ba7cdaeb2cc229c24314747b3c760f3dcab6862bc6a87dabd5f553",
  "cid": "QmV1ff598e1497ba7cdaeb2cc229c24314747b3c760f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288848,
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
      "evaluated_at": 1760288848
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
  "sig": "68ca80cb2b6a2a21dd8c3b36ceabe00238ea1725b2314210cf4950334145648a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023218255
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '1151ecc015fd8f1a'}}}een': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}