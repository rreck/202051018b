```json
{
  "id": "350e4cff26b3430b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291378,
  "host_pid": "9e6742732c60:1",
  "hash": "3a5be9b6ddd3ee9bfb1c35074406ea6e532cf9f27091a5b8b97252b958b1abfb",
  "cid": "QmV13a5be9b6ddd3ee9bfb1c35074406ea6e532cf9f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291378,
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
      "evaluated_at": 1760291378
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
  "sig": "55c44891e62860c007f29b10b12f998690bedbd4da560a4e141f365b06d415d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 55056904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}