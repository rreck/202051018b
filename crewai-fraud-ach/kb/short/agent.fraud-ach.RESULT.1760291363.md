```json
{
  "id": "0bc5b350484d0367",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291363,
  "host_pid": "9e6742732c60:1",
  "hash": "e9b3e24c06f37b0947ebeee5b43586137e00df5c13803004fb6c0bbf035fb050",
  "cid": "QmV1e9b3e24c06f37b0947ebeee5b43586137e00df5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291363,
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
      "evaluated_at": 1760291363
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
  "sig": "b619a6341df6c0ecbde0a7f8ffde1da52c1861d25383f73fc0d67c33d3516db3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037692858
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 249, 'threshold': 50, 'total_amount': 32450178, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 248, 'first_seen': 1760284979, 'matching_hash': '7018b288608f6738'}}}