```json
{
  "id": "787157be6059a841",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288369,
  "host_pid": "9e6742732c60:1",
  "hash": "96c2613960325d4a76894e3a23f9636bdc2449ed0eb968984881fa06746b9f58",
  "cid": "QmV196c2613960325d4a76894e3a23f9636bdc2449ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288369,
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
      "evaluated_at": 1760288369
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
  "sig": "a05aa95330e31c9004e0ccddf81008400ac0051c2f5bc193ca607d3eda571d15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027745016
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 43488991, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}