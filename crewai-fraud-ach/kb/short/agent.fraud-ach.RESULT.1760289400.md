```json
{
  "id": "840aba58a7155568",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289400,
  "host_pid": "9e6742732c60:1",
  "hash": "4a1bd9ec630d2218d666fb908e90a19a3bb62a21e1730d454105796f43b7ca30",
  "cid": "QmV14a1bd9ec630d2218d666fb908e90a19a3bb62a21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289400,
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
      "evaluated_at": 1760289400
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
  "sig": "db4c86b1f747e8478eeaf31a0f1423f2cc52100632e1a885d1f54abe1f4ab7b2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468078455
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50, 'total_amount': 54772266, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285764, 'matching_hash': '379f6acb9d31a698'}}}