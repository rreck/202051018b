```json
{
  "id": "390829950000037e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293341,
  "host_pid": "9e6742732c60:1",
  "hash": "b8fe654748f445c072fa27c709a18540cefd8198a67698b563f87767f8da5413",
  "cid": "QmV1b8fe654748f445c072fa27c709a18540cefd8198",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293341,
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
      "evaluated_at": 1760293341
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
  "sig": "4cf0f898e5e5cc6defa4d3881207bebb5ced21daa7267c60865206f32f3e56e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021865843
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 54000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': '0e7cb19dffe9e37d'}}}