```json
{
  "id": "559aa0bc5f3cf302",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292377,
  "host_pid": "9e6742732c60:1",
  "hash": "794f9d051e6ba808feec618792cfef02b0e1b30984a1810c1391969407697140",
  "cid": "QmV1794f9d051e6ba808feec618792cfef02b0e1b309",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292377,
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
      "evaluated_at": 1760292377
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
  "sig": "c29df373a5dcdb9da5cbf71c68ed0bac49d89607a20057aacee016b74bc11094"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022029056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 38553984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': '0de74255bde38153'}}}