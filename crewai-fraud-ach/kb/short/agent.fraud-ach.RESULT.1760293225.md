```json
{
  "id": "f32a3d894f8f3b66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293225,
  "host_pid": "9e6742732c60:1",
  "hash": "9583ce94b6f217ab7f4e576c638f60786e748a9432d8c6dc147ce368cdc815df",
  "cid": "QmV19583ce94b6f217ab7f4e576c638f60786e748a94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293225,
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
      "evaluated_at": 1760293225
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
  "sig": "15ea32d99f8e7b47823f0d9f47c7efeb9ad5b24cc121f39c0d7baf398b1f2a48"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 73778212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}