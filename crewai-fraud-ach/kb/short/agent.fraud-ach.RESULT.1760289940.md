```json
{
  "id": "a31c8f290aa8f538",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289940,
  "host_pid": "9e6742732c60:1",
  "hash": "49cf02287e7663dcc1393448c0046bd5e66148f72940ff841d2dd8a6568b9d20",
  "cid": "QmV149cf02287e7663dcc1393448c0046bd5e66148f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289940,
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
      "evaluated_at": 1760289940
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
  "sig": "60a0d22034399d38dc41cb9495c37e71b0a106156ec917151cf2807dd13396e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596849873
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 39102403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'd03c8a9dd75ef277'}}}maly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 4.0, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7743228}}}