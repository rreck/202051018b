```json
{
  "id": "15e98f7a388d680f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290163,
  "host_pid": "9e6742732c60:1",
  "hash": "828b1e06b9cad8266a1883f8df85f6c27c033547f28c8a401658d558bfda968d",
  "cid": "QmV1828b1e06b9cad8266a1883f8df85f6c27c033547",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290163,
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
      "evaluated_at": 1760290163
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
  "sig": "1cf4b19591052859f8206f369ee69fd357de0b293a7e7d716a72a6e4cfff8390"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596849873
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 40814917, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'd03c8a9dd75ef277'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5513113}}}