```json
{
  "id": "2faad1725f331e23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290717,
  "host_pid": "9e6742732c60:1",
  "hash": "b5b2d59675ea89c590bdc6c3098f42fa39c2a2a4eb913b1643bc4dbbc0171c2f",
  "cid": "QmV1b5b2d59675ea89c590bdc6c3098f42fa39c2a2a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290717,
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
      "evaluated_at": 1760290717
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
  "sig": "ca8992448673d635d5a15a3571dd62538f17ce3e5b99fb403b6413db29db8cc8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 60869685, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}