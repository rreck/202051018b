```json
{
  "id": "9f68512a71e9f8c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291151,
  "host_pid": "9e6742732c60:1",
  "hash": "2ab9c04c6fec8835eba59204914b2d2f2f4b856e502393673c8a9034ecd5751e",
  "cid": "QmV12ab9c04c6fec8835eba59204914b2d2f2f4b856e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291151,
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
      "evaluated_at": 1760291151
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
  "sig": "62b81c7821e24e96b040faf55bffc08088cecabadf7db79a739a7b5b86e71d35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460612944
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 55268304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': 'ecd204bdadc44322'}}}