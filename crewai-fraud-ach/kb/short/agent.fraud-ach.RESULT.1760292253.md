```json
{
  "id": "af3b57cecb830e90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292253,
  "host_pid": "9e6742732c60:1",
  "hash": "2278c1ea26915b31ac622931dd2730b22c4f0fbbe27a9d9007018d80981019ba",
  "cid": "QmV12278c1ea26915b31ac622931dd2730b22c4f0fbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292253,
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
      "evaluated_at": 1760292253
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
  "sig": "dd7f877da62b58ab4d34e3ef9ef4b737eb41c5ab8ff16fca94218cfd7095c8f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 87370907, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}