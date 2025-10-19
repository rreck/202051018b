```json
{
  "id": "beb9bb1d7f074cd0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293605,
  "host_pid": "9e6742732c60:1",
  "hash": "bb528ec81c66f068464a4678650bc89ab69c5150fc859aaab6e47e6bef735753",
  "cid": "QmV1bb528ec81c66f068464a4678650bc89ab69c5150",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293605,
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
      "evaluated_at": 1760293605
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
  "sig": "d36dca45fe069ad985af2fe28131bb94dce6bcfa58ce705792730d41355c059e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592351032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 46811142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}