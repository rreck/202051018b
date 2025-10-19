```json
{
  "id": "73fee802bb1794a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293374,
  "host_pid": "9e6742732c60:1",
  "hash": "db03115fb941f7e8f7751ba14f092f35370f68b1041bdad7ba8988770a6575f3",
  "cid": "QmV1db03115fb941f7e8f7751ba14f092f35370f68b1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293374,
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
      "evaluated_at": 1760293374
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
  "sig": "d9dd9ef670f760ac21dbca9e374ea67d300e91960991e5a65f40310218475374"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465949521
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 84612640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '5db5b45722d53397'}}}