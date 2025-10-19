```json
{
  "id": "12017073546689e4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290128,
  "host_pid": "9e6742732c60:1",
  "hash": "f96d6c7ca79c1ea7946d887025312255946a100a6b12dcffd97a9036c6224043",
  "cid": "QmV1f96d6c7ca79c1ea7946d887025312255946a100a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290128,
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
      "evaluated_at": 1760290128
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
  "sig": "01703c0e62c9173d2e9a56241684c803551ce6bf9c61d4d6b639e7c021d764bc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596690593
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 30728190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}