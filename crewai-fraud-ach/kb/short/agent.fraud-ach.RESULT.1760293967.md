```json
{
  "id": "3818ff23fb908266",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293967,
  "host_pid": "9e6742732c60:1",
  "hash": "b10b2e353f549aa2d7f8f244a5c7ce723a9e47687b41a26175d85e226ca84618",
  "cid": "QmV1b10b2e353f549aa2d7f8f244a5c7ce723a9e4768",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293967,
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
      "evaluated_at": 1760293967
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
  "sig": "7edf323d4a333d5234733dd2aae65f041ac342732c0854ee7de6b606d59cc94d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037688830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 58516828, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}