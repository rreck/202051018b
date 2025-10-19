```json
{
  "id": "024eb1a1c4145e78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289484,
  "host_pid": "9e6742732c60:1",
  "hash": "d6cd0063a7e6eed222fae4a5072b22a5e4c7b080852c516199a134ea65c1a69a",
  "cid": "QmV1d6cd0063a7e6eed222fae4a5072b22a5e4c7b080",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289484,
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
      "evaluated_at": 1760289484
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
  "sig": "72b457b8e5d573ea013aaf9d9770f3583e71f94ba30c43ba79e1b6f6539109fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 39462752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}