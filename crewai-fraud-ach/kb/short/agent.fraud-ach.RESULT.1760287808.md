```json
{
  "id": "be3fbcdb0c65cc17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287808,
  "host_pid": "9e6742732c60:1",
  "hash": "ac68b04340f09e81658ab10d6ebb1d1df3dccf7be7d191efbfc36269ae994c75",
  "cid": "QmV1ac68b04340f09e81658ab10d6ebb1d1df3dccf7b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287808,
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
      "evaluated_at": 1760287808
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
  "sig": "16c9bc28e22f92f339622d725b04b71d8f1b63bd544f8a60b0517d2e26320ec8"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 23755879, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}