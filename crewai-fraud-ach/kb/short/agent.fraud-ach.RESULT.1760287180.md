```json
{
  "id": "64d690cbaf15b067",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287180,
  "host_pid": "9e6742732c60:1",
  "hash": "3247c1f5b20673130a0d8b062595118e614fee4ae48cc4a7ccc39d35423953b3",
  "cid": "QmV13247c1f5b20673130a0d8b062595118e614fee4a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287180,
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
      "evaluated_at": 1760287180
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "69925fbb1b872973724758ac8982025eb23b0e3204e4162795dd994108563089"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150980279
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 11466840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': '8a0222b527408f48'}}}