```json
{
  "id": "26c515b91268d2a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293265,
  "host_pid": "9e6742732c60:1",
  "hash": "b9a72a5703e8a5e3d1a645a16998daa950f12e1601d074a68cb4cb1ded10d9a6",
  "cid": "QmV1b9a72a5703e8a5e3d1a645a16998daa950f12e16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293265,
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
      "evaluated_at": 1760293265
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
  "sig": "4cd45b1307fb25855942f898eae9fb01a13e8d5cb57982f657adc5764eda7f07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032341010
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 22936200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': 'f26a81694d784881'}}}