```json
{
  "id": "9dedafe7846e272c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291667,
  "host_pid": "9e6742732c60:1",
  "hash": "dee99fa6429561ed896b6e1f62b47c5116c114ed3cc9f3e5241687c5e4333a06",
  "cid": "QmV1dee99fa6429561ed896b6e1f62b47c5116c114ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291667,
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
      "evaluated_at": 1760291667
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
  "sig": "76d9072652f2ccfa59f7fd923398b52dffd3daa42c4d0d8db17a1f9145a77a8e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023360084
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 32199120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285763, 'matching_hash': 'bfec758d4b349e38'}}}