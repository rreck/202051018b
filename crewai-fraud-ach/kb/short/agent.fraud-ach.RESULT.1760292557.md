```json
{
  "id": "e733e45a04fc8405",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292557,
  "host_pid": "9e6742732c60:1",
  "hash": "5d205174f974a8472528109fc08fc6dc566bf7dd46e6a66f54a214363ba1d8b4",
  "cid": "QmV15d205174f974a8472528109fc08fc6dc566bf7dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292557,
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
      "evaluated_at": 1760292557
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
  "sig": "c3dbe8398b89f0b2b9db98e2cab5b546c92389941abf3896d75c6d7ad83c406b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270359022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 44690600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}