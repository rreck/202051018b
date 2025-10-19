```json
{
  "id": "5b2b1da2b3b8528b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291928,
  "host_pid": "9e6742732c60:1",
  "hash": "03e98b7940988c8a78a700b7d209412598868cf8988098815370d4f1634f09d7",
  "cid": "QmV103e98b7940988c8a78a700b7d209412598868cf8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291928,
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
      "evaluated_at": 1760291928
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
  "sig": "1e3a0ee272a66d18116d5b2114a38f5dee708ab10654ba88f43de24236967c0e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038959082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 16010694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285765, 'matching_hash': '98ae9ae4174799d3'}}}