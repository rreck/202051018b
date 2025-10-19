```json
{
  "id": "bd2845d140f07166",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292044,
  "host_pid": "9e6742732c60:1",
  "hash": "a5868eb278b3406a97e5dca0f56527351ac951aaa2e2e1738047e8475cce939a",
  "cid": "QmV1a5868eb278b3406a97e5dca0f56527351ac951aa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292044,
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
      "evaluated_at": 1760292044
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
  "sig": "6dbf09283833eeb0e72520098d58984ec53d6360fe5fa91039441c2acfaf9e8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155862167
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 18900000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '207d73478b089b6e'}}}maly': {'fraud_detected': True, 'risk_score': 88, 'details': {'zscore': 4.85, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9237211}}}