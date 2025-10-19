```json
{
  "id": "008119f39096f08c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287557,
  "host_pid": "9e6742732c60:1",
  "hash": "1062ebc4cdedb3efa3f453f2fc5392bb49a21210922a6546faad013f8c05cae8",
  "cid": "QmV11062ebc4cdedb3efa3f453f2fc5392bb49a21210",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287557,
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
      "evaluated_at": 1760287557
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
  "sig": "8ae79a2edaf63151b23bc21752a700c4c3917c153750a7f8f664939ee91acdae"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 111000025839448
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 24219328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': 'a0edb6bd92ae1076'}}}