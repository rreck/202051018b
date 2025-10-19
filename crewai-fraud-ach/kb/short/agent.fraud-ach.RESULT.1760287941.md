```json
{
  "id": "995e0d3b2a23768e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287941,
  "host_pid": "9e6742732c60:1",
  "hash": "6453fba734e64968c67588c3586562d58f0e7c97e59d5aedd88b1b76696cab29",
  "cid": "QmV16453fba734e64968c67588c3586562d58f0e7c97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287941,
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
      "evaluated_at": 1760287941
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
  "sig": "d5317accd80e733e2eb18ff92f2b89c1774ab0f7087bad5a3a8c3d7386e5f1a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597164999
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 13799170, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': 'b2fd55917469a01e'}}}