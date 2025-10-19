```json
{
  "id": "37bfefde8835ff61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285670,
  "host_pid": "9e6742732c60:1",
  "hash": "8b40199e006f5007172b8cd883784fff648989c6811d2f418959fc036898387d",
  "cid": "QmV18b40199e006f5007172b8cd883784fff648989c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285670,
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
      "evaluated_at": 1760285670
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
  "sig": "7ab0c5bb1d3e17209072b7ed1d72c95378989b6cb20ed31b814f8c02e8715e56"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 28654792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}