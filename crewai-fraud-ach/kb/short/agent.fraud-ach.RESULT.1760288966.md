```json
{
  "id": "c727f0bf594515f9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288966,
  "host_pid": "9e6742732c60:1",
  "hash": "1c6eb5501c8c298d665fb9cf434d80fc7af69fd6dd79440cadec2cf84bd69dcf",
  "cid": "QmV11c6eb5501c8c298d665fb9cf434d80fc7af69fd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288966,
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
      "evaluated_at": 1760288966
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
  "sig": "0a553a9ec9a45108aec13aeaea5b5dec1af8fb6cc52f9103b7eb37429e5fbdd6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599905929
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 42343230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': 'da08c58383816f07'}}}