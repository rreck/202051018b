```json
{
  "id": "962c28834f556d37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286797,
  "host_pid": "9e6742732c60:1",
  "hash": "ef5ef159e7fa5bbc7174ab6574e513c207aad94c033a7fce0a66eb7ecb39c0a1",
  "cid": "QmV1ef5ef159e7fa5bbc7174ab6574e513c207aad94c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286797,
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
      "evaluated_at": 1760286797
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "1d6646bfc3e38cc4d1f3c1dae987e189d2db8e4289a16596d8b7d9308ef26cf5"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11775176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 36, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}