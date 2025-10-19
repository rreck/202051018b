```json
{
  "id": "3a6ef6b8be0503ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292010,
  "host_pid": "9e6742732c60:1",
  "hash": "3b94ac028c89a97f644fe12eb218ebfbc349ec7a425f9ba4b67c503d87104791",
  "cid": "QmV13b94ac028c89a97f644fe12eb218ebfbc349ec7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292010,
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
      "evaluated_at": 1760292010
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
  "sig": "5a55d36bac6a53603167abc7611100c4d69a90f6478c9ea2aa37a1d35dd3071e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595535562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 25417036, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '052e7693e8a3f40d'}}}