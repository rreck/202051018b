```json
{
  "id": "94a24c65b6356356",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288158,
  "host_pid": "9e6742732c60:1",
  "hash": "e0dc970c514bfc4b02d84bb3b32d1822437022abc15a50cac2b6dc956a356dda",
  "cid": "QmV1e0dc970c514bfc4b02d84bb3b32d1822437022ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288158,
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
      "evaluated_at": 1760288158
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
  "sig": "6f6d186cbbc355bf4c034bded396f10a2c79497de35962ea664c7170af74d64c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 26254284, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}