```json
{
  "id": "50ffaecd0ef73db0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290011,
  "host_pid": "9e6742732c60:1",
  "hash": "2734ac3e638616a5227cafc83b74a1ee50b3767962616cfd434ed9002f46eb26",
  "cid": "QmV12734ac3e638616a5227cafc83b74a1ee50b37679",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290011,
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
      "evaluated_at": 1760290011
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
  "sig": "40606c92a03f0a5b22e0f3fc2ea8901f2f4b18a17c0d5e6c2d1b263592d2909c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153838694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 50331344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '9b5298dfc7691fa1'}}}