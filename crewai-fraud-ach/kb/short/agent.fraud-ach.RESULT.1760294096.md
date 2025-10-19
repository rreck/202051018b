```json
{
  "id": "cc19bd670f00b12a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294096,
  "host_pid": "9e6742732c60:1",
  "hash": "7539f8dc180f562b2986260af01723d9d3b687eb0330310a281945a9a71d8001",
  "cid": "QmV17539f8dc180f562b2986260af01723d9d3b687eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294096,
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
      "evaluated_at": 1760294096
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
  "sig": "e261ae13646e92c918ea92fb36ae87ea6e91091f4b3a8765d529c57af4325d71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 89736570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}