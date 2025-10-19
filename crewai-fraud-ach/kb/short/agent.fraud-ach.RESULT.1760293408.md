```json
{
  "id": "b6edc6924d88b312",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293408,
  "host_pid": "9e6742732c60:1",
  "hash": "d11c0c5f21d22be146f85509050c6db46d0b0c815eb402ea435fc0418c8bdec6",
  "cid": "QmV1d11c0c5f21d22be146f85509050c6db46d0b0c81",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293408,
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
      "evaluated_at": 1760293408
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
  "sig": "f3c9cf1ce02f61e2d59e5e8c6f9297cd78c88be8bb4ce6a14e408cf235527ea9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596892918
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 54754624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'c247331c92498799'}}}