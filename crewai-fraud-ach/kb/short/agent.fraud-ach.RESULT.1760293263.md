```json
{
  "id": "2ab38a3239321f32",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293263,
  "host_pid": "9e6742732c60:1",
  "hash": "5a426ab61657df692c9484302b92a24b884872fdf0e37db8a5e3cc18b486e404",
  "cid": "QmV15a426ab61657df692c9484302b92a24b884872fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293263,
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
      "evaluated_at": 1760293263
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
  "sig": "3310258e37343c05e05178719b5351838e93f501e9238c11551b37e73656c539"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 26612270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}