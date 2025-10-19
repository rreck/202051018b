```json
{
  "id": "9333015e3dd07176",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294549,
  "host_pid": "9e6742732c60:1",
  "hash": "7033d56f5a5a45d436b78176e5dd4c6a6edaec70db7771445f912056f4de5493",
  "cid": "QmV17033d56f5a5a45d436b78176e5dd4c6a6edaec70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294549,
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
      "evaluated_at": 1760294549
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
  "sig": "d958195d212a81ab20687e7e72fa51050655fd38c47432b4103d86584295ceb7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031437397
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 114471120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': 'dcc4ccfc6ce6722f'}}}