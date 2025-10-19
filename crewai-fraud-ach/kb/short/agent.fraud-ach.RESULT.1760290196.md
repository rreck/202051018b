```json
{
  "id": "988ba14be9a3441d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290196,
  "host_pid": "9e6742732c60:1",
  "hash": "f26a4e294d609bf18975cce35b01196689e8c262275e376544f700d2fc3058d2",
  "cid": "QmV1f26a4e294d609bf18975cce35b01196689e8c262",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290196,
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
      "evaluated_at": 1760290196
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
  "sig": "6af011a748cf1e2ba8ea9a5267f201a8fbc4ea1cb6fd7ed74bf33043b137d05c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021906357
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 63041328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': '507361b82f38c481'}}}