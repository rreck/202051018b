```json
{
  "id": "61ea28a97714978d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294623,
  "host_pid": "9e6742732c60:1",
  "hash": "0543a0f34f79585fd831e0428b417a453cecf8a51f767429d98dd9cfbc91b7c2",
  "cid": "QmV10543a0f34f79585fd831e0428b417a453cecf8a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294623,
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
      "evaluated_at": 1760294623
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
  "sig": "567df158cf2d75c1d10eaed96d439d9c26cbcf524fa3da96cbd32b4a11c1b2a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 27324098, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}