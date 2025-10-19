```json
{
  "id": "b314efcd4a7b21aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294092,
  "host_pid": "9e6742732c60:1",
  "hash": "2c543afc84712792e7be6c1c71cc17f21d2201016efe2ba268af25cbf760a664",
  "cid": "QmV12c543afc84712792e7be6c1c71cc17f21d220101",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294092,
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
      "evaluated_at": 1760294092
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
  "sig": "becafce46f87722cd1aa4c79c0641f198dfe722225e890d7ad212b79af927266"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246289995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 24188472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '1ab4d10c626d0dd7'}}}