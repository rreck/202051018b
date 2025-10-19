```json
{
  "id": "98a3128e578637ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292176,
  "host_pid": "9e6742732c60:1",
  "hash": "44eaf2f059a490b7a69caa035c2d9784a209f47717d8bc6d556b00b686a4dfac",
  "cid": "QmV144eaf2f059a490b7a69caa035c2d9784a209f477",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292176,
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
      "evaluated_at": 1760292176
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
  "sig": "953b7e495c836e26d6d99dbe836d430901b769695c4f7ec4c2f5a292af29a4a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275563549
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 81597120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': 'a33681b350a57503'}}}