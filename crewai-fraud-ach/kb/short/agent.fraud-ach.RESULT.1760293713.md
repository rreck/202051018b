```json
{
  "id": "4852a384530d5c90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293713,
  "host_pid": "9e6742732c60:1",
  "hash": "78eeb229367b86997bbe1205a9cdf9ba6ea4f2e552bb9f85ce2d7873593046be",
  "cid": "QmV178eeb229367b86997bbe1205a9cdf9ba6ea4f2e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293713,
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
      "evaluated_at": 1760293713
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
  "sig": "269812f45b55255b4f02e337e6b9ce7f94bc770bf82a4bd43d20a29762f5b912"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026701294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 57714272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': 'c6488d75609f0f90'}}}