```json
{
  "id": "b61b7783f1f4855b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291759,
  "host_pid": "9e6742732c60:1",
  "hash": "0545a69f7b6a786577388f01f60297ad8e7e0b6e569304395e45c4c9898d9b1e",
  "cid": "QmV10545a69f7b6a786577388f01f60297ad8e7e0b6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291759,
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
      "evaluated_at": 1760291759
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
  "sig": "7c9edc986954665fa1cc75ae381ef0626a4fadc8f9c3ed41678ea80b63fa6fb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 67882178, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}