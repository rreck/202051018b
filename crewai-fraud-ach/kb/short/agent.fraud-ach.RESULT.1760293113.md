```json
{
  "id": "066ef4bfdcc2a667",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293113,
  "host_pid": "9e6742732c60:1",
  "hash": "bbf94ece88a32ce16463d3f345152c86c3b59d403f9db1ef2467fb345fcbbc38",
  "cid": "QmV1bbf94ece88a32ce16463d3f345152c86c3b59d40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293113,
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
      "evaluated_at": 1760293113
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
  "sig": "274e6fc6392d683f03f1c42c8f3968fee7356658fd9379bf3a0ce382c1f0412e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599553408
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 25301352, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '67e91645ed6012ef'}}}