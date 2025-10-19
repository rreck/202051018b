```json
{
  "id": "4a61249648bbbab0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294898,
  "host_pid": "9e6742732c60:1",
  "hash": "2b8c0df3885d19603d805b2f16c27a303740bc82027bfd97f6559e6ba191c93b",
  "cid": "QmV12b8c0df3885d19603d805b2f16c27a303740bc82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294898,
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
      "evaluated_at": 1760294898
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
  "sig": "f3ff917620c8bfc235dd6411c8073194de65a8ed1d05a58041c0c70fee21967d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039404283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 82256742, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '11fbcf742e15d2b0'}}}