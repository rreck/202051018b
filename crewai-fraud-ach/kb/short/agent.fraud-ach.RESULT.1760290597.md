```json
{
  "id": "16edb864417b8d1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290597,
  "host_pid": "9e6742732c60:1",
  "hash": "81e2c4315a243533340ae201f6735af051812c618c05e3e8a952d118a39dfcee",
  "cid": "QmV181e2c4315a243533340ae201f6735af051812c61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290597,
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
      "evaluated_at": 1760290597
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
  "sig": "a95fc35e9aafe2f6c94c215c210dfca76c07e9b65f1e0c7ed5e4e6ce2bb6429c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023386962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 15400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}