```json
{
  "id": "2ce89bb36309f26d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294599,
  "host_pid": "9e6742732c60:1",
  "hash": "a280b0e07a3250d0a5ff6fd25159c73d70dd7cb54a5e964e825bfb6eab94e1f1",
  "cid": "QmV1a280b0e07a3250d0a5ff6fd25159c73d70dd7cb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294599,
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
      "evaluated_at": 1760294599
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
  "sig": "d8fe544577b93a3e7d45d32e80fa92382d956c8d03cc80bb0ec485427cadf34b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020947870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 16261234, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}