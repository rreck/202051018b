```json
{
  "id": "b9c0f3df4988cf25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288222,
  "host_pid": "9e6742732c60:1",
  "hash": "e19a86cf8efeec5d7786a08d8d913a0f87bfc65ecc190493d7b9fc91dc8f97f4",
  "cid": "QmV1e19a86cf8efeec5d7786a08d8d913a0f87bfc65e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288222,
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
      "evaluated_at": 1760288222
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
  "sig": "8d41800a707edd59ac51981a0eee749b3e65e645dae8d5ea1028df2cc7a926e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 27369328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}