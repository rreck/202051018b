```json
{
  "id": "bb9eabed6486b2f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288344,
  "host_pid": "9e6742732c60:1",
  "hash": "3558b08ea5fa4bcc943a628d9c9a27f0e04de9baeda15753c50d1e3c1368773d",
  "cid": "QmV13558b08ea5fa4bcc943a628d9c9a27f0e04de9ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288344,
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
      "evaluated_at": 1760288344
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
  "sig": "32c02bb71d027dbf6bb6284c57acde8908aaef89100f376b37059bc3fdbba649"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021718881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 11777670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'c5f4c03352e0db07'}}}