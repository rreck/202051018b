```json
{
  "id": "e9f75b3863f57d1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291350,
  "host_pid": "9e6742732c60:1",
  "hash": "979fe58f4351b5db9546c8074f517b25c5433ea731afb7e10298e30a3638172d",
  "cid": "QmV1979fe58f4351b5db9546c8074f517b25c5433ea7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291350,
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
      "evaluated_at": 1760291350
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
  "sig": "d19b3e2419bf163c40191ed92911ae3b67e25cd506cf6fe2ade171350bbf75ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592351032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 36478953, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}