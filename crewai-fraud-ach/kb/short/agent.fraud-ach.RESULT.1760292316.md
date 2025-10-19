```json
{
  "id": "297677a076433831",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292316,
  "host_pid": "9e6742732c60:1",
  "hash": "5e92c1274d8ef151b94d2a2f13153772a99727e630c2ba9d8e3205387c9c927d",
  "cid": "QmV15e92c1274d8ef151b94d2a2f13153772a99727e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292316,
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
      "evaluated_at": 1760292316
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
  "sig": "38197cae815c97e78a00bf1c6c30d3999420f41a0fb9b7db7a34dc9898b53fd3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 24136710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}