```json
{
  "id": "e228943001f26772",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286753,
  "host_pid": "9e6742732c60:1",
  "hash": "8e9c27af11db8b3efdd1602b514facc638f140d74aa6b63454c38ad58fea38af",
  "cid": "QmV18e9c27af11db8b3efdd1602b514facc638f140d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286753,
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
      "evaluated_at": 1760286753
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a975b8ea22c42cef05d8adfda00701d7f753bb79dfc9a70ebe703d13325953e8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000245124241
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11715228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285764, 'matching_hash': '1e6f1dd53bdf6417'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}