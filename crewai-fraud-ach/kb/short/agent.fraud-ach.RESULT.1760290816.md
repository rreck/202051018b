```json
{
  "id": "e458d8be8c50a1e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290816,
  "host_pid": "9e6742732c60:1",
  "hash": "6015382a75129ad92e416d72b6c99d125ffb9fd6b86c741e951c24183dd23dc0",
  "cid": "QmV16015382a75129ad92e416d72b6c99d125ffb9fd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290816,
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
      "evaluated_at": 1760290816
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
  "sig": "b6d5b52efe0fe81acabfcdc9423d0d0792950344922fea83d04f04a59d4ba71f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 46829280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}