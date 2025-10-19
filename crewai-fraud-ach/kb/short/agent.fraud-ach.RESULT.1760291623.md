```json
{
  "id": "ada95e88cb775ce5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291623,
  "host_pid": "9e6742732c60:1",
  "hash": "1f6af2614c3678b611126b7847f73427073fe89294b5b0002403177cc074057e",
  "cid": "QmV11f6af2614c3678b611126b7847f73427073fe892",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291623,
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
      "evaluated_at": 1760291623
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "a6706e1391771b79e89683da90de0375f66549e111a50c44b667c571174bd21c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 122105155421893
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 906228133, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': 'b50b947262955843'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5062727}}}