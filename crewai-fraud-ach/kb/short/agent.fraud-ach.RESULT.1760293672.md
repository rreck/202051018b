```json
{
  "id": "342cd85440a37d53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293672,
  "host_pid": "9e6742732c60:1",
  "hash": "1816307aa95011823a26d29d6c569f5ed2bee9c3f79f9baa7279bf0f124b99d3",
  "cid": "QmV11816307aa95011823a26d29d6c569f5ed2bee9c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293672,
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
      "evaluated_at": 1760293672
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
  "sig": "58cd4fb2215873c6e7ee9eee4d9590e1a6c75646928f0bdce06d0d12f26e64a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599696280
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 299, 'threshold': 50, 'total_amount': 71211335, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 298, 'first_seen': 1760284979, 'matching_hash': '32fd26aee1bbbffc'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6481360}}}