```json
{
  "id": "5e200685408eba4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291567,
  "host_pid": "9e6742732c60:1",
  "hash": "f632ccfef038efbb3c39281cb8557196757d59a65e5561df0289ca2c4b802801",
  "cid": "QmV1f632ccfef038efbb3c39281cb8557196757d59a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291567,
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
      "evaluated_at": 1760291567
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
  "sig": "44ba82ef44aba7918f370edfcbab0190cefcf7ed698d0b946c0c4615ed9a517b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 78361474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9245331}}}