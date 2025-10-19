```json
{
  "id": "ef9db2e91e3ec083",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293184,
  "host_pid": "9e6742732c60:1",
  "hash": "b23f4f37318c8976da777eac7ccd3e6f18d2397c546709164261ba70dba231fe",
  "cid": "QmV1b23f4f37318c8976da777eac7ccd3e6f18d2397c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293184,
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
      "evaluated_at": 1760293184
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
  "sig": "e7d5e4e8716d5072b97945106c8dcc5b9be494d0adc7476f48b1f0d3504c7ca4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 51083790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '7b717df8c1c9c887'}}}