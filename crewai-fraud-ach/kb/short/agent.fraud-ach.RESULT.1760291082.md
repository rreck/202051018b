```json
{
  "id": "e2be43b06afe8d79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291082,
  "host_pid": "9e6742732c60:1",
  "hash": "548fe85c6b7b424a1fcfed17944f2bb69043337dbf7261fc25d0b75c2b339447",
  "cid": "QmV1548fe85c6b7b424a1fcfed17944f2bb69043337d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291082,
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
      "evaluated_at": 1760291082
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
  "sig": "44840cb171d6ab956ae169310c8173dcb848091cc599954b5df3cb36a2f8bef9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 52829168, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}