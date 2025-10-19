```json
{
  "id": "24a638adb84088fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293789,
  "host_pid": "9e6742732c60:1",
  "hash": "abf83f765e27ae8119a7f715e6910106592bd063741c96b2a07f7d0a12d9af81",
  "cid": "QmV1abf83f765e27ae8119a7f715e6910106592bd063",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293789,
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
      "evaluated_at": 1760293789
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
  "sig": "ab677de96214218f025b030680f8f02489eecb722edfe188f953c3a8ff60ee21"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 71605800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}