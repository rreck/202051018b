```json
{
  "id": "11bd59017ece95a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289936,
  "host_pid": "9e6742732c60:1",
  "hash": "ca8de27de2599e72cab269e92714164355c89ea6e4ac0005c82b1cc8e2777bee",
  "cid": "QmV1ca8de27de2599e72cab269e92714164355c89ea6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289936,
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
      "evaluated_at": 1760289936
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
  "sig": "eb7eca2daa056b7cd531993b27314623a21bc04a4802c52a07df457e88604d0a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277234112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 51650096, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': '11106d4d9e5d055e'}}}aly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6178432}}}