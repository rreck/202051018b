```json
{
  "id": "ef09a274563441b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288062,
  "host_pid": "9e6742732c60:1",
  "hash": "e599c037a66480bd73fa6cb91526e48a122553cacf1e8ba6a8de0297313880bf",
  "cid": "QmV1e599c037a66480bd73fa6cb91526e48a122553ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288062,
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
      "evaluated_at": 1760288062
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
  "sig": "221c51a9489a05e6406bdf104fa6c6fbf289d0dc6b494f493a11c8bfdb110269"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 40484124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}