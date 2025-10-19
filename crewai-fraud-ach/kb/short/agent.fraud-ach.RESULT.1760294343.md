```json
{
  "id": "f2424fa9b48f7d3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294343,
  "host_pid": "9e6742732c60:1",
  "hash": "2d120c5f57b9d792ca907049bbbe1bf614d128632678380766d278770c5e22b0",
  "cid": "QmV12d120c5f57b9d792ca907049bbbe1bf614d12863",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294343,
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
      "evaluated_at": 1760294343
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
  "sig": "79591eb7c72eca98aa9169397beebd51dc646985f0680b8e7f7b7a47e7820660"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 111496784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}