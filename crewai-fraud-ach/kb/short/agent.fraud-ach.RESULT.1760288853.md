```json
{
  "id": "d30630b771c433aa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288853,
  "host_pid": "9e6742732c60:1",
  "hash": "dc9ffc3ded93364a2788447b5b2607b60e707864b2b99520f7e3be43e911a2a8",
  "cid": "QmV1dc9ffc3ded93364a2788447b5b2607b60e707864",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288853,
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
      "evaluated_at": 1760288853
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
  "sig": "d43578e3ecb74a49c321182662d9ae551fd915453e487d37684ef254cdbe6d9d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032435684
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 11789108, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '191acc35d8c1baac'}}}aly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.93, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9380590}}}