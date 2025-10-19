```json
{
  "id": "f3e94577aeb35cc8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290915,
  "host_pid": "9e6742732c60:1",
  "hash": "650e35a31e6f6c7a15d83b32143465c5293730014b6726972a51dd552f9966db",
  "cid": "QmV1650e35a31e6f6c7a15d83b32143465c529373001",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290915,
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
      "evaluated_at": 1760290915
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
  "sig": "92e2bd2487c184d441146b7e7cfe68d054edf771347cfebee46055d796310ba2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 60422598, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}