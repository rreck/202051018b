```json
{
  "id": "2f72144909deb606",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294651,
  "host_pid": "9e6742732c60:1",
  "hash": "2d5bc7c5be8bf08c8fc072f7f6547a667aef8241f04ec401216615ab6e516eaf",
  "cid": "QmV12d5bc7c5be8bf08c8fc072f7f6547a667aef8241",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294651,
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
      "evaluated_at": 1760294651
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
  "sig": "877deb6807448e747ea57ba63cfadbd78f21cb1cc992fc7b3bcb40207b298682"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461662622
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 46492072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '96e0bea374e50243'}}}